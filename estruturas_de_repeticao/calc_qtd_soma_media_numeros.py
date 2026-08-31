"""
Algoritmo que lê números inteiros até que o valor 0 seja informado.
O programa contabiliza a quantidade de números digitados, calcula a
soma dos valores e, ao final, calcula e exibe a média aritmética dos
números informados.
"""

qtdNumeros = 0
somaNumeros = 0

while True:
    numero = int(input("Digite o número(0 para encerrar): "))
    if numero == 0:
        break
    qtdNumeros = qtdNumeros + 1
    somaNumeros = somaNumeros + numero
if qtdNumeros != 0:
    media = somaNumeros / qtdNumeros
else:
    media = 0
    
print(f"Quantidade de números: {qtdNumeros}")
print(f"Soma dos números: {somaNumeros}")
print(f"Média aritmética: {media}")