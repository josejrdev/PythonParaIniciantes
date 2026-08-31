somaSalariosPalmares = 0
somaSalariosCaruaru = 0
somaSalariosRecife = 0
qtdPessoasPalmares = 0
qtdPessoasCaruaru = 0
qtdPessoasRecife = 0
maiorIdadePalmares = -5.0
maiorIdadeCaruaru = -5.0
maiorIdadeRecife = -5.0
menorIdadePalmares = 300
menorIdadeCaruaru = 300
menorIdadeRecife = 300
qtdPessoasAte25SalarioAcima200 = 0
idadePessoaMaiorSalario = 0
regiaoPessoaMaiorSalario = ""
maiorSalario = -5.0
while True:
  regiao = input("Digite a região: ")
  while regiao.lower() != "palmares" and regiao.lower() != "caruaru" and regiao.lower() != "recife":
    regiao = input("Região inválida, Digite a região: ")
  idade = int(input("Digite a idade: "))
  if idade < 0:
    break
  salario = float(input("Digite o salário: "))
  if idade <= 25:
    if salario > 200:
      qtdPessoasAte25SalarioAcima200 = qtdPessoasAte25SalarioAcima200 + 1
  if salario > maiorSalario:
    maiorSalario = salario
    idadePessoaMaiorSalario = idade
    regiaoPessoaMaiorSalario = regiao
  if regiao.lower() == "palmares":
    somaSalariosPalmares = somaSalariosPalmares + salario
    qtdPessoasPalmares = qtdPessoasPalmares + 1
    if idade > maiorIdadePalmares:
      maiorIdadePalmares = idade
    if idade < menorIdadePalmares:
      menorIdadePalmares = idade
  elif regiao.lower() == "caruaru":
    somaSalariosCaruaru = somaSalariosCaruaru + salario
    qtdPessoasCaruaru = qtdPessoasCaruaru + 1
    if idade > maiorIdadeCaruaru:
      maiorIdadeCaruaru = idade
    if idade < menorIdadeCaruaru:
      menorIdadeCaruaru = idade
  elif regiao.lower() == "recife":
    somaSalariosRecife = somaSalariosRecife + salario
    qtdPessoasRecife = qtdPessoasRecife + 1
    if idade > maiorIdadeRecife:
      maiorIdadeRecife = idade
    if idade < menorIdadeRecife:
      menorIdadeRecife = idade
if qtdPessoasPalmares != 0:
  mediaSalarioPalmares = somaSalariosPalmares / qtdPessoasPalmares
else:
  mediaSalarioPalmares = 0
if qtdPessoasCaruaru != 0:
  mediaSalarioCaruaru = somaSalariosCaruaru / qtdPessoasCaruaru
else:
  mediaSalarioCaruaru = 0
if qtdPessoasRecife != 0:
  mediaSalarioRecife = somaSalariosRecife / qtdPessoasRecife
else:
  mediaSalarioRecife = 0
print(f"Média salários Palmares = R$ {mediaSalarioPalmares:.2f}")
print(f"Média salários Caruaru = R$ {mediaSalarioCaruaru:.2f}")
print(f"Média salários Recife = R$ {mediaSalarioRecife:.2f}")
print(f"Maior idade Palmares: {maiorIdadePalmares}, Menor idade Palmares: {menorIdadePalmares}")
print(f"Maior idade Caruaru: {maiorIdadeCaruaru}, Menor idade Caruaru: {menorIdadeCaruaru}")
print(f"Maior idade Recife: {maiorIdadeRecife}, Menor idade Recife: {menorIdadeRecife}")
print(f"Quantidade de pessoas até 25 anos com salário acima de 200: {qtdPessoasAte25SalarioAcima200}")
print(f"Idade da pessoa com maior salário: {idadePessoaMaiorSalario}")
print(f"Região da pessoa com maior salário: {regiaoPessoaMaiorSalario}")