"""
Algoritmo que cria uma função para classificar temperatura
"""
def classificacao_temperatura(temp):
  if temp > 25:
    return "QUENTE"
  elif temp >= 10:
    return "AGRADAVEL"
  else:
    return "FRIO"
temperatura = float(input("Digite a temmperatura em graus celsius: "))
print(classificacao_temperatura(temperatura))