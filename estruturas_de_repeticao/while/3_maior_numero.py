cont = 1
maiorNumero = -5
while cont <= 3:
  numero = int(input("Digite um número: "))
  if numero > maiorNumero:
     maiorNumero = numero
  cont = cont + 1
print(maiorNumero)