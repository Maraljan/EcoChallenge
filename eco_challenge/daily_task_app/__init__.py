from fastapi import APIRouter
from .routers import daily_task_router, daily_task_history_router, user_response_router


router = APIRouter(prefix='/daily_task')

router.include_router(daily_task_router.router)
router.include_router(daily_task_history_router.router)
router.include_router(user_response_router.router)
