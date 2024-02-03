from pydantic import BaseModel


class PingResponse(BaseModel):
    ip: str
    timestamp: str
    version: str
