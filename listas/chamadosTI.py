listaNiveisChamados = [
  "BAIXO", "MEDIO", "CRITICO", "MEDIO",
  "BAIXO", "CRITICO", "MEDIO", "BAIXO",
  "MEDIO", "MEDIO", "CRITICO", "BAIXO"
]
listaNivelBaixo = []
listaNivelMedio = []
listaNivelCritico = []
cont = 0
while cont < len(listaNiveisChamados):
  if listaNiveisChamados[cont] == "BAIXO":
    listaNivelBaixo.append(listaNiveisChamados[cont])
  elif listaNiveisChamados[cont] == "MEDIO":
    listaNivelMedio.append(listaNiveisChamados[cont])
  elif listaNiveisChamados[cont] == "CRITICO":
    listaNivelCritico.append(listaNiveisChamados[cont])
  cont = cont + 1
listaComPrioridades = listaNivelCritico + listaNivelMedio + listaNivelBaixo
cincoPrimeirosClassificados = listaComPrioridades[0:5]
print(f"Chamados Nível Baixo: {listaNivelBaixo}")
print(f"Chamados Nível Médio: {listaNivelMedio}")
print(f"Chamados Nível Critico: {listaNivelCritico}")
print(f"Cinco primeiros chamados classificados: {cincoPrimeirosClassificados}")