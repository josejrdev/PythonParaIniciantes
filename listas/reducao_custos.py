listaGastos = [800, 1200, 300, 150, 500, 900]
listaGastosMenores500 = []
for i in range(len(listaGastos)):
  if listaGastos[i] < 500:
    listaGastosMenores500.append(listaGastos[i])
print(f"Gastos menores que 500: {listaGastosMenores500}")