num= int(input('Digite o número: '))
u = num // 1 % 10
d = num // 10 % 10
C = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena:  {}'.format(d))
print('Centena: {}'.format(C))
print('Milhar:  {}'.format(m))
