from fastapi import APIRouter
from firebase_admin import db  # CORRETO
from pydantic import BaseModel
from datetime import datetime
from typing import List
from .ventoinha import set_ventoinha_estado, get_ventoinha_estado


router = APIRouter()

class SensorData(BaseModel):
    temperatura: float
    umidade: float
    distancia: float
    acao_ventoinha: str = None

dados_sensores: List[SensorData] = []

@router.post("/sensores/{sensor_id}")
async def receber_dados(sensor_id: str, data: SensorData):
    dados_sensores.append(data)

    time_stamp = datetime.now().isoformat()
    print(f"Temperatura: {data.temperatura} °C")
    print(f"Umidade: {data.umidade} %")
    print(f"Distância: {data.distancia} cm")
    print(f"Timestamp: {time_stamp}")

    # Atualiza estado da ventoinha se necessário
    if data.acao_ventoinha == "ligar":
        set_ventoinha_estado("ligado")
    elif data.acao_ventoinha == "desligar":
        set_ventoinha_estado("desligado")

    # Envia ao Firestore em subcoleção 'leituras'
    db.collection("sensores").document(sensor_id).collection("leituras").add({
        "temperatura": data.temperatura,
        "umidade": data.umidade,
        "distancia": data.distancia,
        "acao_ventoinha": data.acao_ventoinha,
        "ventoinha_estado": get_ventoinha_estado(),
        "timestamp": time_stamp
    })

    return {
        "status": "sucesso",
        "timestamp": time_stamp,
        "ventoinha_estado_atual": get_ventoinha_estado()
    }

@router.get("/sensores")
async def listar_dados():
    return {
        "dados": dados_sensores,
        "total": len(dados_sensores)
    }
