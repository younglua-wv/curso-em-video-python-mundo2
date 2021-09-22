from random import randint
from time import sleep

opcao = int(input("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n\nQual é a sua jogada? "))

sleep(1)
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!")
sleep(2)

jogadaMaquina = randint(0, 2)

print("-="*20)
print(f"COMPUTADOR jogou {jogadaMaquina}\nJOGADOR jogou {opcao}")
print("-="*20)

if jogadaMaquina == 0:
  if opcao == 0:
    print("EMPATE")
  elif opcao == 1:
    print("JOGADOR VENCE")
  else:
    print("COMPUTADOR VENCE")

elif jogadaMaquina == 1:
  if opcao == 0:
    print("COMPUTADOR VENCE")
  elif opcao == 1:
    print("EMPATE")
  else:
    print("JOGADOR VENCE")

elif jogadaMaquina == 2:
  if opcao == 0:
    print("JOGADOR VENCE")
  elif opcao == 1:
    print("COMPUTADOR VENCE")
  else:
    print("EMPATE")

else:
  print("OPÇÃO INVÁLIDA!")

