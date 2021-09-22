numero = int(input("Digite um número inteiro: "))

opcao = int(input("Digite uma das opções abaixo:\n[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL\n-> "))

if opcao == 1:
  print(f"O valor {numero} convertido para BINÁRIO é igual a {bin(numero)[2:]}!")
elif opcao == 2:
  print(f"O valor {numero} convertido para OCTAL é igual a {oct(numero)[2:]}!")
elif opcao == 3:
  print(f"O valor {numero} convertido para HEXADECIMAL é igual a {hex(numero)[2:]}!")
else:
  print(f"A opção {opcao} é uma opção INVÁLIDA, tente novamente!")