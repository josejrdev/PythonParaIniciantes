"""
Função que solicita um valor inteiro ao usuário e verifica se ele
está dentro de um intervalo mínimo e máximo informado. Enquanto
o valor estiver fora do intervalo, solicita uma nova entrada.
Quando um valor válido é informado, a função o retorna.
"""
def validador(pergunta,minimo,maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print(f"Valor inválido. Digite um valor entre {minimo} e {maximo}")
        else:
            return v
validador("Digite um valor válido entre 0 e 5: ",0,5)