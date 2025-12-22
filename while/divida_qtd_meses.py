valorDivida = float(input("Digite o valor inicial da divida: "))
taxaJuros = float(input("Digite o valor da taxa de juros: "))
valorMensalPago = float(input("Digite o valor pago mensalmeente: "))
saldo = valorDivida
somaJuros = 0
meses = 0
while saldo > 0:
    juros = saldo * taxaJuros / 100
    somaJuros = somaJuros + juros
    saldo = saldo + juros
    saldo = saldo - valorMensalPago
    meses = meses + 1
if saldo < 0:
    saldo = 0
valorTotal = valorDivida + somaJuros
print(f"Quantidade de meses para pagar divida: {meses}")
print(f"Total de juros pago: R$ {somaJuros:.2f}")
print(f"Valor total pago: R$ {valorTotal:.2f}")