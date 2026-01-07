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