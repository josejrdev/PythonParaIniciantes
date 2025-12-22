listaNomes = []
nomeMaisLongo = ""
qtdNomesIniciamComA = 0
cont = 0
while cont < 10:
  nome = input("Digite o nome: ")
  listaNomes.append(nome)
  if len(nome) > len(nomeMaisLongo):
    nomeMaisLongo = nome
  if listaNomes[cont][0] == "A":
    qtdNomesIniciamComA = qtdNomesIniciamComA + 1
  cont = cont + 1
listaNomes2A6 = listaNomes[2:7]
print(f"O nome mais longo é: {nomeMaisLongo}")
print(f"Os nomes de 2 a 6(índices) são: {listaNomes2A6}")
print(f"Quantidade de nomes que iniciam com A: {qtdNomesIniciamComA}")