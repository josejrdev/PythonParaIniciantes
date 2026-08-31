""" 
Algoritmo que calcula quantos salários minimos 
existem no salário de um funcionário
"""

# Coleta o valor do salário minimo
salario_minimo = float(input("Qual o salário minimo? "))

# Coleta o valor do salario do funcionario
salario_funcionario = float(input("Qual o salário do funcionário? "))

# Calcula quantos salários minimos existem
calc = salario_funcionario / salario_minimo

#Exibe a saida
print("%d" %calc)