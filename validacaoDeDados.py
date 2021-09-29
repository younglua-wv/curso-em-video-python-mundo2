sexo = input("Informe seu sexo: [M/F] ").strip().upper()
while sexo not in 'FM':
  sexo = input("Dados inválidos.\nPor favor, informe seu sexo: ").strip().upper() 
print(f"Sexo {sexo} registrado com sucesso!")