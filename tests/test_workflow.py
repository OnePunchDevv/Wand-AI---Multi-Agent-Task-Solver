import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from app.main import app


# Client fixture for tests
@pytest_asyncio.fixture(scope="function")
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://testserver") as ac:
        yield ac


@pytest.mark.asyncio
async def test_submit_and_get_workflow(client):
    # Submit a new workflow
    workflow_data = {"name": "Test Workflow", "steps": ["step1", "step2"]}
    response = await client.post("/workflows/", json=workflow_data)
    assert response.status_code == 200
    result = response.json()
    assert "workflow_id" in result
    assert result["status"] == "PENDING"

    workflow_id = result["workflow_id"]

    # Retrieve the workflow by ID
    response = await client.get(f"/workflows/{workflow_id}")
    assert response.status_code == 200
    result = response.json()
    assert result["status"] == "PENDING"
    assert result["definition"] == workflow_data
