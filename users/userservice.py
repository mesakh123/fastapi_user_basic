import fastapi_users
from fastapi import Request

from .userrouter import router


from models.usermodel import UserDB
from config.database import SECRET
from auth.auth import jwt_authentication

from .userhandler import on_after_forgot_password, on_after_register, after_verification_request


router.include_router(fastapi_users.get_users_router(),
                      prefix="/users", tags=["users"])

router.include_router(
    fastapi_users.get_auth_router(jwt_authentication), prefix="/auth/jwt", tags=["auth"]
)

router.include_router(
    fastapi_users.get_register_router(on_after_register), prefix="/auth", tags=["auth"]
)

router.include_router(
    fastapi_users.get_reset_password_router(
        SECRET, after_forgot_password=on_after_forgot_password
    ),
    prefix="/auth",
    tags=["auth"],
)

router.include_router(
    fastapi_users.get_verify_router(
        SECRET, after_verification_request=after_verification_request
    ),
    prefix="/auth",
    tags=["auth"],
)
