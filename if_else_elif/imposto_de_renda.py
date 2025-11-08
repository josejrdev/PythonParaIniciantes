valorPago = float(input("Digite o valor pago: "))
if valorPago <= 1000:
    print("Sem imposto")
elif valorPago > 1000 and valorPago <= 3000:
    calcImpostoTaxa2 = (valorPago - 1000) * 20 / 100
    valorFinalTaxa2 = valorPago - calcImpostoTaxa2
    print(f"Imposto: {calcImpostoTaxa2:.2f} Valor final do salário: R${valorFinalTaxa2:.2f}")
elif valorPago > 3000:
    calcImpostoTaxa2 = (3000 - 1000) * 20 / 100
    calcImpostoTaxa3 = (valorPago - 3000) * 35 / 100
    SomaImpostoTaxas = calcImpostoTaxa2 + calcImpostoTaxa3
    valorFinalTaxa3 = valorPago - SomaImpostoTaxas
    print(f"Imposto: R${SomaImpostoTaxas:.2f} R$ Valor final do salário: R${valorFinalTaxa3:.2f}")