from fastapi import APIRouter, UploadFile, Depends
from core.security import verify_api_key
from services.upload import process_uploaded_file

router = APIRouter()


@router.post("/uploadfile/", dependencies=[Depends(verify_api_key)])
async def upload_file(file: UploadFile):
    await process_uploaded_file(file)
    return {"message": "File uploaded and DataFrame created successfully"}
