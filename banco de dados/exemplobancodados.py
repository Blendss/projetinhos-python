import json
import os.path

#digitando

BA = []
#filename = 'C:/Users/00110715/Desktop/data.json'
tr = os.path.exists('data.json')
print(tr)
if(tr == True):
    print("o arquivo esta aberto")
    with open('data.json') as json_file:
        BA = json.load(json_file)
if(tr == False):
    with open('data.json', 'a') as json_file:
        print('o aquivo data.json foi criado')
count = 1
pl = 1
while(pl == 1):
    if(count == 1):
        dicionario = {}
        i1 = input('digite: ')
        dicionario['i1'] = i1
        BA.append(dicionario)
        count = 0
        print(count)
    else:
        print(BA)
        r = input('adicionar mais? s/n')
        if(r == 's'):
            count = 1
        if(r == 'n'):
            count = 0
            pl = 0
            data = json.dumps(BA, indent=4,separators=(", ", ": "), sort_keys=True)
            with open('data.json', 'w', encoding='utf-8') as json_file:
                print("informaçoes do arquivo atualizadas")
                json_file.write(data)
else:
    print('shutdown')

#adicionando

import json
import os.path

BA = []
#filename = 'C:/Users/00110715/Desktop/data.json'
tr = os.path.exists('data.json')
print(tr)
if(tr == True):
    print("o arquivo esta aberto")
    with open('data.json') as json_file:
        BA = json.load(json_file)
if(tr == False):
    with open('data.json', 'a') as json_file:
        print('o aquivo data.json foi criado')

dicionario = {}
#código
BA.append(dicionario)

data = json.dumps(BA, indent=4,separators=(", ", ": "), sort_keys=True)
with open('data.json', 'w', encoding='utf-8') as json_file:
    print("informaçoes do arquivo atualizadas")
    json_file.write(data)