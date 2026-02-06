from model.veiculo import Veiculo

veiculos = []

#função de cadastro de veículos
def cadastro_veiculos():
    
    codigo_veiculo = int(input("Código do veículo: "))
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    preco = float(input("Preço por dia: "))

    veiculo = Veiculo(codigo_veiculo,modelo,ano,cor,preco)
    veiculos.append(veiculo)
    print("\nVeículo cadastrado com sucesso!")

# função para listar veículos
def lista_veiculos():

    print("\n#LISTA DE VEÍCULOS")
    print("-"*94)
    print(f"| {'Código':^8} | {'Modelo':^20} | {'Ano':^15} | {'Cor':^25} | {'Preço':^10} |")
    print("-"*94)
    for veiculo in veiculos:
        print(f"| {veiculo.codigo:^8} | {veiculo.modelo:<20} | {veiculo.ano:^15} | {veiculo.cor:<25} | {veiculo.preco:^10} |")
    print("-"*94)

def pegar_veiculos():
    return veiculos