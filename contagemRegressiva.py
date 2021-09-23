from time import sleep

contador = 10

for contador in range(11, 1, -1):
  contador -= 1
  print(contador)
  sleep(1)
print("\nBOOM! BOOM! BOOM!")