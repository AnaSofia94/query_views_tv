import pytest
from httpx import AsyncClient
from main import app

@pytest.mark.asyncio
async def test_analyze_data():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v1/analyze/", headers={"Authorization": "your_generated_api_key_here"})
    assert response.status_code == 200
    assert "message" in response.json()
    assert "label_counts" in response.json()