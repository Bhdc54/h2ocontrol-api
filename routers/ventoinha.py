from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

ventoinha_estado = "desligado"

class VentoinhaState(BaseModel):
    estado: str

def set_ventoinha_estado(novo_estado: str):
    global ventoinha_estado
    if novo_estado in ["ligado", "desligado"]:
        ventoinha_estado = novo_estado

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

