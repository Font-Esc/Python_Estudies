import math
co = float(input('Digite o comprimento do cateto oposto = '))
ca = float(input('Digite o comprimento do cateto adjacente = '))
hi= math.hypot(co,ca)
sen= co/hi
cos= ca/hi
tan= ca/co
print('O comprimento da hipotenusa é igual a {:.2f}'.format(hi))
print('O valor do seno = {:.2f}'.format(sen))
print('O valor do cosseno = {:.2f}'.format(cos))
print('O valor da tangente = {:.2f}'.format(tan))
