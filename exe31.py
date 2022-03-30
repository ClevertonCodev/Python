distancia = float(input('Qual é a distância da sua viagem em km? '))
print('Voce esta prestes a começar uma viagem de {:.0f} KM!'.format(distancia))
preco= distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}!'.format(preco))