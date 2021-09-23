soma = 0
contaSoma = 0
for index in range(1, 500, 2):
  if index % 3 == 0:
    soma += index
    contaSoma += 1
print(f"A soma dos {contaSoma} valores solicitados é de {soma}!")