"""
Algoritmo que calcula a evolução de um investimento durante 24 meses,
considerando um depósito inicial, uma taxa de juros e um valor mensal
depositado pelo usuário. A cada mês, o programa adiciona o depósito
mensal, calcula os juros sobre o valor acumulado e exibe o saldo do mês.
Ao final, exibe o valor total acumulado.
"""

depositoInicial = float(input("Digite o deposito inicial: "))
taxaJuros = float(input("Digite a taxa de juros: "))
cont = 1
juros = 0
valor = depositoInicial

while cont <= 24:
    valorMensal = float(input("Digite o valor mensal: "))
    juros = (valor + valorMensal) * taxaJuros / 100
    valor = valor + valorMensal + juros
    print(f"Valor mês {cont}: R$ {valor:.2f}")
    cont = cont + 1
    
print(f"Valor total: R$ {valor:.2f}")