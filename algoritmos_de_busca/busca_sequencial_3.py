"""
Programa que realiza uma busca sequencial por dois valores em uma lista.
O programa percorre a lista e verifica qual dos dois valores informados
é encontrado primeiro. Ao localizar um deles, exibe uma mensagem
informando qual valor foi encontrado primeiro e encerra a busca.
"""
l = [15,7,27,39]
p = int(input("Digite o primeiro valor a pesquisar: "))
v = int(input("Digite o segundo valor a pesquisar: "))
cont = 0
while cont < len(l):
    if l[cont] == p:
        print("O valor %d foi encontrado primeiro" %p)
        break
    if l[cont] == v:
        print("O valor %d foi encontrado primeiro" %v)
        break
    cont = cont + 1