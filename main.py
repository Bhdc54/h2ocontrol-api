from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI()

# Modelo de dados que o Arduino vai enviar
class SensorData(BaseModel):
    temperatura: float
    umidade: float
    distancia: float

@app.post("/sensores")
async def receber_dados(data: SensorData):
    """Recebe dados do Arduino e responde"""
    try:
        # Mostra os dados recebidos no terminal
        print(f"Temperatura: {data.temperatura} °C")
        print(f"Umidade: {data.umidade} %")
        print(f"Distância: {data.distancia} cm")
        print(f"Timestamp: {datetime.now().isoformat()}")

        # Decide se vai ligar ou desligar a ventoinha
        ventoinha = False
        if data.temperatura > 30:  # Exemplo: liga ventoinha se temperatura > 30°C
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
