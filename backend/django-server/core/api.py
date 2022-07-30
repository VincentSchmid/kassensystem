from turtle import pos
from ninja import NinjaAPI

from domain.pos.api import router as pos_router

api = NinjaAPI()
api.add_router("/pos/", pos_router, tags=["tables"])
