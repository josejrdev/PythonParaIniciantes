listaConsumo = [
  12, 15, 18, 20, 22, 25, 30, 28, 26, 24,
  40, 42, 38, 36, 34, 33, 31, 29, 27, 26,
  25, 23, 22, 21, 20, 19, 18, 17, 16, 15
]
listaDezPrimeiros = listaConsumo[0:10]
somaDezPrimeiros = 0
cont = 0
while cont < len(listaDezPrimeiros):
  somaDezPrimeiros = somaDezPrimeiros + listaDezPrimeiros[cont]
  cont = cont + 1
listaDezUltimos = listaConsumo[-10:]
somaDezUltimos = 0
cont = 0
while cont < len(listaDezUltimos):
  somaDezUltimos = somaDezUltimos + listaDezUltimos[cont]
  cont = cont + 1
maiorSoma = 0
listaMaiorBloco = []
cont = 0
while cont <= len(listaConsumo) - 5:
  listaBlocoAtual = listaConsumo[cont:cont+5]
  somaBlocoAtual = 0
  x = 0
  while x < len(listaBlocoAtual):
    somaBlocoAtual = somaBlocoAtual + listaBlocoAtual[x]
    x = x + 1
  if somaBlocoAtual > maiorSoma:
    maiorSoma = somaBlocoAtual
    listaMaiorBloco = listaBlocoAtual
  cont = cont + 1
print(f"A soma dos dez primeiros é: {somaDezPrimeiros}")
print(f"A soma dos dez últimos é: {somaDezUltimos}")
print(f"O maior bloco contínuo de cinco valores é: {listaMaiorBloco}")
print(f"A soma do maior bloco contínuo de cinco valores é: {maiorSoma}")