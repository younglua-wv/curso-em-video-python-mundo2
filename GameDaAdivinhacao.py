from random import randint

palpites = 0
print("Vou pensar em um número entre 0 e 10. \nTente Adivinhar...")
n = randint(0, 10)
numero = int(input("Em que número eu pensei? "))
while numero != n:
  if numero > 10 or numero < 0:
    print("Valor está fora do período")
    print("\nTente novamente...")
    numero = int(input("\nQual é o seu novo palpite? "))
  else:
    if numero < n:
      print("\nMais... Tente novamente...")
      print("=-" * 15)
      numero = int(input("\nQual é o seu novo palpite? "))
    elif numero > n:
      print("\nMenos... Tente novamente...")
      print("=-" * 15)
      numero = int(input("\nQual é o seu novo palpite? "))
  palpites += 1
print(f"\nParabéns, você acertou com {palpites + 1} palpites! \nUhuuul!!!")