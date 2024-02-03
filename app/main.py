import dotenv
from fastapi import FastAPI

from .routers import matrix, ping

dotenv.load_dotenv()

app = FastAPI(
    title="HDMI Matrix API",
    version="1.0.0",
    summary="REST API for HDMI Matrix Control",
    contact={
        "name": "Jessica Smith",
        "url": "https://github/mintopia/hdmi-matrix-api",
        "email": "jess@mintopia.net",
    },
    license_info={
        "name": "MIT",
        "url": "https://raw.githubusercontent.com/mintopia/hdmi-matrix-api/develop/LICENSE"
    }
)

app.include_router(matrix.router)
app.include_router(ping.router)
