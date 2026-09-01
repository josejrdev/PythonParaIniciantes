"""
Programa que analisa os gastos registrados por hora e identifica
valores suspeitos. Um gasto é considerado suspeito quando é superior
a 30% do gasto registrado na hora anterior. Ao final, armazena e exibe
os valores suspeitos e seus respectivos índices na lista original.
"""
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