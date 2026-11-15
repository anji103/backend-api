from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.modules.users.repository import UsersRepository
from app.modules.users.service import UsersService


def get_users_repository(db: AsyncSession = Depends(get_db)) -> UsersRepository:
    return UsersRepository(db=db)


def get_users_service(
    repository: UsersRepository = Depends(get_users_repository),
) -> UsersService:
    return UsersService(repository=repository)
