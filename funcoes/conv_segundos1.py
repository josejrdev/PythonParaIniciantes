def conversor_s_h(s):
  horas = s // 3600
  minutos = (s % 3600) // 60
  segundos = (s % 3600) % 60
  return ("%d:%0.2d:%0.2d" %(horas,minutos,segundos))
segundos = int(input("Digite a quantidade de segundos inteiros: "))
print(conversor_s_h(segundos))