listaTemperaturas = [
  12, 15, 18, 20, 22, 25, 27, 30, 28, 26,
  24, 23, 21, 19, 17, 16, 14, 13, 15, 18,
  20, 22, 24, 26, 29, 31, 33, 32, 30, 28,
  26, 25, 23, 21, 20, 18, 17, 16, 14, 13,
  12, 14, 16, 18, 20, 23, 25, 27, 29, 31,
  33, 35, 34, 32, 30, 28, 26, 24, 22, 21,
  19, 17, 16, 18, 20, 23, 25, 28, 30, 33,
  35, 36, 34, 32, 30, 27, 25, 23, 21, 19,
  17, 15, 14, 16, 18, 20, 22, 24, 26, 28
]
listaPrimeiroTrimestre = listaTemperaturas[0:30]
listaSegundoTrimestre = listaTemperaturas[30:60]
listaTerceiroTrimestre = listaTemperaturas[60:90]
cont = 0
minPrimeiro = listaPrimeiroTrimestre[0]
maxPrimeiro = listaPrimeiroTrimestre[0]
while cont < len(listaPrimeiroTrimestre):
  if listaPrimeiroTrimestre[cont] < minPrimeiro:
    minPrimeiro = listaPrimeiroTrimestre[cont]
  if listaPrimeiroTrimestre[cont] > maxPrimeiro:
    maxPrimeiro = listaPrimeiroTrimestre[cont]
  cont = cont + 1
amplitudePrimeiro = maxPrimeiro - minPrimeiro
cont = 0
minSegundo = listaSegundoTrimestre[0]
maxSegundo = listaSegundoTrimestre[0]
while cont < len(listaSegundoTrimestre):
  if listaSegundoTrimestre[cont] < minSegundo:
    minSegundo = listaSegundoTrimestre[cont]
  if listaSegundoTrimestre[cont] > maxSegundo:
    maxSegundo = listaSegundoTrimestre[cont]
  cont = cont + 1
amplitudeSegundo = maxSegundo - minSegundo
cont = 0
minTerceiro = listaTerceiroTrimestre[0]
maxTerceiro = listaTerceiroTrimestre[0]
while cont < len(listaTerceiroTrimestre):
  if listaTerceiroTrimestre[cont] < minTerceiro:
    minTerceiro = listaTerceiroTrimestre[cont]
  if listaTerceiroTrimestre[cont] > maxTerceiro:
    maxTerceiro = listaTerceiroTrimestre[cont]
  cont = cont + 1
amplitudeTerceiro = maxTerceiro - minTerceiro
trimestreMaisInstavel = ""
if amplitudePrimeiro > amplitudeSegundo and amplitudePrimeiro > amplitudeTerceiro:
  trimestreMaisInstavel = "Primeiro trimestre"
elif amplitudeSegundo > amplitudePrimeiro and amplitudeSegundo > amplitudeTerceiro:
  trimestreMaisInstavel = "Segundo trimestre"
else:
  trimestreMaisInstavel = "Terceiro trimestre"
print(f"Amplitude do primeiro trimestre: {amplitudePrimeiro}")
print(f"Amplitude do segundo trimestre: {amplitudeSegundo}")
print(f"Amplitude do terceiro trimestre: {amplitudeTerceiro}")
print(f"Trimestre mais instável: {trimestreMaisInstavel}")