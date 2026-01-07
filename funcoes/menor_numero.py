def menorN (a,b):
    if a < b:
        return (f"O Número {a} é menor que o número {b}")
    elif a == b:
        return (f"Os Números {a} e {b} são iguais.")
    else:
        return (f"O Número {b} é menor que o número {a}")
print(menorN(5,1))