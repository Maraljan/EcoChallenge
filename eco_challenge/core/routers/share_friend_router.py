from fastapi import APIRouter

from eco_challenge.core.models.share_friends_model import ShareFriendGet, ShareFriendCreate
from eco_challenge.core.storages.share_friend_storage import ShareFriendStorageDepends

router = APIRouter(prefix='/share_friend', tags=['ShareFriends'])


@router.post('/')
async def create_shared_friend(
        share_friend_create: ShareFriendCreate,
        storage: ShareFriendStorageDepends) -> ShareFriendGet:
    return await storage.save_object(share_friend_create)


@router.get('/')
async def get_share_friends(storage: ShareFriendStorageDepends) -> list[ShareFriendGet]:
    return await storage.get_objects()


@router.delete('/{share_friend_id}')
async def delete_share_friend(share_friend_id: int, storage: ShareFriendStorageDepends):
    await storage.delete_object(share_friend_id)
