"""
Programa que verifica se um número inteiro é par ou ímpar.
A função verificarPar() utiliza o operador de módulo (%) para
determinar se o número é divisível por 2. A função parOuImpar()
utiliza esse resultado para informar se o número é par ou ímpar.
"""

def verificarPar(x):
    return x % 2 == 0

def parOuImpar(n):
    if verificarPar(n) == True:
        return (f"O Número {n} é par.")
    else:
        return (f"O Número {n} é impar.")
    
print(parOuImpar(3))