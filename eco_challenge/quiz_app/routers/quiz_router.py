from fastapi import APIRouter

from eco_challenge.core.storages.quiz_storage import QuizStorageDepends
from eco_challenge.quiz_app.models.quiz_model import QuizGet, QuizCreate

router = APIRouter(prefix='/quiz', tags=['Quiz'])


@router.post('/')
async def create_quiz(quiz_create: QuizCreate, storage: QuizStorageDepends) -> QuizGet:
    return await storage.save_object(quiz_create)


@router.get('/')
async def get_quizzes(storage: QuizStorageDepends) -> list[QuizGet]:
    return storage.get_objects()


@router.get('/{quiz_id}')
async def get_quiz(quiz_id: int, storage: QuizStorageDepends):
    return await storage.get_obj(quiz_id)


@router.delete('/{quiz_id}')
async def delete_quiz(quiz_id: int, storage: QuizStorageDepends):
    return await storage.delete_object(quiz_id)
