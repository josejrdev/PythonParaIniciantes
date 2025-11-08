numero1 = int(input("Dividendo: "))
numero2 = int(input("Divisor: "))

resto = numero1
vezes = 0

while resto >= numero2:
    resto -= numero2
    vezes += 1
print("Resto:", resto)
print("Quociente:", vezes)
