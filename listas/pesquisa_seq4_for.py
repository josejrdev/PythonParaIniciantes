lista = [1,2,3,4,5]
pesquisa = int(input("Digite o primeiro item a pesquisar: "))
cont = 0
for valor in lista:
    if valor == pesquisa:
        print("Valor %d foi encontrado, na posição %d" %(pesquisa, cont))
        break
    cont = cont + 1
else:
    print("Valor %d não achado" %pesquisa)