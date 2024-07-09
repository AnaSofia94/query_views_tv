# TV Data Show FastAPI Project

This project is a FastAPI application for managing and analyzing TV show data. The application supports uploading data, analyzing it, clustering, classification, and more.

## Project Structure

    tv_data_show/
    ├── controllers/
    │   ├── v1/
    │   │   ├── init.py
    │   │   ├── analyze.py
    │   │   ├── query.py
    │   │   ├── upload.py
    │   ├── init.py
    ├── core/
    │   ├── init.py
    │   ├── config.py
    │   ├── security.py
    ├── db/
    │   ├── init.py
    │   ├── base.py
    │   ├── models.py
    │   ├── schemas.py
    │   ├── session.py
    ├── services/
    │   ├── init.py
    │   ├── analyze.py
    │   ├── upload.py
    │   ├── query.py
    ├── globals.py
    ├── main.py
    ├── generate_api_key.py
    ├── interview_data.db
    ├── test.db
    ├── requirements.txt
    ├── Dockerfile
    ├── .env
    └── tests/
        ├── init.py
        ├── conftest.py
        ├── test_main.py
        ├── test_analyze.py
        ├── test_query.py
        ├── test_upload.py

## Setup and Installation

### Prerequisites

- Docker
- Python 3.11
- pip

### Environment Variables

Create a `.env` file in the root of your project with the following content:

API_KEY=your_api_key_here

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/tv_data_show.git
    cd tv_data_show
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Generate an API key:**

    You can generate an API key manually and place it in the `.env` file or use the provided script:

    ```bash
    python generate_api_key.py
    ```

    This will create an `api_key.txt` file. Move the API key from `api_key.txt` to your `.env` file.

### Running the Application

#### Using Docker

1. **Build the Docker image:**

    ```bash
    docker build -t tv_data_show:latest .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 --env-file .env tv_data_show:latest
    ```

#### Using Python

1. **Run the application:**

    ```bash
    uvicorn main:app --reload
    ```

## Project Functionality

### Uploading Data

Endpoint: `/api/v1/uploadfile/`

- Method: `POST`
- Description: Upload a CSV file containing TV show data.
- Example:

    ```bash
    curl -X POST "http://127.0.0.1:8000/api/v1/uploadfile/" -F "file=@path_to_your_file.csv" -H "Authorization: your_api_key"
    ```

### Analyzing Data

Endpoint: `/api/v1/analyze/`

- Method: `POST`
- Description: Analyze the uploaded data.
- Example:

    ```bash
    curl -X POST "http://127.0.0.1:8000/api/v1/analyze/" -H "Authorization: your_api_key"
    ```

### Fetching Results

Endpoint: `/api/v1/results/`

- Method: `GET`
- Description: Fetch the analysis results.
- Example:

    ```bash
    curl -X GET "http://127.0.0.1:8000/api/v1/results/" -H "Authorization: your_api_key"
    ```

### Computing Similarity

Endpoint: `/api/v1/similarity/`

- Method: `GET`
- Description: Compute the similarity of a given video ID with other videos.
- Example:

    ```bash
    curl -X GET "http://127.0.0.1:8000/api/v1/similarity/?video_id=YourVideoID" -H "Authorization: your_api_key"
    ```

### Clustering Videos

Endpoint: `/api/v1/cluster/`

- Method: `GET`
- Description: Cluster the videos into a specified number of clusters.
- Example:

    ```bash
    curl -X GET "http://127.0.0.1:8000/api/v1/cluster/?n_clusters=5" -H "Authorization: your_api_key"
    ```

### Classifying Videos

Endpoint: `/api/v1/classify/`

- Method: `GET`
- Description: Classify the videos based on their features.
- Example:

    ```bash
    curl -X GET "http://127.0.0.1:8000/api/v1/classify/" -H "Authorization: your_api_key"
    ```

## Testing

### Running Tests

1. **Install test dependencies:**

    ```bash
    pip install pytest httpx python-dotenv
    ```

2. **Run the tests:**

    ```bash
    pytest
    ```

### Test Files

- `tests/conftest.py`: Sets up environment variables for tests.
- `tests/test_main.py`: Tests the main endpoints.
- `tests/test_analyze.py`: Tests the analyze functionality.
- `tests/test_query.py`: Tests the query functionality.
- `tests/test_upload.py`: Tests the upload functionality.


