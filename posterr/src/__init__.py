from fastapi import FastAPI

from . import routes
from .database.loader import Bootloader

app = FastAPI(title="Posterr", description="Strider Web Back-end Assessment - 3.0")
app.include_router(routes.router)

bootloader = Bootloader()
