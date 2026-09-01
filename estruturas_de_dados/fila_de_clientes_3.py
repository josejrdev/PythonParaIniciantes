"""
Programa que simula o gerenciamento de duas filas de atendimento.
O usuário pode atender pessoas da primeira ou da segunda fila,
adicionar novas pessoas ao final de cada fila ou encerrar o programa.
As opções A, B, F e G correspondem, respectivamente, ao atendimento
da primeira fila, atendimento da segunda fila, adição na primeira fila
e adição na segunda fila. O programa também verifica quando uma fila
está vazia e valida as opções informadas.
"""
filaUm = list(range(1,11))
filaDois = list(range(1,11))
contFinalFilaUm = len(filaUm)
contFinalFilaDois = len(filaDois)
gerenciador = 1
while gerenciador > 0:
    print("Primeira Fila:", filaUm)
    print("Segunda Fila:", filaDois)
    print("A(Primeira) e B(Segunda) realiza atendimento de pessoas.")
    print("F(Primeira) e G(Segunda) adiciona pessoas as filas.")
    print("S encerra o programa.")
    opcao = input("Digite a opção desejada(A, B, F, G ou S): ")
    for letra in opcao:
        if letra.upper() == "S":
            gerenciador = 0
            break
        if letra.upper() == "A":
            if len(filaUm) > 0:
                pessoaAtendidaFilaUm = filaUm.pop(0)
                print("A pessoa %d foi atendida na primeira fila." %pessoaAtendidaFilaUm)
            else:
                print("Primeira fila está vazia, não há pessoas para atender.")
        elif letra.upper() == "B":
            if len(filaDois) > 0:
                pessoaAtendidaFilaDois = filaDois.pop(0)
                print("A pessoa %d foi atendida na segunda fila." %pessoaAtendidaFilaDois)
            else:
                print("Segunda fila está vazia, não há pessoas para atender.")
        elif letra.upper() == "F":
            contFinalFilaUm = contFinalFilaUm + 1
            filaUm.append(contFinalFilaUm)
            print("Pessoa %d adicionada ao final da primeira fila." %contFinalFilaUm)
        elif letra.upper() == "G":
            contFinalFilaDois = contFinalFilaDois + 1
            filaDois.append(contFinalFilaDois)
            print("Pessoa %d foi adicionada ao final da segunda fila." %contFinalFilaDois)
        else:
            print("Opção inválida, digite apenas A, B, F, G ou S.")