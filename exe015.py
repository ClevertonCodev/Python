alu= int(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
t = (alu * 60) + ( km * 0.15)
print('O total a pagar é {:.2f}!'.format(t))