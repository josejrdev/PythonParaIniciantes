valorInvestimento = float(input("Digite o valor do investimento: "))
tipoInvestimento = int(input("Digite o tipo de investimento: "))
if tipoInvestimento == 1:
  calcInvestimento = valorInvestimento + (valorInvestimento * 3 / 100)
  nomeInvestimento = "Poupança"
elif tipoInvestimento == 2:
  calcInvestimento = valorInvestimento + (valorInvestimento * 4 / 100)
  nomeInvestimento = "Fundo de renda fixa"
print(f"Valor: {calcInvestimento:.2f} Investimento: {nomeInvestimento}")