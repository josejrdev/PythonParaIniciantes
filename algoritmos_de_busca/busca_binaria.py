"""
Programa que implementa um algoritmo de busca binária para localizar
um determinado valor em uma lista ordenada. A cada iteração, o algoritmo
compara o valor procurado com o elemento central da lista e descarta
a metade que não pode conter o valor. Ao final, retorna o índice do
elemento encontrado ou -1 caso o valor não esteja presente na lista.
"""
def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2  # Ponto central
        if lista[meio] == alvo:
            return meio  # Elemento encontrado!
        elif alvo < lista[meio]:
            fim = meio - 1  # Descarta direita
        else:
            inicio = meio + 1  # Descarta esquerda
    return -1  # Não encontrado

lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56]
alvo = 23
indice = busca_binaria(lista_ordenada, alvo)
print(f"Elemento {alvo} encontrado no índice {indice}" if indice != -1 else "Não encontrado!")