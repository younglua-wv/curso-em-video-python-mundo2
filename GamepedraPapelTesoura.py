from random import randint
from time import sleep

nome = input("Nome do Jogador: ")

itens = ("Pedra", "Papel", "Tesoura")

opcao = int(input("\nSuas opções:\n\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n\nQual é a sua jogada? "))

jogadaMaquina = randint(0, 2)

if opcao > 2 or opcao < 0:
  print("\nOpção inválida!\nTente novamente!")

else:
  
  print("\nJO")
  sleep(1)
  print("KEN")
  sleep(1)
  print("PO!!!\n")
  
  print("-="*20)
  
  print(f"COMPUTADOR escolheu {itens[jogadaMaquina]}")
  
  print(f"{nome} escolheu {itens[opcao]}")
  
  print("-="*20)

  if jogadaMaquina == 0:
    if opcao == 0:
      print("EMPATE")
    elif opcao == 1:
      print(f"{nome} VENCEU")
    else:
      print("COMPUTADOR VENCEU")

  elif jogadaMaquina == 1:
    if opcao == 0:
      print("COMPUTADOR VENCEU")
    elif opcao == 1:
      print("EMPATE")
    else:
      print(f"{nome} VENCEU")

  elif jogadaMaquina == 2:
    if opcao == 0:
      print(f"{nome} VENCEU")
    elif opcao == 1:
      print("COMPUTADOR VENCEU")
    else:
      print("EMPATE")
