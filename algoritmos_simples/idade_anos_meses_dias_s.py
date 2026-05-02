anoNascimento = int(input("Digite o ano de nascimento: "))
anoAtual = int(input("Digite o ano atual: "))
calcAnos = anoAtual - anoNascimento
calcMeses = calcAnos * 12
calcDias = calcMeses * 30
calcSemanas = calcDias // 7
print(f"Anos: {calcAnos}, Meses: {calcMeses}, Dias: {calcDias}, Semanas: {calcSemanas}")