# Algoritmo que informa se o ano atual é bissexto ou não

# Coleta o ano atual do usuário
ano_atual = int(input("Digite o ano atual: "))

# Par if/else que informa se o ano é bissexto ou não é bissexto
if ano_atual % 4 == 0:
    print(f"{ano_atual} é bissexto.")
else:
    print(f"{ano_atual} não é bissexto.")