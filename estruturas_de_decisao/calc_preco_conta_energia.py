""" 
Algoritmo que calcula o preço total de uma conta de energia
de acordo com o tipo de instação do usuário
"""

# Coleta o consumo em kwn
consumoKwh = float(input("Digite a quantidade de Kwn consumida: "))

# Coleta o tipo de instalação
tipoInstalacao = input("Digite o tipo de instalação: ")

# estrutura de if / elif / else que calcula o preço da conta de acordo com o tipo de instalação 
if tipoInstalacao.lower() == "r":
    if consumoKwh <= 500:
        calcPreco = consumoKwh * 0.40
    else:
        calcPreco = consumoKwh * 0.65
    print("Preço a pagar R$%.2f" %calcPreco)
elif tipoInstalacao.lower() == "c":
    if consumoKwh <= 1000:
        calcPreco = consumoKwh * 0.55
    else:
        calcPreco = consumoKwh * 0.60
    print("Preço a pagar R$%.2f" %calcPreco)
elif tipoInstalacao.lower() == "i":
    if consumoKwh <= 5000:
        calcPreco = consumoKwh * 0.55
    else:
        calcPreco = consumoKwh * 0.60
    print("Preço a pagar R$%.2f" %calcPreco)
else:
    print("Tipo de instação inválido.")