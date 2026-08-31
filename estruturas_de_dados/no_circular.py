class NoCircular:
    """
    Representa um único nó em uma lista duplamente ligada circular.
    """
    def __init__(self, valor):
        """
        Inicializa um novo nó circular.

        Parâmetros:
            valor: Dado a ser armazenado no nó.
        """
        self.valor = valor          # Valor armazenado no nó
        self.proximo = self         # Aponta inicialmente para si mesmo
        self.anterior = self        # Aponta inicialmente para si mesmo

    def __repr__(self):
        """
        Representação textual do nó circular.
        """
        return f"NoCircular({self.valor})"

# Criando quatro nós
n1 = NoCircular("A")
n2 = NoCircular("B")
n3 = NoCircular("C")
n4 = NoCircular("D")

# Encadeando para frente
n1.proximo = n2
n2.proximo = n3
n3.proximo = n4
n4.proximo = n1  # Fecha o ciclo: último aponta para o primeiro

# Encadeando para trás
n2.anterior = n1
n3.anterior = n2
n4.anterior = n3
n1.anterior = n4  # Fecha o ciclo: primeiro aponta para o último

# Navegação para frente
print(n4)                                  # NoDuplo(D)
print(n4.proximo)                          # NoDuplo(A)
print(n4.proximo.proximo)                  # NoDuplo(B)
print(n4.proximo.proximo.proximo)          # NoDuplo(C)
print(n4.proximo.proximo.proximo.proximo)  # NoDuplo(D)

# Navegação para trás
print(n1)                                     # NoDuplo(A)
print(n1.anterior)                            # NoDuplo(D)
print(n1.anterior.anterior)                   # NoDuplo(C)
print(n1.anterior.anterior.anterior)          # NoDuplo(B)
print(n1.anterior.anterior.anterior.anterior) # NoDuplo(A)