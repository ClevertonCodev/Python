import math
an = float(input('digite o ângulo que vc deseja?'))
seno = math.sin(math.radians(an))
print(' O ângulo de {} tem o SENO de {:.2f}'.format(an,seno))
co = math.cos(math.radians(an))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(an, co))
tan = math.tan(math.radians(an))
print('O ângulo de {} tem a TANGETE de {:.2f}'.format(an, tan))