"""
Algoritmo que lê 10 números inteiros, identifica quais são pares e quais
são primos e calcula separadamente a soma dos números pares e a soma dos
números primos. Para verificar se um número é primo, o programa conta
quantos divisores inteiros ele possui.
"""

cont = 1
somaNumerosPares = 0
somaNumerosPrimos = 0

while cont <= 10:
  numeros = int(input(f"Digite o {cont}° número: "))
  if numeros % 2 == 0:
    somaNumerosPares = somaNumerosPares + numeros
  if numeros > 1:
    divisores = 0
    i = 1
    while i <= numeros:
      if numeros % i == 0:
        divisores = divisores + 1
      i = i + 1
    if divisores == 2: 
      somaNumerosPrimos = somaNumerosPrimos + numeros
  cont = cont + 1
print(f"A soma dos números pares é: {somaNumerosPares}")
print(f"A soma dos números primos é: {somaNumerosPrimos}")