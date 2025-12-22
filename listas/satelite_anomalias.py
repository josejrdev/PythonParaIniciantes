listaLuminosidades = [
  12, 18, 20, 22, 25, 28, 30, 32, 35, 40,
  38, 42, 45, 47, 50, 55, 58, 60, 62, 65,
  68, 70, 72, 75, 78, 80, 82, 85, 88, 90,
  92, 95, 98, 100, 102, 105, 108, 110, 112, 115,
  10, 15, 18, 22, 27, 29, 31, 33, 37, 41,
  44, 46, 49, 53, 56, 59, 61, 63, 67, 71,
  73, 76, 79, 83, 86, 89, 91, 94, 97, 99,
  101, 104, 107, 109, 111, 114, 116, 118, 120, 123,
  14, 19, 23, 26, 29, 34, 36, 39, 43, 48,
  52, 54, 57, 64, 66, 69, 74, 77, 81, 84,
  87, 93, 96, 103, 106, 113, 117, 119, 121, 124,
  126, 128, 130, 132, 134, 136, 138, 140, 142, 144,
  11, 16, 21, 24, 30, 38, 41, 45, 51, 58,
  63, 68, 72, 75, 79, 82, 86, 90, 94, 99,
  103, 108, 112, 116, 120, 125, 129, 133, 137, 141,
  145, 148, 150, 152, 155, 158, 160, 162, 165, 168,
  13, 17, 19, 23, 27, 31, 35, 37, 42, 46,
  50, 55, 60, 66, 71, 76, 81, 88, 92, 97,
  101, 106, 110, 115, 119, 122, 127, 131, 135, 139,
  143, 147, 149, 153, 157, 161, 164, 167, 169, 172
]
cont = 0
somaLuminosidades = 0
listaLuminosidadesAcimaDe150 = []
listaMaiorSequencia = []
listaSequenciaAtual = []
while cont < len(listaLuminosidades):
  somaLuminosidades = somaLuminosidades + listaLuminosidades[cont]
  cont = cont + 1
mediaGeral = somaLuminosidades / 200
cont = 0
while cont < len(listaLuminosidades):
  if listaLuminosidades[cont] > int(mediaGeral * 150 / 100):
    listaLuminosidadesAcimaDe150.append(listaLuminosidades[cont])
  cont = cont + 1
cont = 1
listaSequenciaAtual = [listaLuminosidades[0]]
while cont < len(listaLuminosidades):
  if listaLuminosidades[cont] > listaLuminosidades[cont - 1]:
    listaSequenciaAtual.append(listaLuminosidades[cont])
  else:
    if len(listaSequenciaAtual) > len(listaMaiorSequencia):
      listaMaiorSequencia = listaSequenciaAtual
    listaSequenciaAtual = [listaLuminosidades[cont]]
  cont = cont + 1
if len(listaSequenciaAtual) > len(listaMaiorSequencia):
  listaMaiorSequencia = listaSequenciaAtual
print(f"Média geral de luminosidades: {mediaGeral:.2f}")
print(f"Luminosidades acima de 150%: {listaLuminosidadesAcimaDe150}")
print(f"Maior sequência contínua crescnte: {listaMaiorSequencia}")