from fastapi import FastAPI

app = FastAPI(
    title="AgenticAI Backend",
    description="Initial FastAPI backend setup for AgenticAI project",
    version="0.1.0",
)


@app.get("/", tags=["Health"])
async def root() -> dict:
    """
    Health check endpoint.

    Returns:
        dict: A simple JSON response indicating the API is running.
    """
    return {"message": "AgenticAI API is running!"}
