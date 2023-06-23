from typing import Annotated
from fastapi import Depends

from eco_challenge.daily_task_app.models.user_response_model import UserResponse, UserResponseCreate
from .storage import Storage


class UserResponseStorage(Storage[UserResponse, UserResponseCreate]):
    model = UserResponse

    def get_pk(self):
        return self.model.user_response_id


UserResponseStorageDepends = Annotated[UserResponseStorage, Depends(UserResponseStorage)]
