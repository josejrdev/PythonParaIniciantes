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