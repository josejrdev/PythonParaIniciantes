dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resto = dividendo
while resto >= divisor:
    resto = resto - divisor
print(f"O Resto é {resto}")