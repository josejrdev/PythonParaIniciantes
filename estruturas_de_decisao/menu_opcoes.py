while True:
    print("Menu " + "-" * 51)
    print("Digite 1 para exibir o número cinco, dez vezes.")
    print("Digite 2 para exibir o número cinco, vinte e nove vezes.")
    print("Digite 3 para exibir o número quarenta, oitenta vezes.")
    print("Digite 4 para sair do programa.")
    opcao = int(input("Digite a opção desejada: "))
    if opcao == 1:
        for v in range(1,11):
            print(f"{v}° vez = 5")
    elif opcao == 2:
        for v in range(1,30):
            print(f"{v}° vez = 5")
    elif opcao == 3:
        for v in range(1,81):
            print(f"{v}° vez = 40")
    elif opcao == 4:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida, opções válidas: (1,2,3 ou 4).")