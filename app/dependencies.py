import os

from fastapi import Header, HTTPException


def verify_api_key(authorization: str = Header(None)):
    if authorization is None:
        raise HTTPException(401, "Unauthorised")
    key = authorization.split(" ")[-1]
    if key != os.getenv('API_KEY'):
        raise HTTPException(401, "Unauthorised")

    return True
