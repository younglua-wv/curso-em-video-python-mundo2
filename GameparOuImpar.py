from random import randint
n = pc = cont = 0
resultado = result = game = ""
print("=-" * 15)
print("VAMOS JOGAR PAR OU ÍMPAR")
print("=-" * 15)
while True:
  n = int(input("Diga um valor: "))
  pc = randint(0, 10)
  soma = n + pc 
  game = str(input("Par ou Ímpar? [P/I] ")).strip().upper()[0]
  if soma % 2 != 0:
    resultado = "ÍMPAR"
    result = "I"
  elif soma % 2 == 0:
    resultado = "PAR"
    result = "P"
  print("--" * 15)
  print(f"Você jogou {n} e o computador {pc}. \nA somatória dos valores é um total de: {soma}, que é um número {resultado}!")
  print("--" * 15)
  if result == game:
    print("Você VENCEU!\nVamos jogar novamente...")
    print("=-" * 15)
    cont += 1
  elif result != game:
    print("Você PERDEU!")
    print("=-" * 15)
    print(f"GAME OVER! Você venceu {cont} vez(es).")
    break
  