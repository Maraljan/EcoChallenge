from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from eco_challenge.auth.dependencies import CurrentUser
from eco_challenge.auth.jwt import TokenResponse, JwtToken
from eco_challenge.core.database import DbSession
from eco_challenge.auth.authservice import AUTH_SERVICE
from eco_challenge.core.models.user_model import UserGet

router = APIRouter(prefix='/auth', tags=['Auth'])


@router.post('/login')
async def login(session: DbSession, form: OAuth2PasswordRequestForm = Depends()) -> TokenResponse:
    user = await AUTH_SERVICE.auth_user(session=session, email=form.username, password=form.password)
    return TokenResponse(access_token=JwtToken(email=user.email).encode())


@router.get('/current_user')
async def get_current_user(user: CurrentUser) -> UserGet:
    return user
