from typing import Annotated
from fastapi import Depends

from eco_challenge.quiz_app.models.answer_model import Answer, AnswerCreate
from .storage import Storage


class AnswerStorage(Storage[Answer, AnswerCreate]):

    model = Answer

    def get_pk(self):
        return self.model.answer_id


AnswerStorageDepends = Annotated[AnswerStorage, Depends(AnswerStorage)]
