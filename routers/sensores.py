from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime
from typing import List

router = APIRouter()

# Modelo de dados que o Arduino vai enviar
class SensorData(BaseModel):
    temperatura: float
    umidade: float
    distancia: float
    acao_ventoinha: str = None

# Lista para armazenar os dados recebidos
dados_sensores: List[SensorData] = []

# Estado da ventoinha (compartilhado)
ventoinha_estado = "desligado"

def set_ventoinha_estado(novo_estado: str):
    global ventoinha_estado
    if novo_estado in ["ligado", "desligado"]:
        ventoinha_estado = novo_estado

@router.post("/sensores")
async def receber_dados(data: SensorData):
    dados_sensores.append(data)
    print(f"Temperatura: {data.temperatura} °C")
    print(f"Umidade: {data.umidade} %")
    print(f"Distância: {data.distancia} cm")
    print(f"Timestamp: {datetime.now().isoformat()}")

    if data.acao_ventoinha == "ligar":
        set_ventoinha_estado("ligado")
    elif data.acao_ventoinha == "desligar":
        set_ventoinha_estado("desligado")

    return {
        "status": "sucesso",
        "timestamp": datetime.now().isoformat(),
        "ventoinha_estado_atual": ventoinha_estado
    }

@router.get("/sensores")
async def listar_dados():
    return {
        "dados": dados_sensores,
        "total": len(dados_sensores)
    }
