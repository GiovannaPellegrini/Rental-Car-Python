import os

from cliente import Cliente

from veiculo import Veiculo

import layout 

import veiculo_service


####### VARIÁVEIS GLOBAIS
clientes = []

def lista_clientes():
    print("\n#LISTA DE CLIENTES")
    print("-"*80)
    print(f"| {'Código':^8} | {'Nome':^20} | {'Ano de Nasc.':^15} | {'E-mail':^25} |")
    print("-"*80)
    for cliente in clientes:
        print(f"| {cliente.codigo:^8} | {cliente.nome:<20} | {cliente.ano_nascimento:^15} | {cliente.email:<25} |")
    print("-"*80)


#funções de cadastro de clientes
def cadastro_clientes():

    codigo_cliente = int(input("Código do cliente: "))
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de nascimento: "))
    email = input("E-mail: ")

    cliente = Cliente(codigo_cliente, nome, ano_nascimento,email)
    clientes.append(cliente)
    
    print("\nCliente cadastrado com sucesso!")
    


# execução do sistema
while True:

    layout.limpar_tela()
    layout.titulo()
    layout.menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            layout.titulo()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()
            layout.pressione_continuar()

        case 2:
            layout.titulo()
            lista_clientes()
            layout.pressione_continuar()

        case 3:
            layout.titulo()
            print("\n#CADASTRO DE VEÍCULOS")
            veiculo_service.cadastro_veiculos()   
            layout.pressione_continuar()
        
        case 4: 
            layout.titulo()
            veiculo_service.lista_veiculos()
            layout.pressione_continuar()

        case 5:
            print("\n#ALUGAR CARRO")
            layout.pressione_continuar()

        case 6:
            print("\n#SAIR")
            
        case _:
            print("\n#OPÇÃO INVÁLIDA")
            layout.pressione_continuar()





