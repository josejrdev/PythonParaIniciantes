"""
 Algoritmo que calcula a conta de um chip de 
 celular de acordo com os minutos que foram falados.
"""

# Coleta do usuário os minutos falados
minutos_falados = int(input("Digite os minutos falados: "))

if minutos_falados <= 200:
    calc_conta = minutos_falados * 0.20
elif minutos_falados > 200 and minutos_falados <= 400:
    calc_conta = minutos_falados * 0.18
else:
    calc_conta = minutos_falados * 0.15
print("A conta deu: R$%.2f" %calc_conta)