# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²

print('Vamos descobrir quantos litros de tinta você precisa para pintar sua parede\n')
l = float(input('Qual a largura em metros da parede que você deseja pintar:'))
a = float(input('Qual a altura em metros da parede que você deseja pintar:'))
t = (l * a)/2
print(f'Você vai precisar de {t}L de tinta para pintar a parede')
