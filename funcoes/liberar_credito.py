def liberar_credito(saldo, limite_3=400, limite_2=300, limite_1=200, taxa_1=10, taxa_2=20, taxa_3=25, taxa_4=30):
  if saldo > limite_3:
    return calc_credito(saldo,taxa_4)
  elif saldo > limite_2:
    return calc_credito(saldo,taxa_3)
  elif saldo > limite_1:
    return calc_credito(saldo,taxa_2)
  else:
    return calc_credito(saldo,taxa_1)
def calc_credito(saldo, taxa):
    calc = (saldo * taxa / 100)
    return (f"Para o saldo médio: R$ {saldo:.2f} O Crédito é: R$ {calc:.2f}")
saldo_medio = float(input("Digite o saldo médio: "))
print(liberar_credito(saldo_medio))