valorDoEmprestimo = float(input("Valor da casa: "))
salarioDoComprador = float(input("Qual o salário do comprador: "))
anosDeFinanciamento = int(input("Quantos anos de financimento? "))

valorMensal = valorDoEmprestimo / (anosDeFinanciamento * 12)

if (salarioDoComprador * (30/100)) <= valorMensal:
  print(f"\nPara pagar uma casa de R${valorDoEmprestimo:.2f} em {anosDeFinanciamento} anos a prestação será de R${valorMensal:.2f}\n\nEmpréstimo NEGADO!")
else:
  print(f"\nPara pagar uma casa de R${valorDoEmprestimo:.2f} em {anosDeFinanciamento} anos a prestação será de R${valorMensal:.2f}\n\nEmpréstimo CONCEDIDO!")