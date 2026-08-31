""" 
Algoritmo que recebe uma temperatura em graus celsius do usuário e classifica a 
temperatura em niveis: quente, agradavel ou frio.
"""

# Coleta a temperatura em graus celsius
TempC = float(input("Digite a temperatura em Graus Celsius: "))

# estrutura de decisão com if/elif/else que realiza a classificação da temperatura
if TempC > 25:
  print("Quente.")
elif TempC <= 25 and TempC >= 10:
  print("Agradavel")
else:
  print("Frio")