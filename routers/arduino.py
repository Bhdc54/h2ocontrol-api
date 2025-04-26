from fastapi import APIRouter
from models.dados import ArduinoData

router = APIRouter()

# post para receber os dados do Arduino
@router.post("/dados-arduino/")
async def receber_dados_arduino(data: ArduinoData):
    
    print(f"Temperatura: {data.temperatura}, Umidade: {data.umidade}, Luminosidade: {data.luminosidade}")
    return {"status": "sucesso", "dados": data}
