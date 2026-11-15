from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user_id, get_auth_rate_limiter
from app.modules.users.dependencies import get_users_service
from app.modules.users.schemas import DeleteAccountRequest, RegisterDeviceRequest
from app.modules.users.service import UsersService
from app.shared.utils.response import success_response

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/devices", summary="Register a device for push notifications")
async def register_device(
    payload: RegisterDeviceRequest,
    user_id: str = Depends(get_current_user_id),
    service: UsersService = Depends(get_users_service),
):
    # TODO: result = await service.register_device(user_id, payload.device_id, payload.device_name, payload.platform, payload.push_token)
    # TODO: return success_response(data=DeviceResponse(...).model_dump(), status_code=201)
    return success_response(
        data={"message": "register-device — not yet implemented"}, status_code=501
    )


@router.delete("/devices/{device_id}", summary="Deactivate a device")
async def remove_device(
    device_id: str,
    user_id: str = Depends(get_current_user_id),
    service: UsersService = Depends(get_users_service),
):
    # TODO: await service.remove_device(user_id, device_id)
    # TODO: return success_response(data={"message": messages.USER_DEVICE_REMOVED})
    return success_response(
        data={"message": "remove-device — not yet implemented"}, status_code=501
    )


@router.post(
    "/me/delete",
    summary="Request account deletion",
    dependencies=[
        Depends(get_current_user_id),
        Depends(get_auth_rate_limiter)
    ],
)
async def request_deletion(
    payload: DeleteAccountRequest,
    service: UsersService = Depends(get_users_service),
    user_id: str = Depends(get_current_user_id),  # Still keep it here for access in function
):
    # TODO: result = await service.request_account_deletion(user_id, payload.reason)
    # TODO: return success_response(data={"message": messages.USER_DELETION_SCHEDULED})
    return success_response(
        data={"message": "request-deletion — not yet implemented"}, status_code=501
    )


@router.post(
    "/me/cancel-deletion",
    summary="Cancel a pending account deletion",
    dependencies=[
        Depends(get_current_user_id),
        Depends(get_auth_rate_limiter)
    ],
)
async def cancel_deletion(
    service: UsersService = Depends(get_users_service),
    user_id: str = Depends(get_current_user_id),
):
    # TODO: await service.cancel_account_deletion(user_id)
    # TODO: return success_response(data={"message": messages.USER_DELETION_CANCELLED})
    return success_response(
        data={"message": "cancel-deletion — not yet implemented"}, status_code=501
    )
