def insertion_sort_iterativo(lista):
    n = len(lista)
    for i in range(1, n):
        valor_atual = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > valor_atual:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = valor_atual
    return lista
lista = [39,2,6,5,4,90,45,100,7,24,55]
print(insertion_sort_iterativo(lista))