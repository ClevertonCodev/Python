larg = float(input('Largura da parede:'))
alt = float (input('Altura de parde:'))
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é DE {}m².'.format(larg,alt,area))
tina = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tina))