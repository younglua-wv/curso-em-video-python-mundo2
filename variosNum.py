n = cont = s = 0
while True:
  n = int(input("Digite um número (999 para parar): "))
  if n == 999:
    break
  else:
    s += n
    cont += 1
print(f"A soma dos {cont} valores foi {s}!")