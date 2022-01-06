opção = ''
maioridade = homem = mulher20 = 0
while True:
    print('-' * 25)
    print('   CADASTRE UMA PESSOA')
    print('-' * 25)
    idade = int(input('Idade: '))
    if idade >= 18:
        maioridade += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if sexo == 'F' and idade < 20:
        mulher20 += 1
    if sexo == 'M':
        homem += 1
    print('-' * 25)
    opção = ' '
    while opção not in 'SN':
        opção = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if opção == 'S':
        print('-' * 25)
        print('   CADASTRE UMA PESSOA')
        print('-' * 25)
        idade = int(input('Idade: '))
        if idade >= 18:
            maioridade += 1
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if sexo == 'M':
            homem += 1
    elif opção == 'N':
        print(f'Total de pessoas com mais de 18 anos: {maioridade}\nAo todo temos {homem} homens cadastrados\nE temos {mulher20} mulheres com menos de 20 anos')
        break