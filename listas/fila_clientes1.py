fila = list(range(1,11))
entrarfimDaFila = len(fila)
while True:
    print("Lista atual:", fila)
    print("Digite A para atender pessoas da fila.")
    print("Digite F para adicionar pessoas na fila.")
    print("Digite S para sair.")
    opcao = input("Digite a opção desejada(A, F ou S): ")
    if opcao.upper() == "S":
        break
    if opcao.upper() == "A":
        if len(fila) > 0:
            removido = fila.pop(0)
            print("Pessoa %d foi atendida." %removido)
        else:
            print("Fila vazia, não existem pessoas para atender.")
    elif opcao.upper() == "F":
        entrarfimDaFila = entrarfimDaFila + 1
        fila.append(entrarfimDaFila)
        print("Pessoa %d adicionada ao final da fila." %entrarfimDaFila)
    else:
        print("Opção inválida, digite apenas A, F ou S.")