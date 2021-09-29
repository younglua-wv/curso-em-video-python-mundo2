contMedia = 0
maisVelho = 0
nomeMaisVelho = ""
mulherescont = 0
for i in range(1, 5):
  print(f"----- {i}° PESSOA -----")
  nome = input("Nome: ")
  idade = int(input("Idade: "))
  sexo = input("Sexo [M/F]: ").upper()
  if sexo == "M":
    maisVelho = idade
    nomeMaisVelho = nome
    if idade > maisVelho:
      maisVelho = idade
  if sexo == "F" and idade < 20:
    mulherescont += 1
  contMedia += idade
media = contMedia / 4
print(f"\nA média de idade do grupo é de {media:.2f} anos")
print(f"O homem mais velho tem {maisVelho} anos e se chama {nomeMaisVelho}")
print(f"Ao todo são(é) {mulherescont} mulher(es) com menos de 20 anos")  