# Programa que calcula salário de um funcionário com acréscimo de porcentagem do total de vendas ao salário final
# Coletando Salário fixo
SalarioFixo = float(input("Salário fixo: "))
# Coletando total de vendas
TotalVendas = int(input("Total de vendas: "))
# Coletando porcentagem da comissão
PorcentagemComissao = int(input("Porcentagem da Comissão: "))

# Descobrindo qual é o valor da %
CalculoPorcentagem = (PorcentagemComissao / 100) * TotalVendas

# Somando com o salário fixo para saber salário final
CalculoSalario = SalarioFixo + CalculoPorcentagem

# Exibindo
print("Salário Fixo: " + str(SalarioFixo) + " Total de vendas: " + str(TotalVendas) + " Comissão: " + str(CalculoPorcentagem) + " Salário final: " + str(CalculoSalario))