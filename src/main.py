from fastapi import FastAPI
from dotenv import load_dotenv
from routes import base
app = FastAPI()

load_dotenv(".env")
app.include_router(base.base_router)