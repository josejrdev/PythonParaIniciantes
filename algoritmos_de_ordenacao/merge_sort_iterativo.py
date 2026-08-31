"""
Algoritmo de ordenação Merge Sort iterativo
"""

def merge(lista_e, lista_d):
    lista_f, index_e, index_d = [], 0, 0
    while index_e < len(lista_e) and index_d < len(lista_d):
        if lista_e[index_e] < lista_d[index_d]:
            lista_f.append(lista_e[index_e])
            index_e += 1
        else:
            lista_f.append(lista_d[index_d])
            index_d += 1
    if len(lista_e[index_e:]):
        lista_f.extend(lista_e[index_e:])
    elif len(lista_d[index_d:]):
        lista_f.extend(lista_d[index_d:])
    return lista_f

def merge_sort_iterativo(arr):
  # Inicializa o tamanho da sublista como 1
  tamanho_sublista = 1

  # Continua o loop enquanto o tamanho da sublista for menor que o tamanho da lista original
  while tamanho_sublista < len(arr):
    # Percorre a lista em passos de tamanho 2 * tamanho_sublista
    for inicio in range(0, len(arr), 2 * tamanho_sublista):
      # Calcula o ponto médio da sublista
      meio = inicio + tamanho_sublista

      # Calcula o ponto final da sublista (limitado pelo tamanho da lista original)
      fim = min(inicio + 2 * tamanho_sublista, len(arr))

      # Divide a sublista atual em duas partes: [inicio:meio] e [meio:fim]
      esquerda = arr[inicio:meio]
      direita = arr[meio:fim]

      # Chama a função intercalar para mesclar as sublistas ordenadas (esquerda e direita)
      # e armazenar o resultado de volta na lista original (arr)
      arr[inicio:fim] = merge(esquerda, direita)

    # Dobra o tamanho da sublista para a próxima iteração
    tamanho_sublista *= 2

  # Retorna a lista original ordenada
  return arr