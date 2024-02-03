from datetime import datetime

from fastapi import APIRouter, Request

from ..models.ping_response import PingResponse

router = APIRouter()


@router.get("/v1/ping")
async def ping(request: Request) -> PingResponse:
    return PingResponse(
        ip=request.client.host,
        version="1.0.0",
        timestamp=datetime.now().isoformat()
    )
