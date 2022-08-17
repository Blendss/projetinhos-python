import json
from os import path

filename = 'C:/Users/00110715/Desktop/data.json'
with open('data.json', 'a') as f:
    print("o arquivo esta aberto")
if path.isfile(filename) is False:
    print('o aquivo data.json foi criado')

BA = {}
count = 1
num = 1
pl = 1
while(pl == 1):
    if(count == 1):
        dicionario = {}
        idd = int(input('digite seu id da empresa: '))
        nome = input('digite seu nome: ')
        cargo = input('digite seu cargo: ')
        salario = int(input('digite seu salario: '))
        horae = int(input('digite o horario que voce chega: '))
        horas = int(input('digite o horario que voce sai: '))
        local = input('digite se trabalha home ou office: ')
        dicionario['id'] = idd
        dicionario['nome'] = nome
        dicionario['cargo'] = cargo
        dicionario['salario'] = salario
        dicionario['hora saida'] = horae
        dicionario['hora entrada'] = horas
        dicionario['hora local'] = local
        BA[num] = dicionario
        count = 0
        num += 1
        print(count)
    else:
        print(BA)
        r = input('criar novo usuário? s/n')
        if(r == 's'):
            count = 1
        if(r == 'n'):
            count = 0
            pl = 0
            data = json.dumps(BA, indent=4,separators=(". ", " = "), sort_keys=True)
            print(f)
            with open('data.json', 'a', encoding='utf-8') as f:
                #json.dump(data, f, ensure_ascii=False, indent=4, sort_keys=True)
                print("New json file is created from data.json file")
                f.write(data)
else:
    print('shutdown')