l = [15,7,27,39]
p = int(input("Digite o primeiro valor a pesquisar: "))
v = int(input("Digite o segundo valor a pesquisar: "))
cont = 0
ativarP = False
ativarV = False
while cont < len(l):
    if l[cont] == p:
        statusP = f"Valor {p} encontrado na posição {cont}"
        ativarP = True
    if l[cont] == v:
        statusV = f"Valor {v} encontrado na posição {cont}"
        ativarV = True
    cont = cont + 1
if ativarP == True:
    print(statusP)
else:
    print(f"Valor {p} não foi encontrado.")
if ativarV == True:
    print(statusV)
else:
    print(f"Valor {v} não foi encontrado.")