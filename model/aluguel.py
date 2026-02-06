from dataclasses import dataclass
from model.cliente import Cliente
from model.veiculo import Veiculo

@dataclass
class Aluguel:
    codigo: int
    cliente: Cliente 
    veiculo: Veiculo 
    quantidade_dias: int
    valor_total: float
