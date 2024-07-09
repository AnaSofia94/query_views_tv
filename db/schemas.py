from pydantic import BaseModel


class AnalysisResultBase(BaseModel):
    content_id: str
    actual_label: str
    predicted_label: str
    feature_vector: str
    tvshow: str

    class Config:
        orm_mode = True


class AnalysisResultCreate(AnalysisResultBase):
    pass


class AnalysisResult(AnalysisResultBase):
    id: int
