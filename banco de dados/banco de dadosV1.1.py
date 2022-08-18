import json
import os.path

#filename = 'C:/Users/00110715/Desktop/data.json'
tr = os.path.exists('data.json')
print(tr)
if(tr == True):
    print("o arquivo esta aberto")
if(tr == False):
    with open('data.json', 'a') as json_file:
        print('o aquivo data.json foi criado')
    


BA = []
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
        BA.append(dicionario)
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
            with open('data.json') as json_file:
                load = json.load(json_file)
            BA.append(load)
            print(load)
            data = json.dumps(BA, indent=4,separators=(", ", ": "), sort_keys=True)
            print(json_file)
            with open('data.json', 'w', encoding='utf-8') as json_file:
                #json.dump(data, json_file, ensure_ascii=False, indent=4, sort_keys=True)
                print("informaçoes do arquivo atualizadas")
                json_file.write(data)
        if(r == 't'):
            with open('data.json') as json_file:
                data = json.load(json_file)
                print(data)

else:
    print('shutdown')