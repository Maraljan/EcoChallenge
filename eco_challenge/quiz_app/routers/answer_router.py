from fastapi import APIRouter
from sqlalchemy.orm import selectinload
import sqlmodel

from eco_challenge.core.database import DbSession

from eco_challenge.quiz_app.models.answer_model import Answer, AnswerCreate, AnswerGet

router = APIRouter(prefix='/answer', tags=['Answer'])


@router.post('/')
async def create_answer(answer_create: AnswerCreate, session: DbSession) -> AnswerGet:
    answer = Answer(**answer_create.dict())
    session.add(answer)
    await session.commit()
    await session.refresh(answer)
    return answer


@router.get('/')
async def get_answers(session: DbSession) -> list[AnswerGet]:
    statement = sqlmodel.select(Answer).options(selectinload('*'))
    results = await session.execute(statement)
    quizzes = results.scalars().all()
    return quizzes

