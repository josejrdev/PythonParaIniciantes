lista = [26,54,93,17,77,31,44,55,20]
def selection_sort(lista):
    n = len(lista)
    for i in range(n - 1, 0, -1):
        max_index = i
        for j in range(i):
            if lista[j] > lista[max_index]:
                max_index = j
        lista[i], lista[max_index] = lista[max_index], lista[i]
selection_sort(lista)
print(lista)