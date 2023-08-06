import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from routes import debug
from routes import post

from internal_schemes.dao.base import init_models
from settings import app_settings

init_models()
app = FastAPI(title="Gymmate External API")

# Add URL routers to the API
app.include_router(debug.router)
app.include_router(post.router)


@app.get(
    "/",
    summary="Index page",
    response_class=HTMLResponse,
    description="Links to docs/schemas in Fashion External API",
)
async def root() -> str:
    return """<a href="/docs">Gymmate External API documentation</a>"""


def main() -> None:
    uvicorn.run(
        "main:app",
        host=app_settings.hostname,
        port=app_settings.port,
        log_level="debug",
    )


if __name__ == "__main__":
    main()
