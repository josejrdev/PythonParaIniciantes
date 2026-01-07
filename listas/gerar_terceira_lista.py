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