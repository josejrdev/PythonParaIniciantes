"""
Programa que solicita valores de duas listas ao usuário e encerra a
entrada quando o valor 0 é informado. Em seguida, combina os valores
das duas listas em uma terceira lista, mantendo a ordem dos elementos
da primeira lista seguida pela ordem dos elementos da segunda lista.
Ao final, exibe a lista resultante.
"""
listaUm = []
listaDois = []
listaTres = []
cont = 1
while True:
    print(f"Digite os valores das duas listas, 0 nas entradas encerra.")
    itemListaUm = int(input("Digite o %d° valor da primeira lista: " %cont))
    if itemListaUm == 0:
        break
    itemListaDois = int(input("Digite o %d° valor da segunda lista: " %cont))
    if itemListaDois == 0:
        break
    listaUm.append(itemListaUm)
    listaDois.append(itemListaDois)
    cont = cont + 1
for valor in listaUm:
    listaTres.append(valor)
for valor in listaDois:
    listaTres.append(valor)
print("Lista final: ", listaTres)