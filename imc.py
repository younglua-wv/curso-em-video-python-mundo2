'''peso = float(input("Qual é o seu peso? "))
altura = float(input("Qual é a sua altura?(m) "))

imc = peso / (altura * altura)

if imc < 18.5:
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nATENÇÃO!\n\nVocê está ABAIXO DO PESO!")
elif imc >= 18.5 and imc < 25:
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nPARABÉNS!\n\nVocê está na faixa de peso IDEAL!")
elif imc >= 25 and imc < 30:
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nATENÇÃO!\n\nVocê está com SOBREPESO!")
elif imc >= 30 and imc <= 40:
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nCUIDADO!\n\nVocê está com OBESIDADE!")
else:
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nPROCURE UM MÉDICO IMEDIATAMENTE!\n\nVocê está com OBESIDADE MÓRBIDA!")'''

print ("Bem vindo a Calculadora de IMC")

pergunta_nome = input("Qual é o seu nome? " )
nome = ("Olá" , pergunta_nome)
idade = input (f"Qual sua idade? ")
peso = float(input("Qual seu peso (em KG)? "))
altura = float(input("Qual sua Altura (em metros e usando ponto)? "))

print("Vamos calcular seu IMC")

imc = (peso / (altura * altura))

print(pergunta_nome , (f"seu IMC é: {imc:.2f}"))

if imc < 16:
	print("Seu estado é de Magreza grave\nProcure um médico ou nutricionista.")
elif imc < 17:
	print("Seu estado é de Magreza moderada\nPrecisa rever sua alimentação.")
elif imc < 18.5:
	print("Seu estado é de Magreza leve\nPrecisa rever sua alimentação.")
elif imc < 25:
	print("Você está Saudável.\nParabéns!")
elif imc < 30:
	print("Seu estado é de Sobrepeso\nPrecisa rever sua alimentação.")
elif imc < 35:
	print("Seu estado é de Obesidade Grau I\nProcure um médico ou nutricionista.")
elif imc < 40:
	print("Seu estado é de Obesidade Grau II (severa)\nProcure um médico ou nutricionista.")
else:
	print("Seu estado é de Obesidade Grau III (mórbida)\nProcure um médico ou nutricionista.")