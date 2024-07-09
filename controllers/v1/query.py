from fastapi import APIRouter, Depends, Query
from typing import List
from sqlalchemy.orm import Session
from db.session import get_db
from db.schemas import AnalysisResult as AnalysisResultSchema
from core.security import verify_api_key
from services.query import filter_by_predicted_label_service

router = APIRouter()


@router.get("/filter_by_predicted_label/", response_model=List[AnalysisResultSchema],
            dependencies=[Depends(verify_api_key)])
def filter_by_predicted_label(predicted_label: str, db: Session = Depends(get_db)) -> List[AnalysisResultSchema]:
    return filter_by_predicted_label_service(predicted_label, db)
