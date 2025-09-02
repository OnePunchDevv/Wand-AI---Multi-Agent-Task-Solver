from fastapi import FastAPI

from app.api.routers.health import router as health_router

# Create FastAPI app instance
def create_app() -> FastAPI:
    app = FastAPI(title="WandAI Orchestrator")
    app.include_router(health_router)
    return app


# Initialize the FastAPI app
app = create_app()

# root endpoint
@app.get("/", summary="Root endpoint")
async def root() -> dict[str, str]:
    return {"message": "Welcome to the WandAI Orchestrator API"}