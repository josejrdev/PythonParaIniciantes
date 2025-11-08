valorDivida = float(input("Digite o valor da dívida: "))
taxaJuros = float(input("Digite a taxa de juros mensal (%): "))
valorMensal = float(input("Digite o valor mensal que será pago: "))

divida = valorDivida
meses = 0
total_pago = 0
total_juros = 0

# enquanto ainda houver dívida
while divida > 0:
    juros_mes = divida * taxaJuros / 100   # calcula o juro do mês
    divida = divida + juros_mes - valorMensal  # aplica juro e pagamento
    meses += 1
    total_pago += valorMensal
    total_juros += juros_mes

print(f"\nA dívida será quitada em {meses} meses.")
print(f"Total pago: R${total_pago:.2f}")
print(f"Total de juros pagos: R${total_juros:.2f}")
