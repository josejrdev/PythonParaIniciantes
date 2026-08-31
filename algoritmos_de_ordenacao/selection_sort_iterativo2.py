"""
Algoritmo de ordenação Selection Sort versão 2
"""

def selection_sort_iterativo(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        if min_index != i:
            lista[i], lista[min_index] = lista[min_index], lista[i]
    return lista
lista = [100,5,1,80,1,38,2,5,19,100,10,6]
print(selection_sort_iterativo(lista))