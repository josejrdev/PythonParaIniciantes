listaPrecos = [1500,700,200,2500,600,300]
listaValoresMenor800 = []
for precos in listaPrecos:
    if precos < 800:
        listaValoresMenor800.append(precos)
print(f"Os valores menores que 800 são: {listaValoresMenor800}")