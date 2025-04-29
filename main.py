from fastapi import FastAPI
from .routers import sensores, ventoinha

app = FastAPI()

# Inclui os routers
app.include_router(sensores.router)
app.include_router(ventoinha.router)
