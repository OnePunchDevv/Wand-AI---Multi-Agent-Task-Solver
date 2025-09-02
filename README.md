# FastAPI Workflows Test Project

A minimal FastAPI service that lets you define and track simple workflows, with agents, tools suporting retries and timeouts.

---

## Features

- Submit a workflow definition (`/workflows/`)
- Retrieve workflow state by ID (`/workflows/{id}`)
- Uses **Pydantic models** for workflow specs and runs
- Includes **pytest** tests for endpoints

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
