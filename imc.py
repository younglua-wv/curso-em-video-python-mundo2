peso = float(input("Qual é o seu peso? "))
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
  print(f"O IMC dessa pessoa é de {imc:.2f}\n\nPROCURE UM MÉDICO IMEDIATAMENTE!\n\nVocê está com OBESIDADE MÓRBIDA!")