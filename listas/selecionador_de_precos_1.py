"""
Programa que percorre uma lista de preços e identifica os valores
menores que 800. Os preços que atendem a essa condição são armazenados
em uma nova lista e, ao final, exibidos na tela.
"""
listaPrecos = [1500, 700, 200, 2500, 600, 300]
listaPrecosMenor800 = []
cont = 0
while cont < len(listaPrecos):
  if listaPrecos[cont] < 800:
    listaPrecosMenor800.append(listaPrecos[cont])
  cont = cont + 1
print(f"Preços menores que 800: {listaPrecosMenor800}")