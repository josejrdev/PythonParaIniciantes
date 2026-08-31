"""
Algoritmo que calcula o quociente e o resto de uma divisão inteira
utilizando apenas operações de subtração, sem utilizar o operador
de divisão. O programa realiza subtrações sucessivas do divisor
até que o restante seja menor que o divisor.
"""

numero1 = int(input("Dividendo: "))
numero2 = int(input("Divisor: "))

resto = numero1
vezes = 0

while resto >= numero2:
    resto -= numero2
    vezes += 1
print("Resto:", resto)
print("Quociente:", vezes)
