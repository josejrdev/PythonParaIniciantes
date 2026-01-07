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