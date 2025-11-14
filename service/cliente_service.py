from model.cliente import Cliente

clientes = []

#funções de cadastro de clientes
def cadastro_clientes():

    codigo_cliente = int(input("Código do cliente: "))
    nome = input("Nome: ")
    ano_nascimento = int(input("Ano de nascimento: "))
    email = input("E-mail: ")

    cliente = Cliente(codigo_cliente, nome, ano_nascimento,email)
    clientes.append(cliente)
    
    print("\nCliente cadastrado com sucesso!")


#função para listar clientes
def lista_clientes():
    print("\n#LISTA DE CLIENTES")
    print("-"*80)
    print(f"| {'Código':^8} | {'Nome':^20} | {'Ano de Nasc.':^15} | {'E-mail':^25} |")
    print("-"*80)
    for cliente in clientes:
        print(f"| {cliente.codigo:^8} | {cliente.nome:<20} | {cliente.ano_nascimento:^15} | {cliente.email:<25} |")
    print("-"*80)