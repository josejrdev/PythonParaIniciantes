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