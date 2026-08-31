"""
Algoritmo que calcula o fatorial de um número inteiro positivo utilizando
um laço de repetição. O programa realiza multiplicações sucessivas pelo
valor atual do número até chegar a 1 e, ao final, exibe o resultado do
fatorial.
"""

numero = int(input("Digite um número: "))
fatorial = 1

while numero > 0:
  fatorial = fatorial * numero
  numero = numero - 1
print(fatorial)