def comissao(v,taxa_comissao=4):
  calc_comissao = v * taxa_comissao / 100
  return calc_comissao
def salario_final(s,v):
  calc_salario_final = s + comissao(v)
  return calc_salario_final
salario_inicial = float(input("Digite o salário inicial: "))
valor_vendas = float(input("Digite o valor das vendas: "))
print("O salário final ficou em: R$", salario_final(salario_inicial, valor_vendas))