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