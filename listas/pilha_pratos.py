pilha = list(range(1,21))
contTopoPilha = len(pilha)
while True:
    print("Pilha atual:", pilha)
    print("Digite A para desimpilhar prato na pilha.")
    print("Digite F para empilhar prato na pilha.")
    print("Digite S para sair.")
    opcao = input("Digite a opção desejada(A, F ou S): ")
    if opcao.upper() == "S":
        break
    if opcao.upper() == "A":
        if len(pilha) > 0:
            pratoDesimpilhado = pilha.pop(-1)
            print("Prato %d desimpilhado da pilha." %pratoDesimpilhado)
        else:
            print("Pilha vazia, não existem pratos para desimpilhar.")
    elif opcao.upper() == "F":
        contTopoPilha = contTopoPilha + 1
        pilha.append(contTopoPilha)
        print("Prato %d empilhado na pilha." %contTopoPilha)
    else:
        print("Opção inválida, digite apenas A, F ou S.")