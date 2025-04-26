from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime
from typing import List

app = FastAPI()

# Modelo de dados que o Arduino vai enviar
class SensorData(BaseModel):
    temperatura: float
    umidade: float
    distancia: float

# Lista para armazenar os dados recebidos (simula um banco de dados simples)
dados_sensores: List[SensorData] = []

@app.post("/sensores")
async def receber_dados(data: SensorData):
    """Recebe dados do Arduino e responde"""
    try:
        # Armazena os dados na lista
        dados_sensores.append(data)

        # Mostra os dados recebidos no terminal
        print(f"Temperatura: {data.temperatura} °C")
        print(f"Umidade: {data.umidade} %")
        print(f"Distância: {data.distancia} cm")
        print(f"Timestamp: {datetime.now().isoformat()}")

        # Decide se vai ligar ou desligar a ventoinha
        ventoinha = False
        if data.temperatura > 30:
            ventoinha = True

        return {
            "status": "sucesso",
            "timestamp": datetime.now().isoformat(),
            "ventoinha": ventoinha
        }

    except Exception as e:
        return {
            "status": "erro",
            "detalhe": str(e)
        }

# Nova rota GET para visualizar os dados
@app.get("/sensores")
async def listar_dados():
    """Retorna todos os dados recebidos do Arduino"""
    return {
        "dados": dados_sensores,
        "total": len(dados_sensores)
    }