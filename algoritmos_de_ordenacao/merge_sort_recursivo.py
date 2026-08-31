""" 
Algoritmo de ordenação Merge Sort recursivo
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

def merge_sort_recursivo(arr):
  # Obtém o tamanho da lista
  n = len(arr)

  # Caso base: se a lista tiver 1 ou 0 elementos, ela já está ordenada
  if n <= 1:
    return arr

  # Dividir a lista ao meio
  meio = n // 2
  metade_esquerda = arr[:meio]  # Metade esquerda da lista
  metade_direita = arr[meio:] # Metade direita da lista

  # Ordenar recursivamente as duas metades
  metade_esquerda = merge_sort_recursivo(metade_esquerda)
  metade_direita = merge_sort_recursivo(metade_direita)

  # Combinar as duas metades ordenadas
  return merge(metade_esquerda, metade_direita)  # Retorna a lista ordenada