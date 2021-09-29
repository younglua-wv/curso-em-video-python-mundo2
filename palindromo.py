frase = input("Digite uma frase: ")
frase = frase.upper()
frase = frase.split()
frase = "".join(frase)
inverso = ""
for letra in range(len(frase) -1, -1, -1):
  inverso += frase[letra]
print(f"O inverso de {frase} é {inverso}.")
if inverso == frase:
  print("Temos um palíndromo")
else:
  print("A frase digitada não é um palíndromo!")

  
