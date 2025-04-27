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
    acao_ventoinha: str = None  # Novo campo para controlar a ventoinha

# Lista para armazenar os dados recebidos
dados_sensores: List[SensorData] = []

# Variável para armazenar o estado da ventoinha
ventoinha_estado = False

# Função para definir o estado da ventoinha
def set_ventoinha_estado(estado: bool):
    global ventoinha_estado
    ventoinha_estado = estado
    print(f"Ventoinha {'ligada' if ventoinha_estado else 'desligada'}")

@app.post("/sensores")
async def receber_dados(data: SensorData):
    """Recebe dados do Arduino e pode controlar a ventoinha"""
    try:
        dados_sensores.append(data)

        print(f"Temperatura: {data.temperatura} °C")
        print(f"Umidade: {data.umidade} %")
        print(f"Distância: {data.distancia} cm")
        print(f"Timestamp: {datetime.now().isoformat()}")

        # Se o campo acao_ventoinha for 'ligar', liga a ventoinha
        if data.acao_ventoinha == "ligar":
            set_ventoinha_estado(True)

        # Se o campo acao_ventoinha for 'desligar', desliga a ventoinha
        if data.acao_ventoinha == "desligar":
            set_ventoinha_estado(False)

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

@app.get("/ventoinha/estado")
async def estado_ventoinha():
    """Consulta o estado da ventoinha"""
    return {"ventoinha": ventoinha_estado}
