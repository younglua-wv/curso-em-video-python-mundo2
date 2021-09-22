valorCompras = float(input("Preço das compras: R$"))

opcaoDePagamento = int(input("FORMAS DE PAGAMENTO\n[ 1 ] à vista dinheiro/cheque\n[ 2 ] à vista cartão\n[ 3 ] 2x no cartão\n[ 4 ] 3x ou mais no cartão\n\nQual é a opção de pagamento? "))

if opcaoDePagamento == 1:
  valorComDesconto = valorCompras - (valorCompras*(10/100))
  print(f"Sua compra de R${valorCompras:.2f} vai custar R${valorComDesconto:.2f} com o desconto de 10% aplicado para pagamento no dinheiro ou cheque à vista na opção [ 1 ]!")
elif opcaoDePagamento == 2:
  valorComDesconto = valorCompras - (valorCompras*(5/100))
  print(f"Sua compra de R${valorCompras:.2f} vai custar R${valorComDesconto:.2f} com o desconto de 5% aplicado para pagamento no cartão à vista na opção [ 2 ]!")
elif opcaoDePagamento == 3:
  
  parcelas = valorCompras / 2
  
  print(f"Sua compra vai custar R${valorCompras:.2f} na opção [ 3 ] em parcelas de R${parcelas:.2f} 2x SEM JUROS!")
elif opcaoDePagamento == 4:
  
  quantidadeDeParcelas = int(input("\nQuantas parcelas? "))
  
  valorComJuros = valorCompras + (valorCompras*(20/100))

  parcelas = valorComJuros / quantidadeDeParcelas
  
  print(f"\nSua compra de R${valorCompras:.2f} vai custar R${valorComJuros:.2f} parcelada em {quantidadeDeParcelas}x no cartão de R${parcelas:.2f}!")
else:
  print("OPÇÃO INVÁLIDA!")
  