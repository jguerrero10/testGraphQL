from pydantic import BaseModel


class DeviceInfo(BaseModel):
    id: int
    name: str
    manufacturer: str
    ipv4: str
