from sqlalchemy import Column, Integer, String
from db.base import Base

class AnalysisResult(Base):
    __tablename__ = 'analysis_results'

    id = Column(Integer, primary_key=True, index=True)
    content_id = Column(String, index=True)
    actual_label = Column(String)
    predicted_label = Column(String)
    feature_vector = Column(String)
    tvshow = Column(String)