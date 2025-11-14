from dataclasses import dataclass

@dataclass
class Veiculo:
    codigo: int
    modelo: str
    ano: int
    cor: str
    preco: float