"""
Algoritmo que calcula a evolução de um investimento durante 24 meses,
considerando um depósito inicial e uma taxa de juros. A cada mês, os
juros são calculados sobre o valor acumulado e adicionados ao saldo.
O programa exibe o valor do investimento ao final de cada mês e,
ao final, apresenta o valor total acumulado.
"""

depositoInicial = float(input("Digite o deposito inicial: "))
taxaJuros = float(input("Digite a taxa de juros: "))
cont = 1
juros = 0
valor = depositoInicial

while cont <= 24:
    juros = valor * taxaJuros / 100
    valor = valor + juros
    print(f"Valor mês {cont}: R$ {valor:.2f}")
    cont = cont + 1
print(f"Valor total: R$ {valor:.2f}")