"""
Programa que calcula aproximadamente quantos salários mínimos
correspondem ao salário de um funcionário. A função quantos_salarios_m()
utiliza a divisão inteira para determinar a quantidade de salários
mínimos contida no salário informado.
"""
def quantos_salarios_m(s_f,s_m):
  calc = s_f // s_m
  return calc
salario_funcionario = float(input("Digite o valor do salário do funcionário: "))
salario_minimo = float(input("Digite o valor do salário minimo: "))
print("O funcionário recebe %d salários minimos" %quantos_salarios_m(s_m=salario_minimo,s_f=salario_funcionario))