from dataclasses import dataclass

@dataclass
class Cliente:
    codigo: int
    nome: str
    ano_nascimento: int
    email: str
    