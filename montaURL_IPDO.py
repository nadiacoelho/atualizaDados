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