nome= str(input('Qual é o seu nome?')).strip()
print('Analizando seu nome.... ')
print('Seu nome em maiúsculo {}'.format(nome.upper()))
print('Seu nome em menusculo {}'.format(nome.lower()))
print('Seu nome todo tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))