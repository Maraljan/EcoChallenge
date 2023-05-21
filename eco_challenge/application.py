from fastapi import FastAPI


import contextlib
from .core.database import DATA_BASE
from . import routers, quiz_app


@contextlib.asynccontextmanager
async def lifespan(application: FastAPI):
    await DATA_BASE.connect()
    yield None


def create_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)
    app.include_router(routers.user_router.router)
    # app.include_router(routers.share_friend_router.router)
    app.include_router(quiz_app.router)
    return app
