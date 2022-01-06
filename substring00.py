# -*- coding: utf-8 -*-
# Programa: substring00.py
# Programador:
# Data: 28/04/2015
# Este programa lê um texto e uma palavra com três caracters
# e verifica se a palavra ocorre no texto e imprime os resultados.
# início do módulo principal
# descrição das variáveis utilizadas
# str texto, palavra, resposta
# int tam1, tam2, i, j, posicao

# pré: texto palavra

# Passo 1. Leia as strings e compute o tamanho
# Passo 1.1. Leia a sequencia
texto = input()
# Passo 1.2. Leia a subsequencia
palavra = input()
# Passo 1.3. Compute o tamanho das strings
tam = len(texto)
# Passo 2. Encontre palavra em texto
# Passo 2.1. Incialize os índices das strings
i = 0
resposta = 'não'
# Passo 2.2. Compare os caracteres de subsequencia com sequencia
while i < tam-2:
   if texto[i]==palavra[0] and texto[i+1]==palavra[1] and texto[i+2]==palavra[2]:
      resposta = 'sim'
      i = tam # finaliza o laço
   else:
      i = i + 1
# Passo 3. Imprima o resultado
print(resposta)

# pós:     
# fim do módulo principal
