"""
Users Repository
================
All database access for the users module lives here.
"""

from sqlalchemy.ext.asyncio import AsyncSession


class UsersRepository:
    """
    Handles all database operations for the users module.

    Responsibilities:
    ─────────────────
    - Device registration and management
    - Account deletion lifecycle persistence
    """

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    # TODO: implement
    # async def get_device_by_device_id(self, device_id: str) -> UserDevice | None
    # async def register_device(self, user_id: UUID, device_id: str, device_name: str | None, platform: str | None, push_token: str | None) -> UserDevice
    # async def deactivate_device(self, device_id: str) -> None
    # async def get_user_devices(self, user_id: UUID) -> list[UserDevice]

    # async def get_pending_deletion(self, user_id: UUID) -> AccountDeletion | None
    # async def create_deletion_request(self, user_id: UUID, reason: str | None, scheduled_purge_at: datetime) -> AccountDeletion
    # async def cancel_deletion_request(self, deletion_id: UUID) -> None
