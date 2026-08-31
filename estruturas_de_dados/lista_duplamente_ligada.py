"""
Algoritmo de Lista duplamente ligada
"""

class ListaDuplamenteLigada:
    """
    Implementa uma lista duplamente encadeada.
    """

    def __init__(self):
        """
        Inicializa a lista como vazia.
        """
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def limpar(self) -> None:
        """
        Remove todos os elementos da lista.
        """
        # Poderia iterar e quebrar as referências para ajudar o GC,
        # mas reatribuir inicio/fim é suficiente em Python.
        self.inicio = None
        self.fim = None
        self._tamanho = 0

    def esta_vazia(self) -> bool:
        """
        Verifica se a lista está vazia.
        """
        return self._tamanho == 0

    def _no_em(self, posicao: int) -> NoDuplo:
        """
        Retorna o nó da posição especificada. Otimizado para buscar
        a partir do início ou do fim, dependendo da posição. (Método interno)
        """
        if not 0 <= posicao < self._tamanho:
            raise IndexError("Índice fora do intervalo.")

        # Otimização: buscar do início ou do fim?
        if posicao < self._tamanho // 2:
            # Busca a partir do início
            no = self.inicio
            for _ in range(posicao):
                no = no.proximo
        else:
            # Busca a partir do fim (mais rápido para índices altos)
            no = self.fim
            for _ in range(self._tamanho - 1, posicao, -1):
                no = no.anterior
        return no

    def inserir_no_inicio(self, valor: any) -> None:
        """
        Insere um novo elemento no início da lista. O(1)
        """
        novo_no = NoDuplo(valor)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.proximo = self.inicio
            self.inicio.anterior = novo_no
            self.inicio = novo_no
        self._tamanho += 1

    def inserir_no_final(self, valor: any) -> None:
        """
        Insere um novo elemento no final da lista. O(1)
        """
        novo_no = NoDuplo(valor)
        if self.esta_vazia():
            self.inicio = novo_no
            self.fim = novo_no
        else:
            novo_no.anterior = self.fim
            self.fim.proximo = novo_no
            self.fim = novo_no
        self._tamanho += 1

    def inserir_em(self, posicao: int, valor: any) -> None:
        """
        Insere um novo elemento em uma posição específica da lista. O(n)
        """
        if not 0 <= posicao <= self._tamanho:
             raise IndexError("Índice fora do intervalo para inserção.")

        if posicao == 0:
            self.inserir_no_inicio(valor)
        elif posicao == self._tamanho:
            self.inserir_no_final(valor)
        else:
            # Encontra o nó que *estará* após o novo nó
            no_atual = self._no_em(posicao)
            no_anterior = no_atual.anterior
            novo_no = NoDuplo(valor)

            # Liga novo_no com anterior
            novo_no.anterior = no_anterior
            no_anterior.proximo = novo_no

            # Liga novo_no com atual
            novo_no.proximo = no_atual
            no_atual.anterior = novo_no

            self._tamanho += 1

    def remover_do_inicio(self) -> any:
        """
        Remove e retorna o primeiro elemento da lista. O(1)
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        valor_removido = self.inicio.valor
        if self._tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.inicio = self.inicio.proximo
            self.inicio.anterior = None # Nova cabeça não tem anterior

        self._tamanho -= 1
        return valor_removido

    def remover_do_final(self) -> any:
        """
        Remove e retorna o último elemento da lista. O(1)
        """
        if self.esta_vazia():
            raise IndexError("A lista está vazia.")

        valor_removido = self.fim.valor
        if self._tamanho == 1:
            self.inicio = None
            self.fim = None
        else:
            self.fim = self.fim.anterior
            self.fim.proximo = None # Nova cauda não tem próximo

        self._tamanho -= 1
        return valor_removido

    def remover_em(self, posicao: int) -> any:
        """
        Remove e retorna o elemento da posição especificada. O(n)
        """
        if not 0 <= posicao < self._tamanho:
            raise IndexError("Índice fora do intervalo para remoção.")

        if posicao == 0:
            return self.remover_do_inicio()
        if posicao == self._tamanho - 1:
            return self.remover_do_final()

        # Nó a ser removido
        no_removido = self._no_em(posicao)
        no_anterior = no_removido.anterior
        no_proximo = no_removido.proximo

        # Refaz as ligações
        no_anterior.proximo = no_proximo
        no_proximo.anterior = no_anterior

        self._tamanho -= 1
        return no_removido.valor

    def posicao_de(self, valor: any) -> int:
        """
        Retorna o índice da primeira ocorrência do valor na lista,
        ou -1 se não encontrado. O(n)
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
        """ Permite o uso de 'valor in lista'. O(n) """
        return self.posicao_de(valor) != -1

    def __len__(self) -> int:
        """ Retorna o número de elementos da lista. O(1) """
        return self._tamanho

    def __getitem__(self, posicao: int) -> any:
        """ Permite acessar o valor via lista[i]. O(n) """
        no = self._no_em(posicao)
        return no.valor

    def __setitem__(self, posicao: int, valor: any) -> None:
        """ Permite modificar o valor via lista[i] = valor. O(n) """
        no = self._no_em(posicao)
        no.valor = valor

    def __iter__(self):
        """ Permite iterar sobre os valores (início ao fim). O(n) """
        atual = self.inicio
        while atual:
            yield atual.valor
            atual = atual.proximo

    def __str__(self) -> str:
        """ Retorna uma representação amigável da lista. O(n) """
        if self.esta_vazia():
            return "None <- [] -> None"
        valores = " <-> ".join(str(valor) for valor in self)
        return f"None <- {valores} -> None"

    def __repr__(self) -> str:
        """ Retorna uma representação técnica da lista. O(1) """
        return f"ListaDuplamenteLigada(tamanho={self._tamanho})"