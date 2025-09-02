# FastAPI Workflows Test Project

A minimal FastAPI service that lets you define and track simple workflows, with agents, tools suporting retries and timeouts.

---

## Features

- Submit a workflow definition (`/workflows/`)
- Retrieve workflow state by ID (`/workflows/{id}`)
- Uses **Pydantic models** for workflow specs and runs
- Includes **pytest** tests for endpoints

---

## Design Decisions

- **FastAPI as the framework**  
  Chosen for its async support and type safety with Pydantic.

- **Router-based organization**  
  Split endpoints into `health` and `workflows` routers for clarity and scalability.

- **Pydantic models for contracts**  
  Used `WorkflowSpec` and `WorkflowRun` to enforce schema validation and keep request/response strict.

- **In-memory state store**  
  A simple Python dict holds workflow runs. This keeps the prototype lightweight while leaving room for later DB integration.

- **Status tracking**  
  Each workflow has an overall `status` (`PENDING`) and per-task status mapping, providing a foundation for future execution logic.

- **Minimal dependencies**  
  Only FastAPI, Uvicorn, HTTPX, and Pytest are required — avoiding complexity and making setup trivial.

- **Tests-first approach**  
  Both health and workflows have pytest-based integration tests to validate endpoints early.

---

## Endpoints

### Health
- **GET** `/health`  
  Returns `{"status": "ok"}` if the service is up.

### Workflows
- **POST** `/workflows/`  
  Submit a workflow definition.  
  **Request body:**
  ```json
  @examples/sample_workflow.json
  ```

> **Response:**

```json
{
  "run_id": "d63f64de-b0fd-41d8-bc41-3d8b91a8cabc",
  "status": "PENDING"
  ...
}
```

* **GET** `/workflows/{run_id}`
  Retrieve workflow state by ID.
  **Response example:**

  ```json
    {
    "run_id": "b6329dae-55c2-4cbd-b367-d6f88e3abd39",
    "status": "COMPLETED",
    "nodes": {
        ...
    }
  ```

---

## Project Structure

```
app/
  ├── api/
  │   └── routers/
  │       ├── health.py
  │       └── workflows.py
  ├── models/
  │   └── workflows.py
  ├── tools/
  │   └── base.py
  │   └── ...
  └── main.py
tests/
  ├── test_health.py
  └── test_workflows.py
```

---

## Trade-offs (due to 24h constraint)

To keep the project lightweight and finish within one day, we made the following trade-offs:

- **In-memory storage only**  
  No database — all workflows reset on server restart.

- **No logging / monitoring**  
  Skipped structured logging and metrics to reduce boilerplate.

- **Minimal API surface**  
  Only `health`, `submit workflow`, and `get workflow` endpoints implemented.

- **No workflow execution engine**  
  Workflows are stored and tracked, but not executed.

- **Simplified models**  
  Basic Pydantic schemas only — no versioning or advanced validation.

These choices allow the project to be **readable, testable, and demo-ready quickly**.

---

## Getting Started

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
uvicorn app.main:app --reload
```


### 3. Run tests

```bash
pytest -v
```
