listaVelocidades = [
  42, 38, 45, 47, 50, 41, 39, 43, 44, 46, 48, 40,
  52, 49, 47, 45, 43, 41, 40, 38, 42, 44, 46, 50,
  55, 58, 60, 62, 59, 57, 61, 63, 65, 66, 64, 62,
  60, 59, 57, 56, 58, 60, 62, 64, 63, 61, 59, 57,
  70, 72, 75, 78, 80, 82, 85, 88, 90, 87, 84, 82,
  79, 77, 75, 74, 73, 78, 82, 85, 88, 90, 92, 93,
  95, 94, 92, 90, 87, 85, 84, 83, 82, 81, 80, 79,
  78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67
]
listaVelocidadesManha = listaVelocidades[0:24]
listaVelocidadesTarde = listaVelocidades[24:48]
listaVelocidadesNoite = listaVelocidades[48:]
somaVelocidadesManha = 0
somaVelocidadesTarde = 0
somaVelocidadesNoite = 0
cont = 0
while cont < 24:
  somaVelocidadesManha = somaVelocidadesManha + listaVelocidadesManha[cont]
  somaVelocidadesTarde = somaVelocidadesTarde + listaVelocidadesTarde[cont]
  cont = cont + 1
cont = 0
while cont < 48:
  somaVelocidadesNoite = somaVelocidadesNoite + listaVelocidadesNoite[cont]
  cont = cont + 1
mediaVelocidadesManha = somaVelocidadesManha / 24
mediaVelocidadesTarde = somaVelocidadesTarde / 24
mediaVelocidadesNoite = somaVelocidadesNoite / 48
if mediaVelocidadesManha > mediaVelocidadesTarde and mediaVelocidadesManha > mediaVelocidadesNoite:
  print(f"O periodo da manhã com {mediaVelocidadesManha:.2f} km/h foi o mais perigoso")
elif mediaVelocidadesTarde > mediaVelocidadesManha and mediaVelocidadesTarde > mediaVelocidadesNoite:
  print(f"O periodo da tarde com {mediaVelocidadesTarde:.2f} km/h foi o mais perigoso")
else:
  print(f"O periodo da noite com {mediaVelocidadesNoite:.2f} km/h foi o mais perigoso")