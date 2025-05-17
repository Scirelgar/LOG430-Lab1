import pytest
from httpx import AsyncClient
from fastapi import status
from ..src import main


@pytest.mark.asyncio
async def test_root_status_code():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.asyncio
async def test_root_response_content():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/")
    assert response.json() == {"message": "Hello World"}
