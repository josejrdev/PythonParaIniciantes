lista = []
while True:
    print(f"Lista atual: {lista}")
    print("Menu de opções " + "-" * 10)
    print("A Adicionar item a lista.")
    print("R Remover item da lista.")
    print("Q Sair do programa.")
    opcao = input("Digite a opção desejada: ")
    if opcao.upper() == "A":
        print("Que tipo de item deseja adicionar? ")
        print("F: Float, I: Int, S: String")
        opcao_add = input("Digite a opção desejada: ")
        if opcao_add.upper() == "F":
            numero = float(input("Digite o número para adicionar: "))
            lista.append(numero)
        elif opcao_add.upper() == "I":
            numero = int(input("Digite o número para adicionar: "))
            lista.append(numero)
        elif opcao_add.upper() == "S":
            palavra = input("Digite a string para adicionar: ")
            lista.append(palavra)
        else:
            print("Opção inválida, opções: F,I ou S.")
    elif opcao.upper() == "R":
        print("Que tipo de item deseja remover? ")
        print("F: Float, I: Int, S: String")
        opcao_remover = input("Digite a opção desejada: ")
        if opcao_remover.upper() == "F":
            print(f"Lista atual: {lista}")
            numero = float(input("Digite o número para remover: "))
            for v in lista:
                if numero == v:
                    lista.remove(numero)
                    break
            else:
                print(f"{numero} não encontrado.")
        elif opcao_remover.upper() == "I":
            print(f"Lista atual: {lista}")
            numero = int(input("Digite o número para remover: "))
            for v in lista:
                if numero == v:
                    lista.remove(numero)
                    break
            else:
                print(f"{numero} não encontrado.")
        elif opcao_remover.upper() == "S":
            print(f"Lista atual: {lista}")
            palavra = input("Digite a string para remover: ")
            for v in lista:
                if palavra == v:
                    lista.remove(palavra)
                    break
            else:
                print(f"{palavra} não encontrado.")
        else:
            print("Opção inválida, opções: F,I ou S.")
    elif opcao.upper() == "Q":
        break