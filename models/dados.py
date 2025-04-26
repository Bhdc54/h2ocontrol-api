from pydantic import BaseModel

class ArduinoData(BaseModel):
    temperatura: float
    umidade: float