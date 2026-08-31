"""
Algoritmo que calcula o resto de uma divisão inteira utilizando apenas
operações de subtração. O programa subtrai repetidamente o divisor do
dividendo até que o valor restante seja menor que o divisor e, ao final,
exibe o resto da divisão.
"""

dividendo = int(input("Dividendo: "))
divisor = int(input("Divisor: "))
resto = dividendo

while resto >= divisor:
    resto = resto - divisor
    
print(f"O Resto é {resto}")