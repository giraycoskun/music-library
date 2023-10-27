"""_summary_

Returns:
    _type_: _description_
"""
from fastapi import FastAPI, Request
from fastapi.exceptions import ResponseValidationError
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
from loguru import logger

from core.test_oauth import list_playlists

load_dotenv()

app = FastAPI(
    title="Music Library API",
    description="A music library api (FastAPI Framework)",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def root() -> dict:
    """_summary_

    Returns:
        dict: _description_
    """
    return {
        "Hello": "World",
        "API Name": "music-library",
        "API Version": "0.1.0",
        "Description": "A music library",
        "Documentation": "",
        "Environment": "Dev",
        "Developer": "giraycoskun",
        "Contact": "giraycoskun.dev@gmail.com",
    }


@app.get("/ping")
async def ping() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return "pong"


@app.get("/test")
async def test() -> dict:
    """_summary_

    Returns:
        str: _description_
    """
    response = list_playlists()
    return response


@app.exception_handler(ResponseValidationError)
async def handle_response_validation_error(
    request: Request, exception: ResponseValidationError
):
    # Log the error
    logger.error(exception)

    # Return a custom response body
    return JSONResponse(status_code=422, content={"errors": exception.errors()})
