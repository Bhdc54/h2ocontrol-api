from fastapi import APIRouter
from ..models import VentoinhaState
from ..services.ventoinha_service import set_ventoinha_estado, ventoinha_estado

router = APIRouter()

@router.get("/ventoinha")
async def obter_estado_ventoinha():
    return {"estado": ventoinha_estado}

@router.post("/ventoinha")
async def definir_estado_ventoinha(estado: VentoinhaState):
    if estado.estado in ["ligado", "desligado"]:
        set_ventoinha_estado(estado.estado)
        return {"mensagem": f"Ventoinha agora está {ventoinha_estado}"}
    else:
        return {"erro": "Estado inválido! Use 'ligado' ou 'desligado'."}
