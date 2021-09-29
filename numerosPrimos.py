numero = int(input("Digite um número: "))
contador = 0
for i in range(1, numero+1):
  if numero % i == 0:
    print('\033[33m', i, '\033[m', end=" ")
    contador += 1
  else:
    print('\033[31m', i, '\033[m', end=" ")
print(f"\nO numero {numero} foi divisível {contador} vezes ", end="")
if contador > 2:
  print("e por isso ele NÃO É PRIMO!")
else:
  print("e por isso ele É PRIMO!")
  