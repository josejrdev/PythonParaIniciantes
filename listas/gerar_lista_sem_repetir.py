listaUm = []
listaDois = []
listaTres = []
cont = 1
while True:
    print("Digite os itens das duas listas, 0 nas entradas encerra.")
    itemListaUm = int(input("Digite o %d° item da primeira lista: " %cont))
    if itemListaUm == 0:
        break
    itemListaDois = int(input("Digite o %d° item da segunda lista: " %cont))
    if itemListaDois == 0:
        break
    listaUm.append(itemListaUm)
    listaDois.append(itemListaDois)
    cont = cont + 1
for item in listaUm:
    if item not in listaTres:
        listaTres.append(item)
for item in listaDois:
    if item not in listaTres:
        listaTres.append(item)
print("Terceira lista: ", listaTres)