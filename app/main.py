from fastapi import FastAPI
from app.api import users   # 👈 import your users router file

app = FastAPI()

# register router
app.include_router(users.router, prefix="/auth")