print("="*21)
print("10 Termos de uma P.A.")
print("="*21)

termo = int(input("Digite o primeiro termo da P.A.: "))
razao = int(input("Digite a razão P.A.: "))

contador = termo + (10 - 1) * razao
for termo in range(termo, contador+1, razao):
  print(f"{termo} ->" ,end = " ")
print("ACABOU")