import os

from cliente import Cliente

from veiculo import Veiculo

####### VARIÁVEIS GLOBAIS
clientes = []
veiculos = []

#função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#função para pressionar continuar
def pressione_continuar():
    input("Pressione Enter para continuar...")

#titulo do sistema
def titulo():
    limpar_tela()
    print("#"*50)
    print("#"+ " "*15 +"LOCADORA DE CARROS" + " "*15+"#")
    print("#"*50)

def lista_clientes():
    print("\n#LISTA DE CLIENTES")
    print("-"*80)
    print(f"| {'Código':^8} | {'Nome':^20} | {'Ano de Nasc.':^15} | {'E-mail':^25} |")
    print("-"*80)
    for cliente in clientes:
        print(f"| {cliente.codigo:^8} | {cliente.nome:<20} | {cliente.ano_nascimento:^15} | {cliente.email:<25} |")
    print("-"*80)

#menu principal
def menu():
    print("\n#Menu de Opções")
    print("1 - Cadastro de Clientes")
    print("2 - Lista de Clientes")
    print("3 - Cadastro de Veículos")
    print("4 - Lista de Veículos")
    print("5 - Alugar Carro")
    print("6 - Sair do Sistema")

#funções de cadastro de clientes
def cadastro_clientes():

    codigo_cliente = int(input("Código do cliente: "))
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de nascimento: "))
    email = input("E-mail: ")

    cliente = Cliente(codigo_cliente, nome, ano_nascimento,email)
    clientes.append(cliente)
    
    print("\nCliente cadastrado com sucesso!")
    

#função de cadastro de veículos
def cadastro_veículos():
    
    codigo_veiculo = int(input("Código do veículo: "))
    modelo = input("Modelo: ")
    ano = int(input("Ano: "))
    cor = input("Cor: ")
    preco = float(input("Preço por dia: "))

    veiculo = Veiculo(codigo_veiculo,modelo,ano,cor,preco)
    veiculos.append(veiculo)
    print("\nVeículo cadastrado com sucesso!")

   # execução do sistema
while True:

    limpar_tela()
    titulo()
    menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            titulo()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()
            pressione_continuar()

        case 2:
            titulo()
            lista_clientes()
            pressione_continuar()

        case 3:
            titulo()
            print("\n#CADASTRO DE VEÍCULOS")
            cadastro_veículos()   
            pressione_continuar()

        case 5:
            print("\n#ALUGAR CARRO")
            pressione_continuar()

        case 6:
            print("\n#SAIR")
            
        case _:
            print("\n#OPÇÃO INVÁLIDA")
            pressione_continuar()





