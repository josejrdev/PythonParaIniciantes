listaValores = [
  12000, 24000, 6555, 8900,
  50000, 78000, 1000, 10000,
  21000, 45500, 12000, 15000
]
listaValoresPrimeiroTrimestre = listaValores[0:3]
listaValoresSegundoTrimestre = listaValores[3:6]
listaValoresTerceiroTrimestre = listaValores[6:9]
listaValoresQuartoTrimestre = listaValores[9:12]
maiorValorPrimeiroTrimestre = -5.0
maiorValorSegundoTrimestre = -5.0
maiorValorTerceiroTrimestre = -5.0
maiorValorQuartoTrimestre = -5.0
menorValorPrimeiroTrimestre = 9999999
menorValorSegundoTrimestre = 9999999
menorValorTerceiroTrimestre = 9999999
menorValorQuartoTrimestre = 9999999
cont = 0
while cont < len(listaValoresPrimeiroTrimestre):
  if listaValoresPrimeiroTrimestre[cont] > maiorValorPrimeiroTrimestre:
    maiorValorPrimeiroTrimestre = listaValoresPrimeiroTrimestre[cont]
  if listaValoresPrimeiroTrimestre[cont] < menorValorPrimeiroTrimestre:
    menorValorPrimeiroTrimestre = listaValoresPrimeiroTrimestre[cont]
  cont = cont + 1
cont = 0
while cont < len(listaValoresSegundoTrimestre):
  if listaValoresSegundoTrimestre[cont] > maiorValorSegundoTrimestre:
    maiorValorSegundoTrimestre = listaValoresSegundoTrimestre[cont]
  if listaValoresSegundoTrimestre[cont] < menorValorSegundoTrimestre:
    menorValorSegundoTrimestre = listaValoresSegundoTrimestre[cont]
  cont = cont + 1
cont = 0
while cont < len(listaValoresTerceiroTrimestre):
  if listaValoresTerceiroTrimestre[cont] > maiorValorTerceiroTrimestre:
    maiorValorTerceiroTrimestre = listaValoresTerceiroTrimestre[cont]
  if listaValoresTerceiroTrimestre[cont] < menorValorTerceiroTrimestre:
    menorValorTerceiroTrimestre = listaValoresTerceiroTrimestre[cont]
  cont = cont + 1
cont = 0
while cont < len(listaValoresQuartoTrimestre):
  if listaValoresQuartoTrimestre[cont] > maiorValorQuartoTrimestre:
    maiorValorQuartoTrimestre = listaValoresQuartoTrimestre[cont]
  if listaValoresQuartoTrimestre[cont] < menorValorQuartoTrimestre:
    menorValorQuartoTrimestre = listaValoresQuartoTrimestre[cont]
  cont = cont + 1
print(f"1° Trimestre, Maior valor: R$ {maiorValorPrimeiroTrimestre:.2f} Menor valor: R$ {menorValorPrimeiroTrimestre:.2f}")
print(f"2° Trimestre, Maior valor: R$ {maiorValorSegundoTrimestre:.2f} Menor valor: R$ {menorValorSegundoTrimestre:.2f}")
print(f"3° Trimestre, Maior valor: R$ {maiorValorTerceiroTrimestre:.2f} Menor valor: R$ {menorValorTerceiroTrimestre:.2f}")
print(f"4° Trimestre, Maior valor: R$ {maiorValorQuartoTrimestre:.2f} Menor valor: R$ {menorValorQuartoTrimestre:.2f}")