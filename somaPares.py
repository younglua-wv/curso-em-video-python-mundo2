soma = 0
cont = 0
for n in range(0,6):
  numero = int(input("Digite um número: "))
  if numero % 2 == 0:
    soma += numero
    cont += 1
print(f"A soma dos {cont} valores pares digitados é de: {soma}")