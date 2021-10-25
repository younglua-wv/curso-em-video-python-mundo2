numero = 0
while True:
  numero = int(input("Quer ver a tabuada de qual valor? "))
  print("-" * 14)
  if numero < 0:
    break
  else:
    for n in range(1, 11):
      print(f"{numero:2}  x  {n:2} = {numero * n:2}")
  print("-" * 14)
print("Programa encerrado pelo usuário!\nVolte sempre!")