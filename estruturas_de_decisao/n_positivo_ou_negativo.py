# Algoritmo que informa se um número é positivo, negativo ou zero.

numero = int(input("Digite um número inteiro: "))
if numero > 0:
    print(f"O número {numero} é positivo.")
elif numero < 0:
    print(f"O número {numero} é negativo.")
else:
    print(f"Número Zero")