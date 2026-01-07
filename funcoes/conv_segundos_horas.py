def conv_segundos_horas(s):
  # 60 * 60 = 3600
  horas = s // 3600
  minutos = (s % 3600) // 60
  segundos = (s % 3600) % 60
  return ("%d:%0.2d:%0.2d" % (horas,minutos,segundos))
segundos = int(input("Digite a quantidade de segundos inteiros: "))
print(conv_segundos_horas(segundos))