"""
Algoritmo que lê uma quantidade definida de números inteiros, armazena
esses números em uma lista e percorre a lista para identificar e exibir
apenas os números que são pares, informando também a posição de cada um.
"""

cont = 0
lista_numeros = []
qtd_numeros = int(input("Quantidade de números: "))
cont = 0

while qtd_numeros <= 0:
    print("Quantidade de números inválida.")
    qtd_numeros = int(input("Quantidade de números:"))

while cont < qtd_numeros:
    numero = int(input(f"{cont + 1}° número: "))
    lista_numeros.append(numero)
    cont = cont + 1

for i,v in enumerate(lista_numeros):
    if v % 2 == 0:
        print(f"O {i + 1}° número é par = {v}")



        