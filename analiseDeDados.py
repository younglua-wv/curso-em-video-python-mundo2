idade = cont = homem = mulheres = maiores= 0
sexo = continua = ""
while True:
  print("--" * 15)
  print("CADASTRE UMA PESSOA")
  print("--" * 15)
  idade = int(input("Idade: "))
  sexo = str(input("Sexo: [M/F]: ")).strip().upper()[0]
  print("--" * 15)
  continua = str(input("Quer continuar? [S/N]: ")).strip().upper()[0]
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
print(f"Total de pessoas com mais de 18 anos: {cont}\nAo todo temos {homem} cadastrados\nE temos {mulheres} mulheres com menos de 20 anos.")