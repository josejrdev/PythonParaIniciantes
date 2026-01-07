l = [15,7,27,39]
p = int(input("Digite o valor a pesquisar: "))
cont = 0
achou = False
while cont < len(l):
    if l[cont] == p:
        achou = True
        break
    cont = cont + 1
if achou:
    print("Elemento %d achado na posição %d" % (p,cont))
else:
    print("Elemento não encontrado")