saldoMedio = float(input("Digite o saldo médio do cliente: "))
if saldoMedio > 400:
  calcCredito = saldoMedio * 30 / 100
elif saldoMedio > 300 and saldoMedio <= 400:
  calcCredito = saldoMedio * 25 / 100
elif saldoMedio > 200 and saldoMedio <= 300:
  calcCredito = saldoMedio * 20 / 100
else:
  calcCredito = saldoMedio * 10 / 100
print(f"Saldo médio R${saldoMedio:.2f} e crédito: R${calcCredito:.2f}")