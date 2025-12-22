listaUm = []
listaDois = []
listaTres = []
while True:
    nLista = int(input("Digite um número para colocar na lista 1(0 encerra): "))
    if nLista == 0:
        break
    listaUm.extend([nLista])
while True:
    nLista = int(input("Digite um número para colocar na lista 2(0 encerra): "))
    if nLista == 0:
        break
    listaDois.extend([nLista])
listaTres.extend(listaUm)
listaTres.extend(listaDois)
print(listaTres)