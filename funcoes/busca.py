"""
Programa que pesquisa um valor informado pelo usuário dentro de uma
lista. A função pesquisar() percorre a lista utilizando enumerate()
para verificar cada elemento e, caso encontre o valor buscado, informa
sua posição. Se o valor não for encontrado, informa que ele não está
presente na lista.
"""
l = [10,20,25,30]
busca = int(input("Digite o valor que deseja buscar: "))
def pesquisar(l,b):
    for i,v in enumerate(l):
        if v == b:
            return (f"Valor {b} achado na posição {i}")
    return (f"Valor {b} não achado na lista")
print(pesquisar(l,busca))