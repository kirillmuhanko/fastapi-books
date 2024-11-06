from fastapi import FastAPI
from core.database import engine

# import models
from controllers import auth_controller, user_controller

app = FastAPI()

# models.Base.metadata.create_all(bind=engine)

app.include_router(auth_controller.router)
app.include_router(user_controller.router)
