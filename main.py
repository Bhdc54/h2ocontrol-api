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

# Lista para armazenar os dados recebidos
dados_sensores: List[SensorData] = []

# Variável para armazenar o estado da ventoinha
ventoinha_estado = False

@app.post("/sensores")
async def receber_dados(data: SensorData):
    """Recebe dados do Arduino"""
    try:
        dados_sensores.append(data)

        print(f"Temperatura: {data.temperatura} °C")
        print(f"Umidade: {data.umidade} %")
        print(f"Distância: {data.distancia} cm")
        print(f"Timestamp: {datetime.now().isoformat()}")

        # Retorna a resposta com o estado atual da ventoinha
        return {
            "status": "sucesso",
            "timestamp": datetime.now().isoformat(),
            "ventoinha_estado_atual": ventoinha_estado
        }

    except Exception as e:
        return {
            "status": "erro",
            "detalhe": str(e)
        }

@app.get("/sensores")
async def listar_dados():
    """Retorna todos os dados recebidos do Arduino"""
    return {
        "dados": dados_sensores,
        "total": len(dados_sensores)
    }

# NOVAS ROTAS para controlar a ventoinha manualmente

@app.post("/ventoinha/ligar")
async def ligar_ventoinha():
    """Liga a ventoinha manualmente"""
    global ventoinha_estado
    ventoinha_estado = True
    print("Ventoinha ligada manualmente!")
    return {"ventoinha": "ligada"}

@app.post("/ventoinha/desligar")
async def desligar_ventoinha():
    """Desliga a ventoinha manualmente"""
    global ventoinha_estado
    ventoinha_estado = False
    print("Ventoinha desligada manualmente!")
    return {"ventoinha": "desligada"}

@app.get("/ventoinha/estado")
async def estado_ventoinha():
    """Retorna o estado atual da ventoinha"""
    return {"ventoinha": ventoinha_estado}
