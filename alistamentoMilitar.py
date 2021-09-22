from datetime import date

anoDeNascimento = int(input("Qual o ano do seu nascimento? "))

anoAtual = date.today().year

idadeAtual = anoAtual - anoDeNascimento

anoDeAlistamento = anoDeNascimento + 18

previsaoDeAlistamento = anoAtual - anoDeAlistamento

#print(f"Current Year -> {date.year}")
if idadeAtual == 18:
  print("Você deve se alistar IMEDIATAMENTE!")

elif (anoAtual - anoDeNascimento) > 18:
  print(f"Você já deveria ter se alistado há {previsaoDeAlistamento} anos.\nSeu alistamento foi em {anoDeAlistamento}!")

else:
  print(f"Ainda falta(am) {18 - idadeAtual} anos para o alistamento.\nSeu alistamento será em {anoDeAlistamento}.")
