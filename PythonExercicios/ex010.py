#Crie um programa que leia o quanto uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar us$1,00 = R$3,27
d= (float(input('Quanto dinheiro você tem na carteira= ')))
print('R${} Reais equivale a US${:.2f} Dolares'.format(d,d/3.27))