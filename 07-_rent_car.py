import os

####### FUNÇÕES GLOBAIS
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def precione_continuar():
    input("Precione Enter para continuar...")


####### TITULO DO SISTEMA
def titulo():
    print("#"*50)
    print("#"+ " "*15 +"LOCADORA DE CARROS" + " "*15+"#")
    print("#"*50)

####### MENU PRINCIPAL
def menu():
    print("\n#Menu de Opções")
    print("1 - Cadastro de Clientes")
    print("2 - Cadastro de Veículos")
    print("3 - Alugar Carro")
    print("4 - Sair do Sistema")

####### FUNÇÕES DO SISTEMA
def cadastro_clientes():
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de nascimento: "))
    email = input("E-mail: ")

while True:
    limpar_tela()
    titulo()
    menu()

    opcao=int(input("\nInforme uma opção: "))

    match opcao:
        case 1:
            limpar_tela()
            print("\n#### CADASTRO DE CLIENTES ####")
            cadastro_clientes()
            precione_continuar()

        case 2:
            print("\n#CADASTRO DE VEÍCULOS")
            precione_continuar()

        case 3:
            print("\n#ALUGAR CARRO")
            precione_continuar()

        case 4:
            print("\n#SAIR")
            
        case 5:
            print("\n#OPÇÃO INVÁLIDA")
            precione_continuar()





