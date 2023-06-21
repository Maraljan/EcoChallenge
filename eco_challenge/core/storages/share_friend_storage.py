from typing import Annotated
from fastapi import Depends

from eco_challenge.core.models.share_friends_model import ShareFriend, ShareFriendCreate
from .storage import Storage


class ShareFriendStorage(Storage[ShareFriend, ShareFriendCreate]):
    model = ShareFriend


ShareFriendStorageDepends = Annotated[ShareFriendStorage, Depends(ShareFriendStorage)]
