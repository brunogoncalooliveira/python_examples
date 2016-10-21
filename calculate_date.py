import sys
import datetime

"""
Função para calcular diferença de datas, excluindo sábados e domingos
"""
def calculate_date( mydate, rule ):
    import re

    sinal = ''
    dias = 0

    myrule= re.compile("[-+]\d+")
    if not myrule.match(rule):
        raise AssertionError('Regra (' + rule + ') para calcular datas invalida')
    else:
        sinal = rule[0]
        rule = rule.replace('+', '').replace('-', '')
        dias = int(rule)
        print('sinal: ' + sinal)
        print('dias: ' + str(dias))


    d = mydate
    cnt = 0
    while cnt < dias:
        if sinal == '-':
            d = datetime.datetime.strptime(d, '%Y-%m-%d') - datetime.timedelta(days=1)
        else:
            d = datetime.datetime.strptime(d, '%Y-%m-%d') + datetime.timedelta(days=1)
        d = d.strftime('%Y-%m-%d')
        if datetime.datetime.strptime(d, '%Y-%m-%d').weekday() not in [5, 6]:
            cnt += 1
    return d

if len(sys.argv) != 3:
    print('numero args invalidos (ex. 2016-10-20 +3)')
    exit()


mydata = sys.argv[1]
myrule = sys.argv[2]
print('')
print( 'IN' )
print( '-----------------' )
print( 'mydata: ' + mydata )
print( 'myrule: ' + myrule )
print( '' )
print( 'OUT' )
print( '-----------------' )
print(calculate_date(mydata, myrule))
print('')
