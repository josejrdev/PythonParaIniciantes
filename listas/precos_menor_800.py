listaPrecos = [1500, 700, 200, 2500, 600, 300]
listaPrecosMenor800 = []
cont = 0
while cont < len(listaPrecos):
  if listaPrecos[cont] < 800:
    listaPrecosMenor800.append(listaPrecos[cont])
  cont = cont + 1
print(f"Preços menores que 800: {listaPrecosMenor800}")