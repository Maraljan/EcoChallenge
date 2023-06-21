import sqlmodel
from fastapi import APIRouter, HTTPException
from sqlmodel import select

from eco_challenge.core.database import DbSession
from eco_challenge.core.storages.quiz_category_storage import QuizCategoryStorageDepends

from eco_challenge.quiz_app.models.quiz_category_model import QuizCategory, QuizCategoryCreate, QuizCategoryGet

router = APIRouter(prefix='/quiz_category', tags=['QuizCategory'])


@router.post('/')
async def create_category(category_create: QuizCategoryCreate, storage: QuizCategoryStorageDepends) -> QuizCategoryGet:
    return await storage.save_object(category_create)


@router.get('/')
async def get_categories(storage: QuizCategoryStorageDepends) -> list[QuizCategoryGet]:
    return await storage.get_objects()


@router.get('/{category_id}')
async def get_category(category_id: int, storage: QuizCategoryStorageDepends) -> QuizCategoryGet:
    return await storage.get_obj(category_id)


@router.delete('/{category_id}')
async def delete_category(category_id: int, storage: QuizCategoryStorageDepends) -> QuizCategoryGet:
    return await storage.delete_object(category_id)

