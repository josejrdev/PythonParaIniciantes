valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
qtdAnosPagar = int(input("Digite a quantidade de anos: "))
limiteValor = salario * 30 / 100
calcPrestacao = valorCasa / (qtdAnosPagar * 12)
if calcPrestacao > limiteValor:
    print("Empréstimo não aprovado.")
else:
    print("Empréstimo aprovado, Valor: R$%.2f mensais" %calcPrestacao)