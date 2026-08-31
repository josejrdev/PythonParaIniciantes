"""
Algoritmo de lista circular
"""

class ListaCircularDupla:
    """
    Implementa uma lista duplamente ligada circular com sentinela.
    """

    def __init__(self):
        """
        Inicializa a lista como vazia.
        """
        self.sentinela = NoCircular(None)  # Nó sentinela, sem valor
        self._tamanho = 0

    def limpar(self) -> None:
        """
        Remove todos os elementos da lista.
        """
        self.sentinela.proximo = self.sentinela
        self.sentinela.anterior = self.sentinela
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.
        """
        return self._tamanho == 0

    def _no_em(self, posicao: int) -> NoCircular:
        """
        Retorna o nó da posição especificada, utilizando busca circular eficiente.
        (Método interno)
        """
        if not 0 <= posicao < self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        no = self.sentinela.proximo
        if posicao < self._tamanho // 2:
            for _ in range(posicao):
                no = no.proximo
        else:
            no = self.sentinela
            for _ in range(self._tamanho - posicao):
                no = no.anterior
        return no

    def inserir_no_inicio(self, valor: any) -> None:
        """
        Insere um novo elemento no início da lista. O(1)
        """
        novo_no = NoCircular(valor)
        if self.esta_vazia():
            self.sentinela.proximo = novo_no
            self.sentinela.anterior = novo_no
            novo_no.proximo = self.sentinela
            novo_no.anterior = self.sentinela
        else:
            primeiro = self.sentinela.proximo
            self.sentinela.proximo = novo_no
            novo_no.proximo = primeiro
            novo_no.anterior = self.sentinela
            primeiro.anterior = novo_no
        self._tamanho += 1

    def inserir_no_final(self, valor: any) -> None:
        """
        Insere um novo elemento no final da lista. O(1)
        """
        if self.esta_vazia():
            self.inserir_no_inicio(valor)
        else:
            novo_no = NoCircular(valor)
            ultimo = self.sentinela.anterior
            ultimo.proximo = novo_no
            novo_no.anterior = ultimo
            novo_no.proximo = self.sentinela
            self.sentinela.anterior = novo_no
        self._tamanho += 1

    def remover_do_inicio(self) -> any:
        """
        Remove e retorna o primeiro elemento da lista. O(1)
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        primeiro = self.sentinela.proximo
        valor_removido = primeiro.valor
        if self._tamanho == 1:
            self.sentinela.proximo = self.sentinela
            self.sentinela.anterior = self.sentinela
        else:
            self.sentinela.proximo = primeiro.proximo
            primeiro.proximo.anterior = self.sentinela
        self._tamanho -= 1
        return valor_removido

    def remover_do_final(self) -> any:
        """
        Remove e retorna o último elemento da lista. O(1)
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        ultimo = self.sentinela.anterior
        valor_removido = ultimo.valor
        if self._tamanho == 1:
            self.sentinela.proximo = self.sentinela
            self.sentinela.anterior = self.sentinela
        else:
            self.sentinela.anterior = ultimo.anterior
            ultimo.anterior.proximo = self.sentinela
        self._tamanho -= 1
        return valor_removido

    def __len__(self) -> int:
        """
        Retorna o número de elementos da lista.
        """
        return self._tamanho

    def __iter__(self):
        """
        Permite iteração direta sobre a lista com `for`.
        """
        atual = self.sentinela.proximo
        for _ in range(self._tamanho):
            yield atual.valor
            atual = atual.proximo

    def __getitem__(self, posicao: int) -> any:
        """
        Permite acesso por índice, como em listas comuns.
        """
        return self._no_em(posicao).valor

    def __contains__(self, valor: any) -> bool:
        """
        Verifica se um valor está presente na lista.
        """
        return any(elemento == valor for elemento in self)

    def __repr__(self) -> str:
        """
        Representação textual da lista.
        """
        elementos = [str(valor) for valor in self]
        return " <-> ".join(elementos) + " (circular)"