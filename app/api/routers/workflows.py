from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from uuid import uuid4
from app.models.workflow import WorkflowSpec, WorkflowRun
from app.orchestration.engine import WorkflowManager

router = APIRouter()
orchestrator = WorkflowManager()

@router.post("/", response_model=WorkflowRun)
async def submit_workflow(spec: WorkflowSpec):
    """Accept a workflow definition and create a new run record."""
    workflow_id = str(uuid4())
    return await orchestrator.start(workflow_id, spec)


@router.get("/{workflow_id}", response_model=WorkflowRun)
async def get_workflow(workflow_id: str):
    """Retrieve a workflow run by ID."""
    run = orchestrator.fetch_execution(workflow_id)
    if not run:
        raise HTTPException(status_code=404, detail="Workflow not found")
    return JSONResponse(content=run.model_dump())
