"""
Algoritmo que lê um número inteiro e exibe a sua tabuada de 1 a 10.
O programa realiza as multiplicações utilizando um laço de repetição
e exibe cada resultado correspondente.
"""

numero = int(input("Digite um número: "))
cont = 1

while cont <= 10:
  tabResultado = numero * cont
  print(f"{numero} x {cont} = {tabResultado}")
  cont = cont + 1