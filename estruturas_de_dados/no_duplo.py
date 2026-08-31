"""
Algoritmo de construção de Nó Duplo
"""

class NoDuplo:
    """
    Representa um único nó em uma lista duplamente encadeada.
    """
    def __init__(self, valor):
        """
        Inicializa um novo nó duplo.

        Parâmetros:
            valor: Dado a ser armazenado no nó.
        """
        self.valor = valor      # Valor armazenado no nó
        self.proximo = None     # Referência para o próximo nó (inicialmente nula)
        self.anterior = None    # Referência para o nó anterior (inicialmente nula)

    def __repr__(self):
        """
        Representação textual do nó duplo.
        """
        return f"NoDuplo({self.valor})"

# Criando três nós duplos
n1 = NoDuplo("A")
n2 = NoDuplo("B")
n3 = NoDuplo("C")

# Encadeando manualmente (frente)
n1.proximo = n2
n2.proximo = n3

# Encadeando manualmente (trás)
n2.anterior = n1
n3.anterior = n2

print(n1)                 # NoDuplo(A)
print(n1.proximo)         # NoDuplo(B)
print(n1.proximo.proximo) # NoDuplo(C)

print(n3)                 # NoDuplo(C)
print(n3.anterior)        # NoDuplo(B)
print(n3.anterior.anterior) # NoDuplo(A)

print(n1.anterior)        # None (início da lista)
print(n3.proximo)         # None (fim da lista)