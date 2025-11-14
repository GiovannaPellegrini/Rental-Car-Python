#titulo do sistema
import os

#função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def titulo():
    limpar_tela()
    print("#"*50)
    print("#"+ " "*15 +"LOCADORA DE CARROS" + " "*15+"#")
    print("#"*50)


#função para pressionar continuar
def pressione_continuar():
    input("Pressione Enter para continuar...")

    
#menu principal
def menu():
    print("\n#Menu de Opções")
    print("1 - Cadastro de Clientes")
    print("2 - Lista de Clientes")
    print("3 - Cadastro de Veículos")
    print("4 - Lista de Veículos")
    print("5 - Alugar Carro")
    print("6 - Sair do Sistema")
