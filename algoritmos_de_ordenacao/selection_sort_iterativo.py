"""
Algoritmo de ordenação Selection Sort iterativo versão 1
"""

def selection_sort_iterativo(lista):
    n = len(lista)
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i):
            if lista[j] > lista[max_index]:
                max_index = j
        if max_index != i:
            lista[i], lista[max_index] = lista[max_index], lista[i]
    return lista
lista = [100,5,1,80,1,38,2,5,19,100,10,6]
print(selection_sort_iterativo(lista))