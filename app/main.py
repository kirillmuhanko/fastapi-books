from fastapi import FastAPI

from app.user.controllers import user_auth_controller

app = FastAPI()

app.include_router(user_auth_controller.router)
