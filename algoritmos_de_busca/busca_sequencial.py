def busca_sequencial(lista,valor_busca):
    for index, valor in enumerate(lista):
        if valor_busca == valor:
            return f"Valor {valor_busca} encontrado. No indice {index}. Foram realizadas {index + 1} comparações."
    return f"Valor {valor_busca} não foi encontrado. Foram realizadas {index + 1} comparações."
lista = [100,5,1,80,1,38,2,5,19,100,10,6]
valor_busca = int(input("Digite o valor que deseja buscar: "))
print(busca_sequencial(lista,valor_busca))