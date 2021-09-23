numero = int(input("Digite um némro para ver sua tabuada de 0 à 10: "))
print("-" * 14)
for n in range(1, 11):
  print(f"{numero:2}  x  {n:2} = {numero * n:2}")
print("-" * 14)