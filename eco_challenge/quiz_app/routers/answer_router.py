from fastapi import APIRouter

from eco_challenge.core.storages.answer_storage import AnswerStorageDepends
from eco_challenge.quiz_app.models.answer_model import AnswerCreate, AnswerGet

router = APIRouter(prefix='/answer', tags=['Answer'])


@router.post('/')
async def create_answer(answer_create: AnswerCreate, storage: AnswerStorageDepends) -> AnswerGet:
    return await storage.save_object(answer_create)


@router.get('/')
async def get_answers(storage: AnswerStorageDepends) -> list[AnswerGet]:
    return await storage.get_objects()
