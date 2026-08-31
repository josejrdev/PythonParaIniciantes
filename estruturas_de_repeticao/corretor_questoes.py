"""
Algoritmo que lê as respostas de 3 perguntas, verifica se cada resposta
corresponde à alternativa correta e contabiliza a quantidade de respostas
corretas, exibindo ao final a pontuação obtida.
"""

cont = 1
pontos = 0
while cont <= 3:
    resposta = input(f"Digite a resposta da {cont}° pergunta: ")
    if resposta.lower() == "b" and cont == 1:
        pontos = pontos + 1
    if resposta.lower() == "a" and cont == 2:
        pontos = pontos + 1
    if resposta.lower() == "d" and cont == 3:
        pontos = pontos + 1 # acumulador
    cont = cont + 1 # contador
print(f"{pontos} pontos.")