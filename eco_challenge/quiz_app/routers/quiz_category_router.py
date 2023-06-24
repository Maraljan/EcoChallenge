from fastapi import APIRouter

from eco_challenge.auth.dependencies import CurrentAdmin, CurrentUser
from eco_challenge.core.storages.quiz_category_storage import QuizCategoryStorageDepends

from eco_challenge.quiz_app.models.quiz_category_model import QuizCategoryCreate, QuizCategoryGet

router = APIRouter(prefix='/quiz_category', tags=['QuizCategory'])


@router.post('/')
async def create_category(category_create: QuizCategoryCreate, storage: QuizCategoryStorageDepends, _: CurrentAdmin) -> QuizCategoryGet:
    return await storage.save_object(category_create)


@router.get('/')
async def get_categories(storage: QuizCategoryStorageDepends, _: CurrentUser) -> list[QuizCategoryGet]:
    return await storage.get_objects()


@router.get('/{category_id}')
async def get_category(category_id: int, storage: QuizCategoryStorageDepends, _: CurrentUser) -> QuizCategoryGet:
    return await storage.get_obj(category_id)


@router.delete('/{category_id}')
async def delete_category(category_id: int, storage: QuizCategoryStorageDepends, _: CurrentAdmin) -> QuizCategoryGet:
    return await storage.delete_object(category_id)

