"""
Programa que define funções para calcular a soma e a média aritmética
dos valores de uma lista. A função somar() percorre todos os elementos
da lista e retorna a soma, enquanto a função media() utiliza essa soma
e a quantidade de elementos da lista para calcular a média.
"""

lista1 = [10,20,30,40,50]
lista2 = [10,10,10]

def somar(l):
    calc = 0
    for v in l:
        calc = calc + v
    return calc
def media(l):
    return somar(l) / len(l)

print(media(lista1))
print(media(lista2))