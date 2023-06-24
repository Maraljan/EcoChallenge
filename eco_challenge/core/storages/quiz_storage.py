from typing import Annotated
from fastapi import Depends

from eco_challenge.quiz_app.models.quiz_model import Quiz, QuizCreate
from .storage import Storage


class QuizStorage(Storage[Quiz, QuizCreate]):
    model = Quiz

    def get_pk(self):
        return self.model.quiz_id


QuizStorageDepends = Annotated[QuizStorage, Depends(QuizStorage)]
