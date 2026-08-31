"""
Algoritmo que calcula média ponderada de duas notas
com pesos 2 e 3 respectivamente
"""

# Coleta a primeira nota
nota_um = float(input("Digite a primeira nota: "))

# Coleta a segunda nota
nota_dois = float(input("Digite a segunda nota: "))

# Calcula a média ponderada
calc_m_p = ((nota_um * 2) + (nota_dois * 3)) / (2 + 3)

# Exibe o resultado
print(calc_m_p)