
dia01 = float(input('Digite seu faturamento do dia 01 = '))
print('')
dia02 = float(input('Digite seu faturamento do dia 02 = '))
print('')
# dia03 = str(input('Digite seu faturamento do dia 03 = '))

maior = str

if dia01 < dia02:
    maior = str('dia 02')
    print('Maior faturamento é {} = R$ {:.2f}'.format(maior, dia02))
    
else:
    maior = str('dia 01')
    print('Maior faturamento é {} = R$ {:.2f}'.format(maior, dia01))
    

    


