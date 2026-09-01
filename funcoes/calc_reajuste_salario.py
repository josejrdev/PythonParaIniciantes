"""
Programa que calcula o reajuste salarial de um funcionário de acordo
com o seu salário atual. Funcionários que recebem até R$ 300,00 têm
um aumento de 35%, enquanto aqueles que recebem acima desse valor
têm um aumento de 15%. Ao final, o programa exibe o salário após
o reajuste.
"""
def reajuste_salario(salario, p_aumento_1=15, p_aumento_2=35, limite=300):
  if salario <= limite:
    return calc_salario(salario,p_aumento_2)
  else:
    return calc_salario(salario,p_aumento_1)
def calc_salario(salario,p_aumento):
  calc = salario + (salario * p_aumento / 100)
  return calc
salario = float(input("Digite o salário do funcionário: "))
print("Salário com reajuste: R$", reajuste_salario(salario))