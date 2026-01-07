def numero_e(n):
  if n > 0:
    return "Positivo"
  elif n == 0:
    return "Número 0"
  else:
    return "Número negativo"
numero = int(input("Digite o número: "))
print(numero_e(numero))