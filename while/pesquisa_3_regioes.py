gerenciador = 1
somaSalarioPalmares = 0.0
qtdPessoasPalmares = 0
somaSalarioCaruaru = 0.0
qtdPessoasCaruaru = 0
somaSalarioRecife = 0.0
qtdPessoasRecife = 0
maiorIdadePalmares = -5.0
menorIdadePalmares = 300
maiorIdadeCaruaru = -5.0
menorIdadeCaruaru = 300
maiorIdadeRecife = -5.0
menorIdadeRecife = 300
qtdIdadeAte25SalarioMaior200 = 0
maiorSalario = -5.0
idadePessoaMaiorSalario = 0
regiaoPessoaMaiorSalario = ""
while gerenciador == 1:
  idade = int(input("Digite a idade(negativa para encerrar): "))
  if idade < 0:
    gerenciador = 0
  else:
    regiao = input("Digite a região(Palmares, Recife, Caruaru): ")
    salario = float(input("Digite o salário: "))
    if regiao.lower() == "palmares":
      somaSalarioPalmares = somaSalarioPalmares + salario
      qtdPessoasPalmares = qtdPessoasPalmares + 1
      if idade > maiorIdadePalmares:
        maiorIdadePalmares = idade
      if idade < menorIdadePalmares:
        menorIdadePalmares = idade
    elif regiao.lower() == "caruaru":
      somaSalarioCaruaru = somaSalarioCaruaru + salario
      qtdPessoasCaruaru = qtdPessoasCaruaru + 1
      if idade > maiorIdadeCaruaru:
        maiorIdadeCaruaru = idade
      if idade < menorIdadeCaruaru:
        menorIdadeCaruaru = idade
    elif regiao.lower() == "recife":
      somaSalarioRecife = somaSalarioRecife + salario
      qtdPessoasRecife = qtdPessoasRecife + 1
      if idade > maiorIdadeRecife:
        maiorIdadeRecife = idade
      if idade < menorIdadeRecife:
        menorIdadeRecife = idade
    if idade <= 25 and salario > 200:
      qtdIdadeAte25SalarioMaior200 = qtdIdadeAte25SalarioMaior200 + 1
    if salario > maiorSalario:
      maiorSalario = salario
      idadePessoaMaiorSalario = idade
      regiaoPessoaMaiorSalario = regiao
if qtdPessoasPalmares != 0:
  mediaSalarioPalmares = somaSalarioPalmares / qtdPessoasPalmares
else:
  mediaSalarioPalmares = 0
if qtdPessoasCaruaru != 0:
  mediaSalarioCaruaru = somaSalarioCaruaru / qtdPessoasCaruaru
else:
  mediaSalarioCaruaru = 0
if qtdPessoasRecife != 0:
  mediaSalarioRecife = somaSalarioRecife / qtdPessoasRecife
else:
  mediaSalarioRecife = 0
print("Médias de salário:")
print(f"Palmares: R${mediaSalarioPalmares:.2f} Caruaru: R${mediaSalarioCaruaru:.2f} Recife: R${mediaSalarioRecife:.2f}")
print("Maiores idades:")
print(f"Palmares: {maiorIdadePalmares} Caruaru: {maiorIdadeCaruaru} Recife: {maiorIdadeRecife}")
print("Menores Idades:")
print(f"Palmares: {menorIdadePalmares} Caruaru: {menorIdadeCaruaru} Recife: {menorIdadeRecife}")
print(f"Quantidade de pessoas até 25 anos com salário acima de R$200,00: {qtdIdadeAte25SalarioMaior200}")
print(f"Dados do maior salário:")
print(f"Idade: {idadePessoaMaiorSalario} Região: {regiaoPessoaMaiorSalario}")