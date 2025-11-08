cont = 1
valorTotalAVista = 0.0
valorTotalAPrazo = 0.0
valorTotalCompras = 0.0
valorPrestacao1APrazo = 0.0
while cont <= 15:
  codigoTransacao = int(input("Digite o código da transação(0 à vista, 1 a prazo): "))
  valorTransacao = float(input("Digite o valor da transação: R$"))
  if codigoTransacao == 0:
    valorTotalAVista = valorTotalAVista + valorTransacao
  elif codigoTransacao == 1:
    valorTotalAPrazo = valorTotalAPrazo + valorTransacao
  valorTotalCompras = valorTotalCompras + valorTransacao
  cont = cont + 1
valorPrestacao1APrazo = valorTotalAPrazo / 3
print(f"Valor total de compras a vista: R${valorTotalAVista:.2f}")
print(f"Valor total de compras a prazo: R${valorTotalAPrazo:.2f}")
print(f"Valor total das compras efetuadas: R${valorTotalCompras:.2f}")
print(f"Valor da primeira prestação das compras a prazo: R${valorPrestacao1APrazo:.2f}")