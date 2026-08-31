"""
Algoritmo que calcula o fatorial de um número inteiro utilizando um
laço de repetição. O programa multiplica sucessivamente os números
inteiros de 1 até o número informado e, ao final, exibe o resultado
do fatorial.
"""

numero = int(input("Digite um número: "))
cont = 1
fatorial = 1

while cont <= numero:
  fatorial = fatorial * cont
  cont = cont + 1
print(fatorial)