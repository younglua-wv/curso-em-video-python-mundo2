# -*- coding: utf-8 -*-
# Programa: intersecao02.py
# Programador:
# Data: 10/09/2020
# Este programa lê duas listas com n e m itens, calcula a
# interseção das listas e imprime o resultado. Aula 24
# início do módulo principal
# descrição das variáveis utilizadas
# list ap1[], isd[], simul[]
# int  tam1, tam2

# pré: tam1 lista1[0] lista1[1] ... lista1[tam1-1]
#      tam2 lista2[0] lista2[1] ... lista2[tam1-1]

# Passo 1. Leia a entrada e inicialize as estruturas
# Passo 1.1. Leia o número de estudantes da lista ap1
tam1 = int(input())
# Passo 1.2. Leia os estunates da lista ap1
ap1 = list(map(int,input().split()))[:tam1]
# Passo 1.3. Leia o tamanho da lista isd
tam2 = int(input())
# Passo 1.4. Leia os estudates da lista isd
isd = list(map(int,input().split()))[:tam2]
# Passo 1.5. Inicilize a lista das matrículas simultaneas
simul = []
# Passo 2. Calcule as matrículas simultaneas
# Passo 2.2. Para cada estudante em ap1 verifique se está isd
for mat in ap1: 
   if mat in isd: 
      simul.append(mat)
# Passo 3. Imprima a nova lista
print(simul)

# pós: para i em {0..tam3-1} and (existe j em {0..tam1-1}) and
#      (existe l em {0..tam2-1}) |  
#      simul[i] == ap1[j] == isd[l]
# fim do módulo principal
