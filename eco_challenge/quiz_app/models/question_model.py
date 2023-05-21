import typing

from sqlmodel import SQLModel, Field, Relationship

from .answer_model import Answer, AnswerGet

if typing.TYPE_CHECKING:
    from .quiz_model import Quiz


class QuestionCreate(SQLModel):
    question: str = Field(index=True)
    quiz_id: int = Field(foreign_key='quiz.quiz_id')


class QuestionGet(QuestionCreate):
    question_id: int
    # quiz: Quiz
    answers: list[AnswerGet] = []


class Question(QuestionCreate, table=True):
    question_id: int | None = Field(default=None, primary_key=True)
    quiz: 'Quiz' = Relationship(back_populates='questions')
    answers: list[Answer] = Relationship(back_populates='question')
