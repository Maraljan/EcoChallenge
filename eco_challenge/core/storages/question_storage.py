from typing import Annotated
from fastapi import Depends

from eco_challenge.quiz_app.models.question_model import Question, QuestionCreate
from .storage import Storage


class QuestionStorage(Storage[Question, QuestionCreate]):
    model = Question


QuestionStorageDepends = Annotated[QuestionStorage, Depends(QuestionStorage)]
