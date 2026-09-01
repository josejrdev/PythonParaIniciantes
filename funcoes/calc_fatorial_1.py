"""
Algoritmo que define uma função para calcular o fatorial de um número
inteiro utilizando um laço de repetição. A função realiza multiplicações
sucessivas dos valores de x até chegar a 1 e retorna o resultado do
fatorial. Ao final, o programa calcula e exibe o fatorial de 0.
"""

def fatorial(x):
    f = 1
    while x > 1:
        f = f * x
        x = x - 1
    return f

print(fatorial(0))