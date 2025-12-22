listaEstoque = [12,3,0,7,2,15]
listaControleEstoque = []
for quantidade in listaEstoque:
    if quantidade >= 5:
        listaControleEstoque.append("OK")
    else:
        listaControleEstoque.append("REPOR")
print(f"Lista para controle de estoque: {listaControleEstoque}")