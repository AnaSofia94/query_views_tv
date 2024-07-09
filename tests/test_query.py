import os
import pytest
from httpx import AsyncClient
from main import app


@pytest.mark.asyncio
async def test_filter_by_predicted_label():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Assuming some data has already been uploaded and analyzed
        response = await ac.get("/api/v1/filter_by_predicted_label/?predicted_label=Undefined",
                                headers={"Authorization": os.getenv("API_KEY")})
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    for item in response.json():
        assert "content_id" in item
        assert "actual_label" in item
        assert "predicted_label" in item
        assert "feature_vector" in item
        assert "tvshow" in item
        assert item["predicted_label"] == "Undefined"
