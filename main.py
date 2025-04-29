from fastapi import FastAPI
from api.routers import sensores
from api.routers import ventoinha


app = FastAPI()

# Inclui os routers
app.include_router(sensores.router)
app.include_router(ventoinha.router)
