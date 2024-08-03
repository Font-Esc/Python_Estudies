#faça um algoritimo que leia o proeço de um produto e mostre seu preço com 5% de desconto
v=float(input('Digite o preço do produto= '))
d=(v/100)*5
print('Produto de {}R$ agora com o cupom de 5% sai por apenas {}R$'. format(v,v-d))