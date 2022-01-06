continua = "S"
produto = ""
barato = ""
maiorQueMil = cont = precoBarato = 0
total = 0.0
print("--"*20)
print("           LOJA SUPER BARATÃO")
print("--"*20)

while continua == "S":
  produto = str(input("Nome do Produto: "))
  preco = float(input("Preço: R$"))
  continua = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
  total += preco
  cont += 1
  if preco > 1000.00:
    maiorQueMil += 1 
  if cont == 1 or preco < precoBarato:
    precoBarato = preco
    barato = produto

print("------------ FIM DO PROGRAMA ------------")
print(f'O total da compra foi de R${total:.2f}\nTemos {maiorQueMil} produto(s) custando mais de R$1000,00\nO produto mais barato foi {barato} que custa R${precoBarato}')