"""
Programa que analisa uma lista de frequência de uma academia,
contabilizando o total de dias em que houve presença, representados
pela letra "S". Ao final, também utiliza o fatiamento da lista para
obter os registros correspondentes à metade final da frequência.
"""
listaFrequenciaAcademia = ["S", "N", "N", "S", "S", "N", "S"]
cont = 0
presencaTotal = 0
while cont < len(listaFrequenciaAcademia):
  if listaFrequenciaAcademia[cont] == "S":
    presencaTotal = presencaTotal + 1
  cont = cont + 1
metadeFinal = listaFrequenciaAcademia[3:]
print(f"Presença total: {presencaTotal} dias")
print(f"Métade final: {metadeFinal}")