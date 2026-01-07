def validador(pergunta,minimo,maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v
validador("Digite um valor válido entre 0 e 5: ",0,5)