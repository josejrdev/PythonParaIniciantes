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