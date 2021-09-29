maior = 0
menor = 0
for i in range(1, 6):
  a = float(input(f"Qual o peso da {i}° pessoa? "))
  if i == 1:  
    maior = a
    menor = a
  else:
    if a > maior:
      maior = a
    if a < menor:
      menor = a

print(f"\nO maior peso computado foi fe {maior:.1f}KG \nO menor peso computado foi de {menor:.1f}KG")