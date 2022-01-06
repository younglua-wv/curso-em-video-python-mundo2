idade = cont = homem = var = mulheres = maiores= 0
sexo = "M" or "F"
continua = "S" or "N"
while True:
  print("--" * 15)
  print("CADASTRE UMA PESSOA")
  print("--" * 15)
  idade = int(input("Idade: "))
  while opção not in 'MF':
    sexo = str(input("Sexo: [M/F]: ")).strip().upper()[0]
  print("--" * 15)
  while opção not in 'SN':
    opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
  if continua == "N":
    if sexo == "M":
      homem += 1
    if idade >= 18:
      cont += 1
    if sexo == "F" and idade < 20:
      mulheres += 1
    break
  else:
    if sexo == "M":
      homem += 1
    if idade >= 18:
      cont += 1
    if sexo == "F" and idade < 20:
      mulheres += 1
print(f"Total de pessoas com mais de 18 anos: {cont}\nAo todo temos {homem} cadastrados\nE temos {mulheres} mulher(es) com menos de 20 anos.")