def verificarPar(x):
    return x % 2 == 0
def parOuImpar(n):
    if verificarPar(n) == True:
        return (f"O Número {n} é par.")
    else:
        return (f"O Número {n} é impar.")
print(parOuImpar(3))