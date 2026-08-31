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