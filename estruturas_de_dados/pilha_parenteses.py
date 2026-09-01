"""
Programa que verifica se uma expressão possui os parênteses
balanceados. O código percorre cada caractere da expressão,
incrementando o contador ao encontrar "(" e decrementando ao
encontrar ")". Caso um parêntese de fechamento apareça sem um
correspondente de abertura ou sobrem parênteses de abertura ao final,
a expressão é considerada inválida.
"""
expressao = input("Digite a expressão: ")
contador = 0
erro = False
for c in expressao:
    if c == '(':
        contador += 1
    elif c == ')':
        contador -= 1
        if contador < 0:
            erro = True
            break
if erro or contador != 0:
    print("Erro")
else:
    print("OK")