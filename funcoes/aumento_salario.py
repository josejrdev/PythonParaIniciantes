def verificar_direito(salario, limite=500):
  if salario < limite:
    return True
def aumento_salario(salario, taxa_aumento=30):
  if verificar_direito(salario):
    calc_salario = salario + (taxa_aumento * salario / 100)
    return (f"Com direito a aumento, Salário final: R$ {calc_salario:.2f}")
  else:
    return (f"O salário R$ {salario:.2f}, Não tem direito a aumento.")
salario_funcionario = float(input("Digite o salário do funcionário: "))
print(f"Situação do salário: {aumento_salario(salario_funcionario)}")