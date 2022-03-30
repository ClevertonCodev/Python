pr= float(input('Qual é o preço do produto? R$ '))
porção = pr*5/100
final = pr - porção
print('O produto que custava R$ {:.2f}, na promoção com desconto de 5% vai custar R$ {:.2f}'.format(pr,final))
