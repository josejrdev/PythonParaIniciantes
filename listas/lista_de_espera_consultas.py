"""
Programa que solicita um nome ao usuário e verifica se ele está entre
os três primeiros nomes de uma lista de espera para consulta. A busca
é realizada percorrendo as quatro primeiras posições da lista e, caso
o nome seja encontrado, uma mensagem é exibida e a busca é encerrada.
"""
listaEsperaConsulta = ["Carlos", "Ana", "Bruno", "Elisa", "Patricia", "João"]
nomeBusca = input("Digite o nome a buscar: ")
for i in range(3):
    if nomeBusca == listaEsperaConsulta[i]:
        print(f"O nome {nomeBusca} está entre os 3 primeiros da lista")
        break