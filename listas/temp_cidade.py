listaTempCidade = [29, 31, 32, 27, 26, 30, 33]
cont = 0
somaTemp = 0
diasAcimaDe30 = listaTempCidade[1:3] + listaTempCidade[6:7]
ultimosTresDias = listaTempCidade[4:]
while cont < len(listaTempCidade):
  somaTemp = somaTemp + listaTempCidade[cont]
  cont = cont + 1
mediaTemp = somaTemp / cont
print(f"Média temperatura: {mediaTemp:.2f}")
print(f"Dias acima de 30: {diasAcimaDe30}")
print(f"Últimos três dias: {ultimosTresDias}")