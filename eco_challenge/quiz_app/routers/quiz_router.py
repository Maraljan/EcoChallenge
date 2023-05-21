from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.quiz_app.models.quiz_model import QuizGet, QuizCreate, Quiz

router = APIRouter(prefix='/quiz', tags=['Quiz'])


@router.post('/')
async def create_quiz(quiz_create: QuizCreate, session: DbSession) -> QuizGet:
    quiz = Quiz(**quiz_create.dict())
    session.add(quiz)
    await session.commit()
    await session.refresh(quiz, [Quiz.category])
    return quiz


@router.get('/')
async def get_quizzes(session: DbSession) -> list[QuizGet]:
    statement = sqlmodel.select(Quiz).options(selectinload('*'))
    results = await session.execute(statement)
    quizzes = results.scalars().all()
    return quizzes


@router.delete('/{quiz_id}')
async def delete_quiz(quiz_id: int, session: DbSession):
    statement = sqlmodel.delete(Quiz).where(Quiz.quiz_id == quiz_id)
    await session.execute(statement)
    await session.commit()
