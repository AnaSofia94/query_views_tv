import logging
from typing import Optional

import numpy as np
from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
from sqlalchemy.orm import Session
from db.models import AnalysisResult
from globals import data_frame_manager

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def cluster_videos_service(n_clusters: int):
    try:
        logging.info(f"Clustering videos into {n_clusters} clusters.")
        df = data_frame_manager.get_dataframe()
        logging.info(f"DataFrame shape: {df.shape}")

        all_vectors = df['feature_vector'].apply(lambda x: list(map(float, x.strip().split(',')))).tolist()
        all_vectors = np.array(all_vectors)

        kmeans = KMeans(n_clusters=n_clusters)
        df['cluster'] = kmeans.fit_predict(all_vectors)
        logging.info(f"Clustering completed. Head of the DataFrame: {df.head()}")

        return df[['content_id', 'cluster']].to_dict(orient="records")
    except Exception as e:
        logging.error(f"Error clustering videos: {e}")
        return {"message": f"Error clustering videos: {str(e)}"}


def classify_videos_service():
    try:
        logging.info("Classifying videos.")
        df = data_frame_manager.get_dataframe()
        logging.info(f"DataFrame shape: {df.shape}")

        all_vectors = df['feature_vector'].apply(lambda x: list(map(float, x.strip().split(',')))).tolist()
        all_vectors = np.array(all_vectors)

        X = all_vectors
        y = df['actual_label']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        logging.info(f"Training set size: {X_train.shape}, Test set size: {X_test.shape}")

        classifier = RandomForestClassifier()
        classifier.fit(X_train, y_train)
        logging.info("Classifier training completed.")

        y_pred = classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        logging.info(f"Classification accuracy: {accuracy}")

        return {"classification_accuracy": accuracy}
    except Exception as e:
        logging.error(f"Error classifying videos: {e}")
        return {"message": f"Error classifying videos: {str(e)}"}


def analyze_data_service(db: Session, actual_label: Optional[str]):
    try:
        logging.info(f"Analyzing data with actual_label: {actual_label}")
        df = data_frame_manager.get_dataframe()
        logging.info(f"Accessing DataFrame in analyze: {df.head()}")

        if df.empty:
            logging.warning("Data not loaded.")
            return {"message": "Data not loaded"}

        if actual_label:
            df = df[df['actual_label'] == actual_label]
            if df.empty:
                logging.warning(f"No data found for actual_label: {actual_label}")
                return {"message": f"No data found for actual_label: {actual_label}"}

        label_counts = df['actual_label'].value_counts().to_dict()
        logging.info(f"Label counts: {label_counts}")

        for index, row in df.iterrows():
            result = AnalysisResult(
                content_id=row['content_id'],
                actual_label=row['actual_label'],
                predicted_label=row['predicted_label'],
                feature_vector=row['feature_vector'],
                tvshow=row['tvshow']
            )
            db.add(result)
        db.commit()
        logging.info("Analysis performed and results saved to database.")

        return {"message": "Analysis performed and results saved to database", "label_counts": label_counts}
    except Exception as e:
        logging.error(f"Error analyzing data: {e}")
        return {"message": f"Error analyzing data: {str(e)}"}


def get_results_service(db: Session):
    try:
        logging.info("Fetching results from database.")
        results = db.query(AnalysisResult).all()
        logging.info(f"Number of results fetched: {len(results)}")
        return results
    except Exception as e:
        logging.error(f"Error fetching results: {e}")
        return {"message": f"Error fetching results: {str(e)}"}


def compute_similarity_service(video_id: str):
    try:
        logging.info(f"Computing similarity for video ID: {video_id}")
        df = data_frame_manager.get_dataframe()
        vector = df.loc[df['content_id'] == video_id, 'feature_vector'].values
        if len(vector) == 0:
            logging.warning("Video ID not found.")
            return {"message": "Video ID not found"}

        vector = np.array([list(map(float, vector[0].split(',')))])
        all_vectors = df['feature_vector'].apply(lambda x: list(map(float, x.split(',')))).tolist()
        all_vectors = np.array(all_vectors)

        similarities = cosine_similarity(vector, all_vectors)
        df['similarity'] = similarities[0]

        similar_videos = df.sort_values(by='similarity', ascending=False).head(10)
        logging.info("Similarity computation completed.")
        return similar_videos[['content_id', 'similarity']].to_dict(orient="records")
    except Exception as e:
        logging.error(f"Error computing similarity: {e}")
        return {"message": f"Error computing similarity: {str(e)}"}
