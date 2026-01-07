IngressosDisponiveis = [10,2,1,3,0]
while True:
    print("Ingressos Disponiveis:")
    for s, q in enumerate(IngressosDisponiveis):
        print("Sala %d - %d ingressos" %(s + 1, q))
    salaEscolhida = int(input("Digite a sala que deseja(0 sai): "))
    if salaEscolhida == 0:
        break
    if salaEscolhida < 0 or salaEscolhida > len(IngressosDisponiveis):
        print("Sala inválida, digite apenas: 1,2,3,4,5")
    elif IngressosDisponiveis[salaEscolhida - 1] == 0:
        print("A Sala %d está lotada" %salaEscolhida)
    else:
        qtdIngressos = int(input("Digite a quantidade de ingressos que deseja: "))
        if qtdIngressos < 0:
            print("Quantidade de ingressos inválida.")
        else:
            if qtdIngressos > IngressosDisponiveis[salaEscolhida - 1]:
                print("Não temos essa quantidade de ingressos na sala %d." %salaEscolhida)
            else:
                IngressosDisponiveis[salaEscolhida - 1] -= qtdIngressos
                print("%d ingressos comprados na sala %d" %(qtdIngressos, salaEscolhida))