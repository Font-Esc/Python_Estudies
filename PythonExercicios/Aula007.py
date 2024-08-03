# +Adição, -Subtração, *Multiplicação, /Divisão, **Potenciação, //Divisão inteira, %Resto da divisão
print('Vamos usar exemplos com o número 5 e 2 para realizar operações')
print('Soma 5+2= {}'.format(5+2))
print('Subtração 5-2= {}'.format(5-2))
print('Multiplicação 5*2= {}'.format(5*2))
print('Divisão 5/2= {}'.format(5/2))
print('Potenciação 5**2= {}'.format(5**2))
print('Divisão inteira 5//2= {}'.format(5//2))
print('Resto da divisão 5%2= {}' .format(5%2))

# Ordem de Procedência (Quem vai executar primeiro)
# 1= ()
# 2= **
# 3= *,/,//,%
# 4= + e -
print("Ordem de procedência", "1º= ()", '2º= **', '3º= *,/,//,%', '4º= + e -')
print('5+3*2== {}'.format(5+3*2))
print('3*5+4**2== {}'.format(3*5+4**2))
print('3*(5+4)**2== {}'.format(3*(5+4)**2))
print('O limite é o tamanho da sua memória ',999**455)
print('Potenciação tanto assim 4**3 como assim pow(4,3) = ', pow(4,3))
print('Raiz Quadrada de 81 (81**(1/2))',81**(1/2))
print('Raiz Cubica de 81 (81**(1/3))',81**(1/3))
print('='*80)
nome= input('Digite seu nome para aparecer 20 vezes = ')
print("Prazer em te conhecer {:20}!".format(nome))
print("Prazer em te conhecer {:>20}!".format(nome))
print("Prazer em te conhecer {:<20}!".format(nome))
print("Prazer em te conhecer {:^20}!".format(nome))
print("Prazer em te conhecer {:=^20}!".format(nome))
print("Prazer em te conhecer {:/^20}!".format(nome))

n1= int(input('Digite o Primeiro número '))
n2= int(input('Digite o Segundo número '))
som= n1+n2
sub= n1-n2
div= n1/n2
mul= n1*n2
di= n1//n2
pot= n1**n2
res= n1%n2
print('Soma= {}, Subtração= {}, Divisão= {}, Multiplicação= {}\n,Divisão inteira= {}, Potenciação= {}, Resto= {}.'.format(som,sub,div,mul,di,pot,res), end=" ")
# end=' ' e \n é o espaço que vai dar
print('\nMuito legal né', end="     ")
