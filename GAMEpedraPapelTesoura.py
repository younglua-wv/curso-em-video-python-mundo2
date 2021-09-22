from random import randint
from time import sleep

opcao = int(input("Suas opções:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA\n\nQual é a sua jogada? "))

sleep(1)
print("\nJO")
sleep(1)
print("KEN")
sleep(1)
print("PO!!!\n")
sleep(2)

jogadaMaquina = randint(0, 2)

print("-="*20)
'''if jogadaMaquina == 0 and opcao == 1 or jogadaMaquina == 1 and opcao == 2 or jogadaMaquina == 2 and opcao == 0:
  "PEDRA" = 0  
  "PAPEL" = 1
  "TESOURA" = 2
  print(f"COMPUTADOR jogou {jogadaMaquina}\nJOGADOR jogou {opcao}")
  print("-="*20)
  print("JOGADOR VENCE")

elif opcao == jogadaMaquina:
  "PEDRA" = 0  
  "PAPEL" = 1
  "TESOURA" = 2
  print(f"COMPUTADOR jogou {jogadaMaquina} \nJOGADOR jogou {opcao}")
  print("-="*20)
  print("EMPATE")

else:
  "PEDRA" = 0  
  "PAPEL" = 1
  "TESOURA" = 2
  print(f"COMPUTADOR jogou {jogadaMaquina}\nJOGADOR jogou {opcao}")
  print("-="*20)
  print("COMPUTADOR VENCE")'''
