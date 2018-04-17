import datetime

a = datetime.date.today().year
m = datetime.date.today().month
d = datetime.date.today().day

baseIPDO = 'http://sdro.ons.org.br/SDRO/DIARIO/'

if m < 10:
    if d < 10:
        enderecoIPDO = baseIPDO + str(a) + '_0' + str(d) + '_0' + str(m) + '/Html/DIARIO_0' + str(d) + '-0' + str(m) + '-' + str(a) + '.xlsx'
    else:
        enderecoIPDO = baseIPDO + str(a) + '' + str(d) + '_0' + str(m) + '/Html/DIARIO' + str(d) + '-0' + str(m) + '-' + str(a) + '.xlsx'
else:
    if d < 10:
        enderecoIPDO = baseIPDO + str(a) + '0' + str(d) + '' + str(m) + '/Html/DIARIO_0' + str(d) + '-' + str(m) + '-' + str(a) + '.xlsx'
    else:
        enderecoIPDO = baseIPDO + str(a) + '' + str(d) + '' + str(m) + '/Html/DIARIO_' + str(d) + '-' + str(m) + '-' + str(a) + '.xlsx'

print(enderecoIPDO)

if m == 1:
    mes = 'JAN'
    mesPasta = 'Janeiro'
elif m == 2:
    mes = 'FEV'
    mesPasta = 'Fevereiro'
elif m == 3:
    mes = 'MAR'
    mesPasta = 'Mar%C3%A7o'
elif m == 4:
    mes = 'ABR'
    mesPasta = 'Abril'
elif m == 5:
    mes = 'MAI'
    mesPasta = 'Maio'
elif m == 6:
    mes = 'JUN'
    mesPasta = 'Junho'
elif m == 7:
    mes = 'JUL'
    mesPasta = 'Julho'
elif m == 8:
    mes = 'AGO'
    mesPasta = 'Agosto'
elif m == 9:
    mes = 'SET'
    mesPasta = 'Setembro'
elif m == 10:
    mes = 'OUT'
    mesPasta = 'Outubro'
elif m == 11:
    mes = 'NOV'
    mesPasta = 'Novembro'
elif m == 12:
    mes = 'DEC'
    mesPasta = 'Dezembro'
