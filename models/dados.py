from pydantic import BaseModel

# dados para o Arduino
class ArduinoData(BaseModel):
    temperatura: float
    umidade: float
    
