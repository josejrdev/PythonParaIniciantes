"""
Algoritmo que lê valores inteiros e positivos até que o valor 0 seja
informado. O programa valida os valores digitados, identifica o maior
e o menor valor entre os números informados e, ao final, exibe esses
dois valores.
"""

gerenciador = 1
maiorValor = -5.9
menorValor = 1000000000
while gerenciador == 1:
  valor = int(input("Digite um valor inteiro e positivo(0 para encerrar): "))
  while valor < 0:
    valor = int(input("Valor inválido, Digite um valor inteiro e positivo(0 para encerrar): "))   
  if valor == 0:
    gerenciador = 0
  else:
    if valor > maiorValor:
      maiorValor = valor
    if valor < menorValor:
      menorValor = valor
print(f"Maior valor: {maiorValor}")
print(f"Menor valor: {menorValor}")