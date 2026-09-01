"""
Programa que solicita um valor ao usuário e realiza uma busca sequencial
em uma lista utilizando um laço for. Caso o valor seja encontrado, exibe
a posição em que ele está e encerra a busca. Se o valor não for encontrado
após percorrer toda a lista, informa que ele não foi localizado.
"""
lista = [1,2,3,4,5]
pesquisa = int(input("Digite o primeiro item a pesquisar: "))
cont = 0
for valor in lista:
    if valor == pesquisa:
        print("Valor %d foi encontrado, na posição %d" %(pesquisa, cont))
        break
    cont = cont + 1
else:
    print("Valor %d não achado" %pesquisa)