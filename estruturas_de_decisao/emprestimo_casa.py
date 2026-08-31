""" 
Algoritmo que calcula o valor de prestação de uma casa
e se esse valor foi maior que um determinado valor limite
não aprova um emprestimo, se não for o emprestimo é aprovado.
"""

# coletando os dados do usuário 
valorCasa = float(input("Digite o valor da casa: "))
salario = float(input("Digite o seu salário: "))
qtdAnosPagar = int(input("Digite a quantidade de anos: "))

# realizando calculos do limite e da prestação
limiteValor = salario * 30 / 100
calcPrestacao = valorCasa / (qtdAnosPagar * 12)

# par if/else para decidir se o empréstimo será ou não aprovado
if calcPrestacao > limiteValor:
    print("Empréstimo não aprovado.")
else:
    print("Empréstimo aprovado, Valor: R$%.2f mensais" %calcPrestacao)