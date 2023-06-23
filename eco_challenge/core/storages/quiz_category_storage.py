from typing import Annotated
from fastapi import Depends

from eco_challenge.quiz_app.models.quiz_category_model import QuizCategory, QuizCategoryCreate
from .storage import Storage


class QuizCategoryStorage(Storage[QuizCategory, QuizCategoryCreate]):
    model = QuizCategory

    def get_pk(self):
        return self.model.category_id


QuizCategoryStorageDepends = Annotated[QuizCategoryStorage, Depends(QuizCategoryStorage)]
