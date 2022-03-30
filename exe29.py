velocidade= float(input('Diga a velocidade que estava o carro em km/h! '))
if velocidade >= 81:
    multa= (velocidade - 80) * 7
    print('Desculpe, mas você foi mutado no valor de R$ {:.2f}, por excesso de velocidade!'.format(multa))
else:
    print('parabéns você estar respeitando a velocidade da via!' )

