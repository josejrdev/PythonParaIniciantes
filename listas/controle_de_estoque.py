"""
Programa que analisa as quantidades de produtos em estoque e cria uma
lista de controle. Para cada quantidade, verifica se há pelo menos
5 unidades disponíveis: caso haja, registra "OK"; caso contrário,
registra "REPOR". Ao final, exibe a lista de controle de estoque.
"""
listaEstoque = [12,3,0,7,2,15]
listaControleEstoque = []
for quantidade in listaEstoque:
    if quantidade >= 5:
        listaControleEstoque.append("OK")
    else:
        listaControleEstoque.append("REPOR")
print(f"Lista para controle de estoque: {listaControleEstoque}")