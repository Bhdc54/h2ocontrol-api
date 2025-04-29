from fastapi import APIRouter
from datetime import datetime
from ..models import SensorData
from ..storage import dados_sensores
from ..services.ventoinha_service import set_ventoinha_estado, ventoinha_estado

router = APIRouter()

@router.post("/sensores")
async def receber_dados(data: SensorData):
    try:
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
    except Exception as e:
        return {"status": "erro", "detalhe": str(e)}

@router.get("/sensores")
async def listar_dados():
    return {"dados": dados_sensores, "total": len(dados_sensores)}
