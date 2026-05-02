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