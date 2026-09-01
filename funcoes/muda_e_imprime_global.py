"""
Programa que demonstra o uso da palavra-chave global para alterar
o valor de uma variável definida fora da função. A função
muda_e_imprime() modifica a variável global "a" de 5 para 7 e
exibe seu valor antes e depois da alteração.
"""

a = 5

def muda_e_imprime():
    global a
    a = 7
    print("A dentro da função: %d" %a)

print("A antes de mudar: %d" %a)

muda_e_imprime()

print("A depois de mudar: %d" %a)