def bubble_sort_nao_otimizado(l):
    n = len(l) # 9
    for i in range(n):
        for j in range(0, n - 1):
            if l[j] > l[j+1]: 
                l[j], l[j+1] = l[j+1], l[j]
lista = [54,26,93,17,77,31,44,55,20]
bubble_sort_nao_otimizado(lista)
print(lista)