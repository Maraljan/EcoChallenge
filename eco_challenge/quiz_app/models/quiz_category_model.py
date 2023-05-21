import typing

from sqlmodel import SQLModel, Field, Relationship


if typing.TYPE_CHECKING:
    from .quiz_model import Quiz


class QuizCategoryCreate(SQLModel):
    category_name: str = Field(index=True)


class QuizCategoryGet(QuizCategoryCreate):
    category_id: int


class QuizCategory(QuizCategoryGet, table=True):
    __tablename__ = 'quiz_category'
    category_id: int | None = Field(default=None, primary_key=True)
    quizzes: list['Quiz'] = Relationship(back_populates='category')
