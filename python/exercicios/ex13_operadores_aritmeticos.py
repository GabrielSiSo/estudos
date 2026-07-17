# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
 
km = float(input('Digite quantos Km você percorreu com o carro alugado:'))
dia = int(input('Digite quantos dias você ficou com o carro alugado:'))
preco = (60*dia) + (km*0.15)
print(f'O total a ser pago pelos dias com o carro e pela quantidade de quilômetros percorridos com ele é R${p:.2f}')