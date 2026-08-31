"""
Algoritmo que calcula o resultado da multiplicação entre dois números
inteiros utilizando apenas operações de adição. O programa soma o
primeiro número a si mesmo a quantidade de vezes indicada pelo segundo
número e, ao final, exibe o resultado.
"""

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
cont = 1
soma = 0

while cont <= numero2:
    soma = soma + numero1
    cont = cont + 1
print(soma)