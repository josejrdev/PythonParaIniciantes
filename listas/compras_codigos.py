somaAVista = 0
somaAPrazo = 0
for i in range(15):
    codigo = input("Digite o código da transação: ")
    valor = float(input("Digite o valor da transação: "))
    if codigo == "0":
        somaAVista = somaAVista + valor
    elif codigo == "1":
        somaAPrazo = somaAPrazo + valor
somaTotal = somaAVista + somaAPrazo
prestacoesAPrazo = somaAPrazo / 3
print(f"Valor total das compras a vista: R$ {somaAVista:.2f}")
print(f"Valor total das compras a prazo: R$ {somaAPrazo:.2f}")
print(f"O Valor total de todas as compras: R$ {somaTotal:.2f}")
print(f"O Valor da primeira prestação das compras a prazo: R$ {prestacoesAPrazo:.2f}")