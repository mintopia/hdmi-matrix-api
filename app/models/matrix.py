from typing import List

from pydantic import BaseModel


class CascadeResponse(BaseModel):
    enabled: bool
    rawdata: str


class CascadeRequest(BaseModel):
    enabled: bool


class Input(BaseModel):
    number: int
    edid: int


class Output(BaseModel):
    number: int
    input: int


class StatusResponse(BaseModel):
    inputs: List[Input]
    outputs: List[Output]
    cascade: bool
    rawdata: str


class CommandRequest(BaseModel):
    command: str


class CommandResponse(BaseModel):
    command: str
    response: str


class OutputRequest(BaseModel):
    input: int


class OutputResponse(BaseModel):
    number: int
    input: int
    rawdata: str
