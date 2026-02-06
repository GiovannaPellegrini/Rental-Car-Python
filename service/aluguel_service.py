import service.cliente_service as cliente_service 
import service.veiculo_service as veiculo_service 

def alugar_veiculo():
    
    lista_veiculos = veiculo_service.pegar_veiculos()

    codigo_cliente = int(input("Digite o código do cliente: ")) 
    cliente = encontrar_cliente(codigo_cliente)
    print(cliente) 

    #codigo_veiculo = int(input("Digite o código do veiculo: "))
    #dias_aluguel = int(input("Digite a quantidade de dias: ")) 

#encontra o cliente pelo código informado
def encontrar_cliente(codigo_parametro):
    lista_clientes = cliente_service.pegar_clientes()

#percorre a lista de clientes proucurando o código informado no parâmetro
    for cliente in lista_clientes:
        if cliente ['codigo'] == codigo_parametro:
            return cliente
    return None 


