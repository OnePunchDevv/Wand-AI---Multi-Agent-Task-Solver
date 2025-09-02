from fastapi import APIRouter
from uuid import uuid4


router = APIRouter()

# In-memory store for now
WORKFLOWS = {}


@router.post("/")
async def submit_workflow(workflow: dict):
    """
    Accept a workflow definition and return a workflow_id.
    Right now, we just save the raw dict in memory.
    """
    workflow_id = str(uuid4())
    WORKFLOWS[workflow_id] = {"status": "PENDING", "definition": workflow}
    return {"workflow_id": workflow_id, "status": "PENDING"}


@router.get("/{workflow_id}")
async def get_workflow_status(workflow_id: str):
    """
    Retrieve workflow status and details.
    """
    workflow = WORKFLOWS.get(workflow_id, None)
    if not workflow:
        return {"error": "Workflow not found"}
    return workflow

