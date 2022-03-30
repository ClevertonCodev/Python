sal= float(input('Qual é o valor do seu salário? R$ '))
if sal <= 1250:
    s1= (sal*15/100) + sal
    #print('Seu salário teve um aumento de 15% e ficou no valor toral de R$ {:.2f}'.format(s1))
else:
    s1= (sal*10/100) + sal #pocento
    #s2= (sal*10/100) +sal

    #print('Seu salário teve um aumento de 10% e ficou no valor total de R$ {:.2f}'.format(s2))
print('Quem ganhava {} {:.2f} {} ficou no valor total de R$ {:.2f}'.format('\33[1:7:44m',sal,'\33m', s1 ))