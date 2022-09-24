from fastapi import FastAPI

from .database.loader import Bootloader

app = FastAPI(title="Posterr", description="Strider Web Back-end Assessment - 3.0")

bootloader = Bootloader()
