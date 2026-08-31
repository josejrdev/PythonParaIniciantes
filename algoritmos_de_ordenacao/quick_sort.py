"""
Algoritmo de ordenação QuickSort
"""

def particionar(lista, inicio, fim):
    pivo = lista[inicio]
    esquerda = inicio + 1
    direita = fim

    while True:
        # Avança enquanto os valores forem menores ou iguais ao pivô
        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda += 1

        # Retrocede enquanto os valores forem maiores ou iguais ao pivô
        while direita >= esquerda and lista[direita] >= pivo:
            direita -= 1

        # Se os ponteiros se cruzaram, encerra o laço
        if esquerda > direita:
            break

        # Troca os elementos fora de ordem
        lista[esquerda], lista[direita] = lista[direita], lista[esquerda]

    # Coloca o pivô em sua posição correta
    lista[inicio], lista[direita] = lista[direita], lista[inicio]
    return direita  # Retorna o índice final do pivô

def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1 # Define 'fim' como o último índice da lista, se não for fornecido

    if inicio < fim:  # Garante que há pelo menos dois elementos para ordenar
        indice_pivo = particionar(lista, inicio, fim)   # Particiona e obtém o índice final do pivô
        quicksort(lista, inicio, indice_pivo - 1)  # Ordena a sub-lista à esquerda do pivô
        quicksort(lista, indice_pivo + 1, fim)  # Ordena a sub-lista à direita do pivô