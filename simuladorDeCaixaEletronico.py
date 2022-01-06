print("="*40)
print("               Banco CEV")
print("="*40)
sacar = 0
while True:
  sacar = float(input("Qual valor você deseja sacar? R$"))
  notacinquenta = sacar // 50
  sacar -= notacinquenta * 50
  if notacinquenta > 0:
    print(f"Total de {notacinquenta:.0f} cédulas de R$50,00")
  notavinte = sacar // 20
  sacar -= notavinte * 20
  if notavinte > 0:
    print(f"Total de {notavinte:.0f} cédulas de R$20,00")
  notadez = sacar // 10
  sacar -= notadez * 10
  if notadez > 0:
    print(f"Total de {notadez:.0f} cédulas de R$10,00")
  notaum = sacar // 1
  sacar -= notaum * 1
  if notaum > 0:
    print(f"Total de {notaum:.0f} cédulas de R$1,00")
  break
print("="*40)
print("Volte sempre ao BANCO CEV!")