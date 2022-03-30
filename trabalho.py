pe = (input(float('quantos atendimetos fez nas fisiovitalis? ')))

fv = 20.30 * pe

bi = (input(float( 'Quantos bipaps você instalou? ' )))

bipap = 33 * bi 

pt = (input(float( 'Quandos plantões na policlinica você fez? ')))

pl = 60 * pt 

sos = (input(float ('Quantos Sobre aviso você ficou? ')))

sobreaviso = 30 * sos 

vl = fv + bipap + pl + sobreaviso

print('o Valor total a receber da fisiovitalies é {}'.format(vl))