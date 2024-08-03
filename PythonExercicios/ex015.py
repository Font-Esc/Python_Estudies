d=float(60)
k=float(0.15)
di=float(input('Quantos dias você andou com o carro= '))
km=float(input('Quantos Km você andou com o carro= '))
kmm=km*k
dii=di*d
print('R${:.2f} a pagar pelo Km\nR${:.2f} de diaria a pagar\ntotal a pagar= {:.2f}'.format(kmm,dii,kmm+dii))