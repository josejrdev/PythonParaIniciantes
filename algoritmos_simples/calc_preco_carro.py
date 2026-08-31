# Pograma que calcula o preço de um carro, acrescentando 28% de comissão para o distribuior e 45% de impostos
# Preço de fábrica
PFA = float(input("Preço de fábrica: "))
# Porcentagem do distribuidor
POD = 28
# Porcentagem dos impostos
POI = 45
# Calculando a porcentagem
CalcPOD = (POD / 100) * PFA
CalcPOI = (POI / 100) * PFA 

# Calculando o preço final
PFI = CalcPOD + CalcPOI + PFA

print("Preço de fábrica: R$" + str(PFA) + " Preço com porcentagem do distribuidor e impostos: R$" + str(PFI)) 