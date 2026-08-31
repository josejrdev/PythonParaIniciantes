"""
Algoritmo que lê a idade de várias pessoas até que o valor 0 seja
informado. O programa contabiliza a quantidade de idades informadas,
soma os valores e calcula e exibe a média das idades.
"""

gerenciador = 1
somaIdades = 0
qtdIdades = 0

while gerenciador == 1:
  idade = int(input("Digite a idade(0 para encerrar): "))
  if idade == 0:
    gerenciador = 0
  else:
    qtdIdades = qtdIdades + 1
    somaIdades = somaIdades + idade
mediaIdades = somaIdades / qtdIdades

print(f"A média de idades é: {mediaIdades:.2f}")