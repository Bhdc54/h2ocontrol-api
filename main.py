from fastapi import FastAPI
from routers import arduino

app = FastAPI()


app.include_router(arduino.router)
