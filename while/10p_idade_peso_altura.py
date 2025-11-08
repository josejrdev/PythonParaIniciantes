cont = 1
somaIdades = 0
qtdPesoMaior90AlturaMenor150 = 0
qtdAlturaMaior190 = 0
qtdIdadeMaior10Menor30 = 0
while cont <= 10:
  idade = float(input("Digite a idade da pessoa: "))
  peso = float(input("Digite o peso da pessoa: "))
  altura = float(input("Digite a altura da pessoa: "))
  somaIdades = somaIdades + idade
  if peso > 90 and altura < 1.50:
    qtdPesoMaior90AlturaMenor150 = qtdPesoMaior90AlturaMenor150 + 1
  if altura > 1.90:
    qtdAlturaMaior190 = qtdAlturaMaior190 + 1
    if idade >= 10 and idade <= 30:
      qtdIdadeMaior10Menor30 = qtdIdadeMaior10Menor30 + 1
  cont = cont + 1
mediaIdade = somaIdades / 10
if qtdAlturaMaior190 != 0:
  percentagemPessoasIdade10e30 = qtdIdadeMaior10Menor30 / qtdAlturaMaior190 * 100
else:
  percentagemPessoasIdade10e30 = 0
print(f"A média de idade: {mediaIdade:.2f}")
print(f"Quantidade de pessoas com peso superior a 90 quilos e altura inferior a 1,50: {qtdPesoMaior90AlturaMenor150}")
print(f"Percentagem de pessoas com idade entre 10 e 30 anos entre pessoas que medem mais de 1,90 metro: {percentagemPessoasIdade10e30:.1f}%")