from fastapi import FastAPI


import contextlib

from eco_challenge.core import routers
from .core.database import DATA_BASE
from . import quiz_app, daily_task_app


@contextlib.asynccontextmanager
async def lifespan(_: FastAPI):
    await DATA_BASE.connect()
    yield None


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(routers.user_router.router)
    app.include_router(routers.role_router.router)
    app.include_router(routers.points_count_router.router)
    app.include_router(routers.points_transaction_router.router)
    app.include_router(routers.auth_router.router)
    app.include_router(quiz_app.router)
    app.include_router(daily_task_app.router)
    return app
