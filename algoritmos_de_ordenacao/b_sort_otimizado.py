def bubble_sort_otimizado(lista):
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(n - 1 - i):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
                trocou = True
        if trocou == False:
            return lista
    return lista