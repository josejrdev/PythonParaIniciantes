def bubble_sort_otimizado(l):
    n = len(l)
    for i in range(n):
        trocou = False
        for j in range(0, n - 1 - i): # Últimos i elementos já estão ordenados, não precisam ser comparados
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                trocou = True
        if trocou == False:
            break
lista = [0,1,2,3,6,8]
bubble_sort_otimizado(lista)
print(lista)