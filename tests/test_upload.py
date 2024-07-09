import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_upload_file():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        files = {'file': ('test.csv', 'content_id,actual_label,predicted_label,feature_vector,tvshow\n1,label1,label2,"0.1,0.2,0.3","show1"\n')}
        response = await ac.post("/api/v1/uploadfile/", files=files, headers={"Authorization": "test_api_key"})
    assert response.status_code == 200
    assert response.json() == {"message": "File uploaded and DataFrame created successfully"}