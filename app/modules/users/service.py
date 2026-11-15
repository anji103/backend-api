"""
Users Service
=============
Business logic for user lifecycle management.
This layer must NOT access the database directly — use the repository.
"""

from app.modules.users.repository import UsersRepository


class UsersService:
    """
    Business logic for user lifecycle management.

    Responsibilities:
    ─────────────────
    - Device registration and deactivation
    - Account deletion workflow (request → cancel)
    """

    def __init__(self, repository: UsersRepository) -> None:
        self.repository = repository

    # TODO: implement
    # async def register_device(self, user_id: UUID, device_id: str, device_name: str | None, platform: str | None, push_token: str | None) -> UserDevice
    #     1. Check if device_id already exists → update push_token if so
    #     2. Otherwise create new UserDevice record
    #     3. Return device

    # async def remove_device(self, user_id: UUID, device_id: str) -> None
    #     1. Fetch device by device_id
    #     2. Verify it belongs to user_id → raise ForbiddenException if not
    #     3. Deactivate (set is_active = False)

    # async def request_account_deletion(self, user_id: UUID, reason: str | None) -> AccountDeletion
    #     1. Check no pending deletion exists → raise ConflictException
    #     2. Revoke all refresh tokens for user
    #     3. Schedule purge date (e.g. 30 days from now)
    #     4. Create AccountDeletion record
    #     5. Return record

    # async def cancel_account_deletion(self, user_id: UUID) -> None
    #     1. Fetch pending deletion for user → raise NotFoundException if none
    #     2. Mark is_cancelled = True, set cancelled_at = now
