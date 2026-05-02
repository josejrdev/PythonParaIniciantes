gerenciador = 1
somaAlturasIdadeMaior50 = 0.0
qtdPessoasAlturaMaior50 = 0
while gerenciador == 1:
  idade = int(input("Digite a idade da pessoa: "))
  if idade <= 0:
    gerenciador = 0
  else:
    altura = float(input("Digite a altura da pessoa: "))
    if idade > 50:
      somaAlturasIdadeMaior50 = somaAlturasIdadeMaior50 + altura
      qtdPessoasAlturaMaior50 = qtdPessoasAlturaMaior50 + 1
if qtdPessoasAlturaMaior50 != 0:
  mediaAlturaIdadeMaior50 = somaAlturasIdadeMaior50 / qtdPessoasAlturaMaior50
else:
  mediaAlturaIdadeMaior50 = 0
print(f"Média de altura de pessoas com mais de 50 anos: {mediaAlturaIdadeMaior50:.2f}")