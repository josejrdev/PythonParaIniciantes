# Complexidade O(n)
# Melhor caso se o valor estiver na primeira posição.
# Pior caso se estiver na última ou se não for encontrado.
lista = [54,26,93,17,77,31,44,55,20]
valor_busca = int(input("Digite um valor para buscar: "))
def busca_sequencial(v,l):
    comparacoes = 0
    for i,e in enumerate(l):
        comparacoes += 1
        if v == e:
            return f"Encontrado. Indice: {i} - Comparaões: {comparacoes}"
    return f"Não encontrado. Comparações: {comparacoes}"
print(busca_sequencial(valor_busca, lista))