listaGastosHora = [
  900, 600, 700, 1500,
  5000, 9000, 9600, 9789,
  9900, 30000, 40000, 45000
]
listaValoresSuspeitos = []
listaIndicesValoresSuspeitos = []
cont = 1
while cont < len(listaGastosHora):
  anteriorAumentado30porCento = ((listaGastosHora[cont - 1] * 30 / 100) + listaGastosHora[cont - 1])
  if listaGastosHora[cont] > anteriorAumentado30porCento:
    listaValoresSuspeitos.append(listaGastosHora[cont])
    listaIndicesValoresSuspeitos.append(cont)
  cont = cont + 1
print(f"Valores suspeitos: {listaValoresSuspeitos}")
print(f"O indice de cada valor suspeito: {listaIndicesValoresSuspeitos}")