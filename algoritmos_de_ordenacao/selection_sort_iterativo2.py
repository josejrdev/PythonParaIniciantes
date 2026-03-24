lista = [6,7,8,3,2]
def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lista[j] < lista[min_index]:
                min_index = j
        lista[i], lista[min_index] = lista[min_index], lista[i]
selection_sort(lista)
print(lista)