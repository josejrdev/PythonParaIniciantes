"""
Algoritmo que converte uma quantidade de segundos inteiros informada pelo
usuário para o formato de horas, minutos e segundos. O programa utiliza
uma função para realizar a conversão e exibe o resultado no formato
HH:MM:SS.
"""

def conv_segundos_horas(s):
  # 60 * 60 = 3600
  horas = s // 3600
  minutos = (s % 3600) // 60
  segundos = (s % 3600) % 60
  return ("%d:%0.2d:%0.2d" % (horas,minutos,segundos))

segundos = int(input("Digite a quantidade de segundos inteiros: "))

print(conv_segundos_horas(segundos))