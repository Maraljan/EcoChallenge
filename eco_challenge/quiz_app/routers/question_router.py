from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.quiz_app.models.question_model import Question, QuestionCreate, QuestionGet

router = APIRouter(prefix='/question', tags=['Question'])


@router.post('/')
async def create_question(question_create: QuestionCreate, session: DbSession) -> QuestionGet:
    question = Question(**question_create.dict())
    session.add(question)
    await session.commit()
    await session.refresh(question)
    return question


@router.get('/')
async def get_questions(session: DbSession) -> list[QuestionGet]:
    statement = sqlmodel.select(Question).options(selectinload('*'))
    results = await session.execute(statement)
    questions = results.scalars().all()
    return questions


@router.delete('/{question_id}')
async def delete_question(question_id: int, session: DbSession):
    statement = sqlmodel.delete(Question).where(Question.question_id == question_id)
    await session.execute(statement)
    await session.commit()
