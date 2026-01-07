fila = list(range(1,11))
contFimDaFila = len(fila)
gerenciador = 1
while gerenciador > 0:
    print("Fila atual: ", fila)
    print("Digite A para atendimento de pessoas.")
    print("Digite F para adicionar pessoas ao fim da fila.")
    print("Digite S para sair.")
    opcao = input("Digite a opção desejada(A, F ou S): ")
    for letra in opcao:
        if letra.upper() == "S":
            gerenciador = 0
            break
        if letra.upper() == "A":
            if len(fila) > 0:
                pAtendida = fila.pop(0)
                print("Pessoa %d foi atendida." %pAtendida)
            else:
                print("Fila vazia, Não existem pessoas para atender.")
        elif letra.upper() == "F":
            contFimDaFila = contFimDaFila + 1
            fila.append(contFimDaFila)
            print("Pessoa %d adicionada ao fim da fila." %contFimDaFila)
        else:
            print("Opção inválida, digite apenas A, F ou S.")