"""
Programa que solicita 10 nomes ao usuário e os armazena em uma lista.
Durante a entrada, identifica o nome mais longo e conta quantos nomes
começam com a letra "A". Ao final, cria uma nova lista contendo os
nomes dos índices 2 a 6 e exibe o nome mais longo, esses nomes e a
quantidade de nomes iniciados com "A".
"""

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