from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
  a = int(input(f"Em que ano a {i}° pessoa nasceu? "))
  if anoAtual - a > 18:
    maior += 1
  elif anoAtual - a <= 18:
    menor += 1
print(f"\nAo todo tivemos {maior} pessoas maiores de idade \nE também tivemos {menor} pessoas menores de idade. ")