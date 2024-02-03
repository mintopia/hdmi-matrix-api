from fastapi import APIRouter, Depends, HTTPException

from ..dependencies import verify_api_key
from ..models.matrix import *
from ..utils.matrix import send_command
from ..utils.regex import re_input, re_edid

router = APIRouter(
    dependencies=[
        Depends(verify_api_key)
    ]
)


@router.get("/v1/status")
async def status() -> StatusResponse:
    response_code, response = send_command(f"EZG STA")
    if response_code == 500:
        raise HTTPException(status_code=500, detail=response)

    cas_response_code, cas_response = send_command(f"EZG CAS")
    if cas_response_code == 500:
        raise HTTPException(status_code=500, detail=response)

    payload = StatusResponse(
        inputs=[],
        outputs=[],
        cascade=cas_response == 'CAS EN',
        rawdata=response,
    )

    for line in response.split("\n"):
        if input_match := re_input.match(line):
            payload.outputs.append(Output(
                number=input_match.group(1),
                input=input_match.group(2),
            ))
        elif edid_match := re_edid.match(line):
            payload.inputs.append(Input(
                number=edid_match.group(1),
                edid=edid_match.group(2),
            ))

    return payload


@router.post("/v1/cascade")
async def cascade(data: CascadeRequest) -> CascadeResponse:
    action = 'DIS'
    if data.enabled:
        action = 'EN'

    response_code, response = send_command(f"EZS CAS {action}")

    if response_code == 500:
        raise HTTPException(status_code=500, detail=response)
    else:
        return CascadeResponse(
            enabled=response == 'CAS EN',
            rawdata=response,
        )


@router.post("/v1/command")
async def command(data: CommandRequest) -> CommandResponse:
    response_code, response = send_command(data.command)

    if response_code == 500:
        raise HTTPException(status_code=500, detail=response)
    else:
        return CommandResponse(
            command=data.command,
            response=response,
        )


@router.post("/v1/output/{output_number}")
async def output(output_number: int, data: OutputRequest):
    response_code, response = send_command(f"EZS OUT{output_number} VS IN {data.input}")

    if response_code == 500:
        raise HTTPException(status_code=500, detail=response)
    else:
        match = re_input.match(response)
        return OutputResponse(
            number=match.group(1),
            input=match.group(2),
            rawdata=response
        )
