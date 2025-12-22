senha = "IFPE420ads1noite"
qtdTentativas = 0
listaHistoricoSenhas = []
while True:
  senhaUsuario = input("Digite a senha: ")
  listaHistoricoSenhas.append(senhaUsuario)
  qtdTentativas = qtdTentativas + 1
  if senhaUsuario == senha:
    break
print(f"Tentativas: {qtdTentativas}")
print(f"Histórico de senhas digitadas: {listaHistoricoSenhas}")