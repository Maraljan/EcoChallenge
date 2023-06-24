from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin, CurrentUser
from eco_challenge.core.storages.answer_storage import AnswerStorageDepends
from eco_challenge.quiz_app.models.answer_model import AnswerCreate, AnswerGet

router = APIRouter(prefix='/answer', tags=['Answer'])


@router.post('/')
async def create_answer(answer_create: AnswerCreate, storage: AnswerStorageDepends, _: CurrentAdmin) -> AnswerGet:
    return await storage.save_object(answer_create)


@router.get('/')
async def get_answers(storage: AnswerStorageDepends, _: CurrentUser) -> list[AnswerGet]:
    return await storage.get_objects()
