"""
Algoritmo que lê uma quantidade definida de números, valida se a
quantidade informada é positiva, armazena os números em uma lista
e calcula e exibe a média aritmética dos valores informados.
"""

qtd_numeros = int(input("Digite a quantidade de números: "))
while qtd_numeros <= 0:
    print("Quantidade inválida.")
    qtd_numeros = int(input("Digite a quantidade de números: "))
cont = 1
lista_numeros = []
while qtd_numeros > 0:
    numero = float(input(f"Digite o {cont}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1
    qtd_numeros = qtd_numeros - 1
media_numeros = sum(lista_numeros) / len(lista_numeros)
print(media_numeros)