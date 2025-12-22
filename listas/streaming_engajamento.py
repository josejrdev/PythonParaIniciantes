listaMinutosAssistidos = [
  12, 30, 45, 22, 18,
  90, 110, 5, 8, 160,
  70, 65, 40, 33, 27,
  15, 14, 200, 250, 300
]
listaMinutosAssistidos.sort()
calcPercentual = len(listaMinutosAssistidos) * 20 / 100
listaMaiorEngajamento = listaMinutosAssistidos[int(-calcPercentual):]
listaMenorEngajamento = listaMinutosAssistidos[0:int(calcPercentual)]
print(f"20% com maior engajamento: {listaMaiorEngajamento}")
print(f"20% com menor engajamento: {listaMenorEngajamento}")