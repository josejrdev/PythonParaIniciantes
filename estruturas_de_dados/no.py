"""
Algoritmo de construção de Nó
"""

class No:
    """
    Representa um único nó em uma lista simplesmente encadeada.
    """
    def __init__(self, valor):
        """
        Inicializa um novo nó.

        Parâmetros:
            valor: Dado a ser armazenado no nó.
        """
        self.valor = valor        # Valor armazenado no nó
        self.proximo = None       # Referência para o próximo nó (inicialmente nula)

    def __repr__(self):
        """
        Representação textual do nó.
        """
        return f"No({self.valor})"

    def __eq__(self, outro):
        """
        Compara dois nós com base no valor armazenado.
        """
        if isinstance(outro, No):
            return self.valor == outro.valor
        return False

# Criando três nós
n1 = No("A")
n2 = No("B")
n3 = No("C")

# Encadeando manualmente
n1.proximo = n2
n2.proximo = n3

print(n1)                  # No(A)
print(n1.proximo)          # No(B)
print(n1.proximo.proximo)  # No(C)
print(n1.proximo.proximo.proximo)  # None (fim da lista)