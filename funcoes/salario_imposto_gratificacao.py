def calc_salario(salario_bruto, taxa_imposto=7, limite_1=350, valor_limite_1=100, limite_2=600, valor_limite_2=75, limite_3=900, valor_limite_3=50, valor_limite_4=35):
  if salario_bruto > limite_3:
    calc_gratificacao = gratificacao(salario_bruto, valor_limite_4)
    calc_imposto = imposto(salario_bruto, taxa_imposto)
    calc_salario = salario_bruto + calc_gratificacao - calc_imposto
    return calc_salario
  elif salario_bruto > limite_2:
    calc_gratificacao = gratificacao(salario_bruto, valor_limite_3)
    calc_imposto = imposto(salario_bruto, taxa_imposto)
    calc_salario = salario_bruto + calc_gratificacao - calc_imposto
    return calc_salario
  elif salario_bruto > limite_1:
    calc_gratificacao = gratificacao(salario_bruto, valor_limite_2)
    calc_imposto = imposto(salario_bruto, taxa_imposto)
    calc_salario = salario_bruto + calc_gratificacao - calc_imposto
    return calc_salario
  else:
    calc_gratificacao = gratificacao(salario_bruto, valor_limite_1)
    calc_imposto = imposto(salario_bruto, taxa_imposto)
    calc_salario = salario_bruto + calc_gratificacao - calc_imposto
    return calc_salario
def imposto(salario_bruto, taxa_imposto):
  calc_imposto = salario_bruto * taxa_imposto / 100
  return calc_imposto
def gratificacao(salario_bruto, valor_limite):
  calc_gratificacao = valor_limite
  return calc_gratificacao
salario_bruto_funcionario = float(input("Salário bruto do funcionário: "))
print(calc_salario(salario_bruto_funcionario))