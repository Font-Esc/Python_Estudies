#Faça um programa que leia a largura e a altura de uma parede em metros e calcule a sua area e a quantidade de tinta necessaria para pintala sabendo que cada litro de tinta printa uma area de 2 metros
ml=float(input('Largura da parede= '))
ma=float(input('Altura da parede= '))
m=ml*ma
print('A parede tem {}m² e vai precisar de {}l litros de tinta.'.format(m,m/2))
