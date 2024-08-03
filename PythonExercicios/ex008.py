#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
m=int(input('Digite uma quantidade de metros= '))
print('{} metros é igual a \n{}mm\n{}cm\n{}dm\n{:.2f}dam\n{}hm\n{}km '.format(m,m*1000,m*100,m*10,m*0.1,m*0.01,m*0.001))