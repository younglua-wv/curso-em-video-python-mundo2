# -*- coding: utf-8 -*-
# Programa: decrescente.py
# Programador:
# Data: 07/11/2012
# Este programa lê uma lista de números verifica se os números
# da lista estão em ordem decrescente e imprime o resultado.
# O programa usa a função verifiqueOrdem para verificar se a 
# lista está em ordem decrescente.
# início do módulo principal
# descrição das variáveis utilizadas
# list lista
# int tam, i
# str msg
 
# pré: lista[0],lista[1],...,lista[tam-1]

# Passo 1. Leia a lista
# Passo 1.1. Leia os elementos da lista
lista = list(map(int, input().split()))
# Passo 1.2. Valcule o tamanho da lista
tam = len(lista)
# Passo 2. Verifique se a lista é decrescente
msg = 'verdadeiro'
i = 0
while i < tam-1:
   if lista[i] <= lista[i+1]:
      msg = 'falso'
      i = tam # finaliza o laço
   i = i + 1
# Passo 3. Imprima os resultados
print(msg)

# pós: 'verdadeiro' and para i em {0..tam-2}:lista[i]>lista[i+1]
#      or 'falso'
# fim do módulo principal

