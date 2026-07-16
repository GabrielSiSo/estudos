#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n = input('Digite algo:')
print(type(n))
print('O que você digitou é uma letra:', n.isalpha())
print('O que você digitou possui letras ou números:', n.isalnum())
print('O que você digitou é um número decimal:', n.isdecimal())
print('O que você digitou é um dígito:', n.isdigit())
print('O que você digitou é um número:', n.isnumeric())
print('O que você digitou tem apenas letras minúsculas:', n.islower())
print('O que você digitou tem apenas letras maiúsculas:', n.isupper())
print('O que você digitou é um espaço:', n.isspace())
print('O que você digitou começa com letra maiúscula:', n.istitle())