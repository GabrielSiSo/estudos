# Faça um programa que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
print('Descubra quanto equivale um desconto de 5% no produto que você deseja comprar\n')
p = float(input('Digite o preço do produto que você deseja comprar:'))
print(f'O produto com 5% de desconto custa {p-(p*5/100)}')