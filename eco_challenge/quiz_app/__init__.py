from fastapi import APIRouter
from .routers import quiz_router, answer_router, question_router, quiz_category_router


router = APIRouter(prefix='/quiz_app')

router.include_router(quiz_router.router)
router.include_router(question_router.router)
router.include_router(quiz_category_router.router)
router.include_router(answer_router.router)
