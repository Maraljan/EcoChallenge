import sqlmodel
from fastapi import APIRouter, HTTPException
from sqlmodel import select

from eco_challenge.core.database import DbSession

from eco_challenge.quiz_app.models.quiz_category_model import QuizCategory, QuizCategoryCreate, QuizCategoryGet

router = APIRouter(prefix='/quiz_category', tags=['QuizCategory'])


@router.post('/')
async def create_category(category_create: QuizCategoryCreate, session: DbSession) -> QuizCategoryGet:
    category = QuizCategory(**category_create.dict())
    session.add(category)
    await session.commit()
    await session.refresh(category)
    return category


@router.get('/')
async def get_categories(session: DbSession) -> list[QuizCategoryGet]:
    categories = await session.execute(select(QuizCategory))
    return categories.scalars().all()


@router.get('/{category_id}')
async def get_category(category_id: int, session: DbSession) -> QuizCategoryGet:
    category = await session.get(QuizCategory, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete('/{category_id}')
async def delete_category(category_id: int, session: DbSession):
    statement = sqlmodel.delete(QuizCategory).where(QuizCategory.category_id == category_id)
    await session.execute(statement)
    await session.commit()
