from sqlmodel import SQLModel, Field, Relationship

from .quiz_category_model import QuizCategory
from .question_model import Question, QuestionGet


class QuizCreate(SQLModel):
    quiz_name: str = Field(index=True)
    points: int
    category_id: int = Field(foreign_key='quiz_category.category_id')


class QuizGet(QuizCreate):
    quiz_id: int
    category: QuizCategory
    questions: list[QuestionGet] = []


class Quiz(QuizCreate, table=True):
    quiz_id: int | None = Field(default=None, primary_key=True)
    category: QuizCategory = Relationship(back_populates='quizzes')
    questions: list[Question] = Relationship(back_populates='quiz')
