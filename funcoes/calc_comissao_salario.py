"""
Algoritmo que calcula o salário final de um funcionário com base no
salário inicial e no valor total de suas vendas. O programa calcula
uma comissão de 4% sobre as vendas e adiciona esse valor ao salário
inicial para obter e exibir o salário final.
"""

def comissao(v,taxa_comissao=4):
  calc_comissao = v * taxa_comissao / 100
  return calc_comissao
def salario_final(s,v):
  calc_salario_final = s + comissao(v)
  return calc_salario_final
salario_inicial = float(input("Digite o salário inicial: "))
valor_vendas = float(input("Digite o valor das vendas: "))
print("O salário final ficou em: R$", salario_final(salario_inicial, valor_vendas))