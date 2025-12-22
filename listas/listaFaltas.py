listaFaltas = [0,2,1,3,0,1,4]
somaQtdFaltas = 0
qtdDiasMaisDeDuasFaltas = 0
for qtdFaltas in listaFaltas:
    somaQtdFaltas = somaQtdFaltas + qtdFaltas
    if qtdFaltas > 2:
        qtdDiasMaisDeDuasFaltas = qtdDiasMaisDeDuasFaltas + 1
qtdFaltasTresPrimeirosDias = sum(listaFaltas[0:3])
print(f"Quantidade de faltas: {somaQtdFaltas}")
print(f"Quantidade de faltas dos três primeiros dias: {qtdFaltasTresPrimeirosDias}")
print(f"Quantidade de dias com mais de duas faltas: {qtdDiasMaisDeDuasFaltas}")