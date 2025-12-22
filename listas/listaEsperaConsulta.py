listaEsperaConsulta = ["Carlos", "Ana", "Bruno", "Elisa", "Patricia", "João"]
nomeBusca = input("Digite o nome a buscar: ")
for i in range(4):
    if nomeBusca == listaEsperaConsulta[i]:
        print(f"O nome {nomeBusca} está entre os 3 primeiros da lista")
        break