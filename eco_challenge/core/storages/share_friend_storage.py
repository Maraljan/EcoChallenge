from typing import Annotated
from fastapi import Depends

from eco_challenge.core.models.share_friends_model import ShareFriend, ShareFriendCreate
from .storage import Storage


class ShareFriendStorage(Storage[ShareFriend, ShareFriendCreate]):
    model = ShareFriend

    def get_pk(self):
        return self.model.share_friend_id


ShareFriendStorageDepends = Annotated[ShareFriendStorage, Depends(ShareFriendStorage)]
