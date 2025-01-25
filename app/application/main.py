from fastapi import FastAPI

from app.application.registration.handlers import router as registration_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Events-Face",
        debug=True,
        docs_url="/api/docs",
        description="Facade for unloading the Events-Provider service",
    )
    app.include_router(registration_router)
    return app
