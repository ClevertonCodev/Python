from math import hypot
co = float(input('comprimento do cateto oposto?'))
ca = float(input('comprimento do cateto adjacente?'))
hi = hypot(co,ca)
#hi = math.hypot(co,ca)
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print('A hipotenusa vai medir {:.2f}'.format(hi))
print('A hipotenusa vai medir {:.2f}'. format(hi))