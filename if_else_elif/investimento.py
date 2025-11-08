valorInvestimento = float(input("Digite o valor do investimento: "))
tipoInvestimento = int(input("Digite o tipo de investimento: "))
if tipoInvestimento == 1:
  calcInvestimento = valorInvestimento + (valorInvestimento * 3 / 100)
  investimento = "Poupança"
elif tipoInvestimento == 2:
  calcInvestimento = valorInvestimento + (valorInvestimento * 4 / 100)
  investimento = "Fundo de renda fixa"
print(f"Valor: {calcInvestimento:.2f} Investimento: {investimento}")