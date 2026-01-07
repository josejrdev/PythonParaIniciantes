l = [10,20,25,30]
busca = int(input("Digite o valor que deseja buscar: "))
def pesquisar(l,b):
    for i,v in enumerate(l):
        if v == b:
            return (f"Valor {b} achado na posição {i}")
    return (f"Valor {b} não achado na lista")
print(pesquisar(l,busca))