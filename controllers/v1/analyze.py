from fastapi import APIRouter, Depends, Query
from typing import Optional
from sqlalchemy.orm import Session
from core.security import verify_api_key
from services.analyze import (
    cluster_videos_service,
    classify_videos_service,
    analyze_data_service,
    get_results_service,
    compute_similarity_service
)
from db.session import get_db

router = APIRouter()


@router.get("/cluster/", dependencies=[Depends(verify_api_key)])
def cluster_videos(n_clusters: int = 5):
    return cluster_videos_service(n_clusters)


@router.get("/classify/", dependencies=[Depends(verify_api_key)])
def classify_videos():
    return classify_videos_service()


@router.post("/analyze/", dependencies=[Depends(verify_api_key)])
def analyze_data(db: Session = Depends(get_db), actual_label: Optional[str] = Query(None)):
    return analyze_data_service(db, actual_label)


@router.get("/results/", dependencies=[Depends(verify_api_key)])
def get_results(db: Session = Depends(get_db)):
    return get_results_service(db)


@router.get("/similarity/", dependencies=[Depends(verify_api_key)])
def compute_similarity(video_id: str):
    return compute_similarity_service(video_id)
