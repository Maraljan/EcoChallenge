from fastapi import APIRouter
from .routers import daily_task_router


router = APIRouter(prefix='/daily_task')

router.include_router(daily_task_router.router)
