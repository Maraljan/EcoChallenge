from fastapi import APIRouter


from eco_challenge.core.storages.question_storage import QuestionStorageDepends
from eco_challenge.quiz_app.models.question_model import QuestionCreate, QuestionGet

router = APIRouter(prefix='/question', tags=['Question'])


@router.post('/')
async def create_question(question_create: QuestionCreate, storage: QuestionStorageDepends) -> QuestionGet:
    return await storage.save_object(question_create)


@router.get('/')
async def get_questions(storage: QuestionStorageDepends) -> list[QuestionGet]:
    return await storage.get_objects()


@router.delete('/{question_id}')
async def delete_question(question_id: int, storage: QuestionStorageDepends):
    return await storage.delete_object(question_id)
