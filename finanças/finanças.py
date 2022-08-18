x = input('voce ainda ganha o mesmo salario? s/n ')
if(x == 's'):
    sal = 3000
    gas = 300
    gaso = 1200
    final = sal - gas - gaso
    salano = sal * 12
    gasano = gas * 12 + gaso * 12
    pos = sal - gaso
    seg = (sal - gaso) * 0.2
    posano = pos * 12
    segano = seg * 12
    print('voce tem R${0} na conta' .format(final))
    print('voce ganha R${0} por ano' .format(salano))
    print('voce gasta em média R${0} por ano' .format(gasano))
    print('voce pode investir R${0}' .format(pos))
    print('voce pode investir com segurança R${0}' .format(seg))
    print('voce pode investir R${0} por ano' .format(posano))
    print('voce pode investir com segurança R${0} por ano' .format(segano))
    qua = int(input('quanto vc vai investir: '))
    tipo = int(input('qual vai ser o tipo de investimento (seguro = 1, medio = 2, arriscado = 3):'))
    if(tipo == 1):
        ret = qua * 0.015 + qua
        print('a media do seu retorno será R$',ret)
    if(tipo == 2):
        ret = qua * 0.3 + qua
        print('a media do seu retorno será R$',ret)
    if(tipo == 3):
        ret = qua * 0.015 + qua
        ret2 = qua * 0.5 + qua
        print('a media do seu retorno será de R$',ret,'a',ret2)

if(x == 'n'):
    sal = int(input('digite seu salario mensal: '))
    gas = int(input('digite quando gastou no mes: '))
    gaso = int(input('digite quando gastou no mes obrigatóriamente: '))
    final = sal - gas - gaso
    salano = sal * 12
    gasano = gas * 12 + gaso * 12
    pos = sal - gaso
    seg = (sal - gaso) * 0.2
    posano = pos * 12
    segano = seg * 12
    print('voce tem R${0} na conta' .format(final))
    print('voce ganha R${0} por ano' .format(salano))
    print('voce gasta em média R${0} por ano' .format(gasano))
    print('voce pode investir R${0}' .format(pos))
    print('voce pode investir com segurança R${0}' .format(seg))
    print('voce pode investir R${0} por ano' .format(posano))
    print('voce pode investir com segurança R${0} por ano' .format(segano))
    