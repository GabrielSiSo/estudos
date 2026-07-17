# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. U$ 1,00 = R$ 5,13

d = float(input('Digite quanto você tem na sua carteira:'))
print(f'Você pode comprar U${d/5.13:.2f}')