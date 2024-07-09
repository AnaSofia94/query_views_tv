from sqlalchemy.orm import Session
from db.models import AnalysisResult as AnalysisResultModel
from db.schemas import AnalysisResult as AnalysisResultSchema
from typing import List

def filter_by_predicted_label_service(predicted_label: str, db: Session) -> List[AnalysisResultSchema]:
    results = db.query(AnalysisResultModel).filter(AnalysisResultModel.predicted_label == predicted_label).all()
    return results