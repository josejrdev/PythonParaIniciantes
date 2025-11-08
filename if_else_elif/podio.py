# programa que exibe o prêmio de um atleta a partir de sua posição em uma corrida
posicao = int(input("Digite a posição do atleta: "))
premio = None
if (posicao <= 3):
    if (posicao == 3):
        premio = "Terceiro Lugar, Prêmio: 5 Mil Reais"
    if (posicao == 2):
        premio = "Segundo Lugar, Prêmio: 8 Mil Reais"
    if (posicao == 1):
        premio = "Primeiro Lugar! Prêmio: Um carro 0KM"
if (posicao <= 6):
    if (posicao == 6):
        premio = "Sexto lugar, foi bem."
    if (posicao == 5):
        premio = "Quinto lugar, uma ótima posição."
    if (posicao == 4):
        premio = "Quarto lugar, foi muito bem."
if (posicao > 6):
    premio = "Ficou na " + str(posicao) + " posição."
else:
    print("Digite uma posição válida.")
print(premio)