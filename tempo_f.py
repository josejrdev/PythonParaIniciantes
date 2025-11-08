# cigarros por dia, anos. ex: 30 * 366 * qtdanos
# ele perde 10 minutos a cada cigarro
# calcula qts dias de vida ele perderá.
# 1 dia tem 60 * 24 minutos por dia.
qtdCigarros = int(input("Quantos cigarros fumados por dia? ")) 
qtdAnos = int(input("Quantos anos fumando? "))
calculoCD = (qtdAnos * 366) * qtdCigarros # calculo cigarro nos dias informados pelo usuário
calculoMinutos = calculoCD * 10 # qts de minutos perdidos naqueles dias
calculoDias = calculoMinutos / (24 * 60) # encaixar os minutos calculados em dias.
print("O fumante perderá %d dias de vida." %calculoDias)