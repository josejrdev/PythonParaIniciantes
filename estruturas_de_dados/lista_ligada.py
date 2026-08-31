"""
Algoritmo de lista ligada
"""

class ListaLigada:
    """
    Implementa uma lista simplesmente encadeada.
    """

    def __init__(self):
        """
        Inicializa a lista como vazia.
        """
        self.inicio = None
        self._tamanho = 0

    def limpar(self) -> None:
        """
        Remove todos os elementos da lista.
        """
        # Poderia iterar e quebrar as referências para ajudar o GC,
        # mas reatribuir inicio é suficiente em Python.
        self.inicio = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.
        """
        return self._tamanho == 0

    def no_em(self, posicao: int) -> No:
        """
        Retorna o nó da posição especificada.
        """
        if not 0 <= posicao < self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        no = self.inicio
        for _ in range(posicao):
            no = no.proximo
        return no

    def inserir_no_inicio(self, valor: any) -> None:
        """
        Insere um novo elemento no início da lista.
        """
        novo_no = No(valor)
        novo_no.proximo = self.inicio
        self.inicio = novo_no
        self._tamanho += 1

    def inserir_no_final(self, valor: any) -> None:
        """
        Insere um novo elemento no final da lista.
        """
        novo_no = No(valor)
        if self.esta_vazia():
            self.inicio = novo_no
        else:
            ultimo = self.no_em(self._tamanho - 1)
            ultimo.proximo = novo_no
        self._tamanho += 1

    def inserir_em(self, posicao: int, valor: any) -> None:
        """
        Insere um novo elemento em uma posição específica da lista.
        """
        if not 0 <= posicao <= self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        if posicao == 0:
            self.inserir_no_inicio(valor)
        else:
            anterior = self.no_em(posicao - 1)
            novo_no = No(valor)
            novo_no.proximo = anterior.proximo
            anterior.proximo = novo_no
            self._tamanho += 1

    def remover_do_inicio(self) -> any:
        """
        Remove e retorna o primeiro elemento da lista.
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        removido = self.inicio
        self.inicio = removido.proximo
        self._tamanho -= 1
        return removido.valor

    def remover_do_final(self) -> any:
        """
        Remove e retorna o último elemento da lista.
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        if self._tamanho == 1:
            return self.remover_do_inicio()

        penultimo = self.no_em(self._tamanho - 2)
        valor = penultimo.proximo.valor
        penultimo.proximo = None
        self._tamanho -= 1
        return valor

    def remover_em(self, posicao: int) -> any:
        """
        Remove e retorna o elemento da posição especificada.
        """
        if not 0 <= posicao < self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        if posicao == 0:
            return self.remover_do_inicio()

        anterior = self.no_em(posicao - 1)
        removido = anterior.proximo
        anterior.proximo = removido.proximo
        self._tamanho -= 1
        return removido.valor

    def posicao_de(self, valor: any) -> int:
        """
        Retorna o índice da primeira ocorrência do valor na lista, ou -1 se não encontrado.
        """
        atual = self.inicio
        pos = 0
        while atual:
            if atual.valor == valor:
                return pos
            atual = atual.proximo
            pos += 1
        return -1

    def __contains__(self, valor: any) -> bool:
        """
        Permite o uso de 'valor in lista'.
        """
        return self.posicao_de(valor) != -1

    def __len__(self) -> int:
        """
        Retorna o número de elementos da lista.
        """
        return self._tamanho

    def __getitem__(self, posicao: int) -> any:
        """
        Permite acessar o valor de um elemento usando colchetes (ex: lista[2]).
        """
        return self.no_em(posicao).valor

    def __setitem__(self, posicao: int, valor: any) -> None:
        """
        Permite modificar o valor de um elemento usando colchetes, como em lista[i] = novo_valor.
        """
        no = self.no_em(posicao)
        no.valor = valor

    def __iter__(self):
        """
        Permite iterar sobre os elementos da lista.
        """
        atual = self.inicio
        while atual:
            yield atual.valor
            atual = atual.proximo

    def __str__(self) -> str:
        """
        Retorna uma representação amigável da lista.
        """
        return " -> ".join(str(valor) for valor in self) + " -> None"

    def __repr__(self) -> str:
        """
        Retorna uma representação técnica da lista.
        """
        return f"ListaLigada(tamanho={self._tamanho})"