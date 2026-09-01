"""
Algoritmo que define uma função para calcular o fatorial de um número
inteiro utilizando um laço de repetição. A função multiplica
sucessivamente os números inteiros de 1 até o valor informado e retorna
o resultado do fatorial. Ao final, o programa calcula e exibe o fatorial
de 4.
"""

def fatorial(n):
    fat = 1 
    x = 1
    while x <=n :
        fat = fat * x
        x = x + 1
    return fat

print(fatorial(4))