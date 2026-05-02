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
lista_um = [1,3,10,20,30,50,80]
lista_dois = [2,4,5,8,15,27,31,44,52]
print(merge(lista_um, lista_dois))