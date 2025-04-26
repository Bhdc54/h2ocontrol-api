from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class SensorData(BaseModel):
    temperatura: float
    distancia: float

@app.post("/sensores")
def receber_dados(dados: SensorData):
    print(f"Temperatura recebida: {dados.temperatura}")
    print(f"Distância recebida: {dados.distancia}")
    return {"message": "Dados recebidos com sucesso!"}
