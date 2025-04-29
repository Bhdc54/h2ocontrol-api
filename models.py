from pydantic import BaseModel

class SensorData(BaseModel):
    temperatura: float
    umidade: float
    distancia: float
    acao_ventoinha: str = None

class VentoinhaState(BaseModel):
    estado: str  # "ligado" ou "desligado"
