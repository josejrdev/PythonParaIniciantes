listaBatimentosCardiacos = [
    88, 90, 92, 87, 85, 86, 89, 91, 93, 94,
    96, 97, 98, 100, 102, 105, 101, 99, 95, 94,
    92, 91, 90, 88, 87, 86, 85, 84, 83, 82,
    80, 82, 84, 86, 89, 90, 92, 93, 95, 97,
    99, 100, 102, 103, 101, 98, 96, 94, 92, 90,
    88, 87, 86, 85, 84, 83, 82, 81, 80, 79
]
listaBatimentosPrimeiroPeriodo = listaBatimentosCardiacos[0:30]
listaBatimentosSegundoPeriodo = listaBatimentosCardiacos[30:]
listaValoresAcimaDe95 = []
somaBatimentosPrimeiroPeriodo = 0
somaBatimentosSegundoPeriodo = 0
cont = 0
while cont < len(listaBatimentosPrimeiroPeriodo):
  somaBatimentosPrimeiroPeriodo = somaBatimentosPrimeiroPeriodo + listaBatimentosPrimeiroPeriodo[cont]
  cont = cont + 1
cont = 0
while cont < len(listaBatimentosSegundoPeriodo):
  somaBatimentosSegundoPeriodo = somaBatimentosSegundoPeriodo + listaBatimentosSegundoPeriodo[cont]
  cont = cont + 1
cont = 0
while cont < len(listaBatimentosCardiacos):
  if listaBatimentosCardiacos[cont] > 95:
    listaValoresAcimaDe95.append(listaBatimentosCardiacos[cont])
  cont = cont + 1
mediaBatimentosPrimeiroPeriodo = somaBatimentosPrimeiroPeriodo / 30
mediaBatimentosSegundoPeriodo = somaBatimentosSegundoPeriodo / 30
variacaoPeriodos = mediaBatimentosSegundoPeriodo - mediaBatimentosPrimeiroPeriodo
print(f"Média de batimentos do primeiro período: {mediaBatimentosPrimeiroPeriodo:.2f}")
print(f"Média de batimentos do segundo período: {mediaBatimentosSegundoPeriodo:.2f}")
print(f"Variação entre periodos de {variacaoPeriodos:.2f}")
print(f"Batimentos Cardiacos acima de 95: {listaValoresAcimaDe95}")