from typing import List
from .models import SensorData

# Lista para armazenar os dados recebidos
dados_sensores: List[SensorData] = []

# Variável para armazenar o estado da ventoinha
ventoinha_estado = "desligado"  # Começa desligada
