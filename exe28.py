from time import sleep
print('Olá pense em um número entre 0 e 5!')
sleep(3)
print('Pense...')
sleep(2)
print('Pense...')
sleep(2)
print('Pense...')
p=str(input('Pensou, sim ou não?  ')).strip().upper()
if p =='SIM':
    jogador=int(input('Digite o número que vc pensou! '))
    print('Processando...')
    sleep(2)
    from random import randint
    computador= randint(0, 5)
else:
    print('Entendi você não quer brincar,tchau!')

if jogador == computador:
    print('Parabéns! Você venceu!')
else:
    print('Ganhei! Pensei no número {} e não o {}!'.format(computador,jogador))