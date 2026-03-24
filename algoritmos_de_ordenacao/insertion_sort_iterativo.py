def insertion_sort(lista):
    """
    Ordena a lista utilizando o algoritmo Insertion Sort (versão iterativa).
    Algoritmo estável, in-place, com complexidade O(n²) no pior caso.
    """
    # Percorre a lista a partir do segundo elemento
    for i in range(1, len(lista)):
        valor_atual = lista[i]  # Elemento a ser inserido na posição correta
        j = i - 1  # Índice do elemento anterior

        # Desloca elementos maiores para a direita
        while j >= 0 and lista[j] > valor_atual:
            lista[j + 1] = lista[j]
            j -= 1

        # Insere o valor atual na posição correta
        lista[j + 1] = valor_atual
lista = [54,26,93,17,77,31,44,55,20]
insertion_sort(lista)
print(lista)