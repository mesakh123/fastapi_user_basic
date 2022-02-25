from fastapi import APIRouter
from fastapi_users import FastAPIUsers
from config.database import get_user_manager
from schemas.user import User, UserCreate, UserUpdate, UserDB
from auth import auth_backend

router = APIRouter()


fastapi_users = FastAPIUsers(
    get_user_manager,
    [auth_backend],
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

current_active_user = fastapi_users.current_user(active=True)


router.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
router.include_router(fastapi_users.get_users_router(),
                      prefix="/users", tags=["users"])
router.include_router(fastapi_users.get_register_router(),
                      prefix="/auth", tags=["auth"])
router.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
router.include_router(
    fastapi_users.get_verify_router(),
    prefix="/auth",
    tags=["auth"],
)
