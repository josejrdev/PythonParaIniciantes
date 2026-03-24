def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_index = i
        for j in range(i+1,n):
            if l[j] < l[min_index]:
                min_index = j
        l[i], l[min_index] = l[min_index], l[i]
lista = [5,3,8,4,2]
selection_sort(lista)
print(lista)
#Selection sort tem complexidade O(n)2
#4 Seleções para ordenar a lista.
#Não é eficiente para listas grandes, por conta da complexidade O(n)2
#Se a lista tivesse quase ordenada ele entraria poucas vezes no if para
#alterar o valor de min index. porém, faria a mesma quantidade de iterações
#para tentar achar os min index