from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from src.di import di_container


@di_container.app.exception_handler(StarletteHTTPException)
async def http_exception_handler(exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)
