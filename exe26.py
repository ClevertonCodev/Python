frase = str(input('Digite uma frase: ')).strip().lstrip().rstrip().upper()
print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
o = int(frase.find('A')+2) - (frase.count(' '))
print('A primeira letra A aparece na posição {}'.format(o))#frase.find('A')+1))
n = int(frase.rfind('A')+1) - (frase.count(' '))
print('A última letra A aparece na posição {}'.format(n))
#- frase.count(' ')))
