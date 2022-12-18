from fastapi import FastAPI, File, HTTPException, Query, UploadFile

from src import __version__
from src.core.models.backend_model import BackendData

from src.test.models.test_model import TestData

app = FastAPI(
    title="Lys Backend",
    version=__version__,
    contact={
        "name": "Sebastian Wilhelmsen",
        "email": "wil.sebastian@protonmail.com" # TODO: Evaluate
    }
)

@app.get("/", tags=["Backend"], response_model=BackendData)
def initial_connection():
    """Returns all available parameters that can be used with the backend.
    
    Returns:
        BackendInfo: Backend parameters
    """
    read_me: str = open("CHANGELOG.md", "r", encoding="utf-8").read()

    return BackendData(
        version=__version__,
        readMe=read_me
    )

@app.get("/test", tags=["test"], response_model=TestData)
def initial_connection():
    return TestData(
        text="test data her"
    )


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=2500)