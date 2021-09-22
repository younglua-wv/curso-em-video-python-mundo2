from datetime import date

anoDeNascimento = int(input("Ano de nascimento: "))

anoAtual = date.today().year

idadeAtual = anoAtual - anoDeNascimento

if idadeAtual <= 9:
  print(f"O atleta tem {idadeAtual} anos.\nClassificação: MIRIM")
elif idadeAtual > 9 and idadeAtual <= 14:
  print(f"O atleta tem {idadeAtual} anos.\nClassificação: INFANTIL")
elif idadeAtual > 14 and idadeAtual <= 19:
  print(f"O atleta tem {idadeAtual} anos.\nClassificação: JÚNIOR")
elif idadeAtual > 19 and idadeAtual <=25:
  print(f"O atleta tem {idadeAtual} anos.\nClassificação: SÊNIOR")
else:
  print(f"O atleta tem {idadeAtual} anos.\nClassificação: MASTER")