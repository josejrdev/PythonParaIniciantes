"""
Programa que calcula o salário líquido de um funcionário a partir do
salário bruto informado. O programa aplica um imposto de 7% sobre o
salário bruto e adiciona uma gratificação fixa de acordo com a faixa
salarial: R$ 100,00 para salários de até R$ 350,00, R$ 75,00 para
salários acima de R$ 350,00 até R$ 600,00, R$ 50,00 para salários
acima de R$ 600,00 até R$ 900,00 e R$ 35,00 para salários acima de
R$ 900,00. Ao final, exibe o salário resultante após a gratificação
e o desconto do imposto.
"""
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