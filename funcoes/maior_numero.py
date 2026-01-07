def maiorNumero (a,b):
    if a > b:
        return (f"{a} é maior.")
    elif a == b:
        return (f"{a} e {b} são iguais.")
    else:
        return (f"{b} é maior")
print(maiorNumero(7,7))