from fastapi import FastAPI
from api.routers import sensores, ventoinha
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Obter o caminho absoluto para o arquivo de configuração do Firebase
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
cred_path = os.path.join(BASE_DIR, "firebase_config.json")

# Inicializa o Firebase Admin com o arquivo de configuração
cred = credentials.Certificate(cred_path)
firebase_admin.initialize_app(cred)

db = firestore.client()

app = FastAPI()

# Inclui os routers
app.include_router(sensores.router)
app.include_router(ventoinha.router)
