import typing

from sqlmodel import SQLModel, Field, Relationship


if typing.TYPE_CHECKING:
    from .question_model import Question


class AnswerCreate(SQLModel):
    answer: str = Field(index=True)
    is_correct: bool = False
    question_id: int = Field(foreign_key='question.question_id')


class AnswerGet(AnswerCreate):
    answer_id: int


class Answer(AnswerCreate, table=True):
    answer_id: int | None = Field(default=None, primary_key=True)
    question: 'Question' = Relationship(back_populates='answers')
