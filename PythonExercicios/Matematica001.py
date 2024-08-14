import math

n = int(input('Digite um número= '))
print('math.pi retorna o valor de Pi', math.pi)
print('math.sqrt retorna a raiz quadrada', math.sqrt(n))
print('math.fabs retorna o valor absoluto', math.fabs(n))
print('math.factorial retorna o valor fatorial', math.factorial(n))
print('math.log10 retorna o logaritmo de x na base 10', math.log10(n))
print('math.pow x elevado a y', math.pow(10, n))
print('math.ceil retorna o menor número inteiro maior ou igual a X', math.ceil(n))
print('math.floor retorna o maior numero inteiro menor ou igual a x', math.floor(n))

import random

print('random.random gera numero aleatorio entre 0 e 1', random.random)
print('10 para que seja um número entre 0 e 10', 10 * random.random())
print('random.choice([lista_itens]) define os números/letras aleatórios a serem gerados')
print(random.choice([16, 21, 17, 22, 94, 44]))
print(random.choice(['Goiaba', 'mamao', 'limão', 'banana']))
