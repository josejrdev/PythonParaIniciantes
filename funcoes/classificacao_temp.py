def cla_temperatura(temp):
  if temp > 25:
    return "QUENTE"
  elif temp >= 10:
    return "AGRADAVEL"
  else:
    return "FRIO"
temperatura = float(input("Digite a temmperatura em graus celsius: "))
print(cla_temperatura(temperatura))