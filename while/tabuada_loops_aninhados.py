print("." * 10 + "OPÇÕES" + "." * 10)
print("." * 10 + "ADIÇÃO: A" + "." * 10)
print("." * 10 + "SUBTRAÇÃO: S" + "." * 10)
print("." * 10 + "MULTIPLICAÇÃO: M" + "." * 10)
print("." * 10 + "FIM: F" + "." * 10)
numeroTab = 1
while True:
    opcaoEscolhida = input("Digite a opção Escolhida: ")
    if opcaoEscolhida.upper() == "A":
        tabuada = 1
        while tabuada <= 10:
            print(f"Tabuada do número: {tabuada}")
            while numeroTab <= 10:
                resultado = tabuada + numeroTab
                print(f"{tabuada} + {numeroTab} = {resultado}")
                numeroTab = numeroTab + 1
            numeroTab = 1
            tabuada = tabuada + 1 
    elif opcaoEscolhida.upper() == "S":
        tabuada = 1
        while tabuada <= 10:
            print(f"Tabuada do número: {tabuada}")
            while numeroTab <= 10:
                resultado = tabuada - numeroTab
                print(f"{tabuada} - {numeroTab} = {resultado}")
                numeroTab = numeroTab + 1
            numeroTab = 1
            tabuada = tabuada + 1 
    elif opcaoEscolhida.upper() == "M":
        tabuada = 1
        while tabuada <= 10:
            print(f"Tabuada do número: {tabuada}")
            while numeroTab <= 10:
                resultado = tabuada * numeroTab
                print(f"{tabuada} x {numeroTab} = {resultado}")
                numeroTab = numeroTab + 1
            numeroTab = 1
            tabuada = tabuada + 1 
    elif opcaoEscolhida.upper() == "F":
        print("fim do programa")
        break
    else:
        print("Digite uma opção válida")