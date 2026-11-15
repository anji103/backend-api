from pydantic import BaseModel, Field

# ── Request Schemas ───────────────────────────────────────────────────────────


class RegisterDeviceRequest(BaseModel):
    device_id: str = Field(min_length=1, max_length=255)
    device_name: str | None = Field(default=None, max_length=255)
    platform: str | None = Field(default=None, pattern="^(ios|android|web)$")
    push_token: str | None = None


class DeleteAccountRequest(BaseModel):
    reason: str | None = Field(default=None, max_length=1000)


# ── Response Schemas ──────────────────────────────────────────────────────────


class DeviceResponse(BaseModel):
    device_id: str
    device_name: str | None
    platform: str | None
    is_active: bool
