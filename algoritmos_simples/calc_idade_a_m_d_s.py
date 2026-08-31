""" 
Algoritmo que coleta o ano de nascimento do usuário e o ano atual 
para calcular a idade em anos, calcular o total de meses de vida, 
o total de dias de vida e o total de semanas de vidas
"""

# Coleta o ano de nascimento
anoNascimento = int(input("Digite o ano de nascimento: "))

# Coleta o ano atual
anoAtual = int(input("Digite o ano atual: "))

# Calcula a idade em anos
calcAnos = anoAtual - anoNascimento

# Calcula o total de meses de vida
calcMeses = calcAnos * 12

# Calcula o total de dias de vida
calcDias = calcMeses * 30

# Calcula o total de semanas de vida
calcSemanas = calcDias // 7

# Exibe os resultados
print(f"Anos: {calcAnos}, Meses: {calcMeses}, Dias: {calcDias}, Semanas: {calcSemanas}")