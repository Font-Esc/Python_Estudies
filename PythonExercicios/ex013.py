#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s= float(input('Digite o salário do funcionário= '))
a= (s/100) * 15
print('O salário de {:.2f}R$ teve um aumento de 15% ficando num total de {:.2f}R$'.format(s,s+a))