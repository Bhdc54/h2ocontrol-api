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
    acao_ventoinha: str = None

# Modelo para receber o estado da ventoinha
class VentoinhaState(BaseModel):
    estado: str  # "ligado" ou "desligado"

# Lista para armazenar os dados recebidos
dados_sensores: List[SensorData] = []

# Variável para armazenar o estado da ventoinha
ventoinha_estado = "desligado"  # Começa desligada

# Função para definir o estado da ventoinha
def set_ventoinha_estado(novo_estado: str):
    global ventoinha_estado
    if novo_estado in ["ligado", "desligado"]:
        ventoinha_estado = novo_estado
        print(f"Ventoinha agora está {ventoinha_estado}")
    else:
        print(f"Estado inválido recebido: {novo_estado}")

@app.post("/sensores")
async def receber_dados(data: SensorData):
    """Recebe dados do Arduino e controla a ventoinha"""
    try:
        dados_sensores.append(data)

        print(f"Temperatura: {data.temperatura} °C")
        print(f"Umidade: {data.umidade} %")
        print(f"Distância: {data.distancia} cm")
        print(f"Timestamp: {datetime.now().isoformat()}")

        # Se vier alguma ação da ventoinha
        if data.acao_ventoinha == "ligar":
            set_ventoinha_estado("ligado")
        elif data.acao_ventoinha == "desligar":
            set_ventoinha_estado("desligado")

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
    """Lista todos os dados recebidos"""
    return {
        "dados": dados_sensores,
        "total": len(dados_sensores)
    }

@app.get("/ventoinha")
async def obter_estado_ventoinha():
    """Consulta o estado atual da ventoinha"""
    return {"estado": ventoinha_estado}

@app.post("/ventoinha")
async def definir_estado_ventoinha(estado: VentoinhaState):
    """Define manualmente o estado da ventoinha: 'ligado' ou 'desligado'"""
    if estado.estado in ["ligado", "desligado"]:
        set_ventoinha_estado(estado.estado)
        return {"mensagem": f"Ventoinha agora está {ventoinha_estado}"}
    else:
        return {"erro": "Estado inválido! Use 'ligado' ou 'desligado'."}
