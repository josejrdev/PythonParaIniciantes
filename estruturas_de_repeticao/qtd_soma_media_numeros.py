"""
Algoritmo que lê números inteiros até que o valor 0 seja informado.
O programa contabiliza a quantidade de números digitados, calcula a
soma dos valores e, ao final, calcula e exibe a média aritmética dos
números informados.
"""

qtdNumeros = 0
somaNumeros = 0

while True:
    numeroInteiro = int(input("Digite um número inteiro: "))
    if numeroInteiro == 0:
        break
    qtdNumeros = qtdNumeros + 1
    somaNumeros = somaNumeros + numeroInteiro
if qtdNumeros != 0:
    media = somaNumeros / qtdNumeros
else:
    media = 0
    
print(f"Quantidade de números digitados: {qtdNumeros}")
print(f"Soma: {somaNumeros}")
print(f"Média Aritmética {media:.2f}")