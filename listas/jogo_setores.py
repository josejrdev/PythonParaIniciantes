listaRecursos = [40,20,10,50,60,15,5,30]
primeiroSetor = listaRecursos[::2]
segundoSetor = listaRecursos[1::2]
somaPrimeiroSetor = sum(primeiroSetor)
somaSegundoSetor = sum(segundoSetor)
if somaPrimeiroSetor > somaSegundoSetor:
    print("A soma do primeiro setor é maior")
elif somaPrimeiroSetor == somaSegundoSetor:
    print("As somas dos dois setores são iguais")
else:
    print("A soma do segundo setor é maior")