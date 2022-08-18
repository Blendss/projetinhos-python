from random import randint
import os
import time
import statistics


def clear_console():
    os.system('cls')

#loop jogo
vs = 1
print('Bem vindo ao jogo da matematica')
hi = []
ti = []

while (vs == 1): 
    vida = 3
    pt = 0   
    count = 1
    dc = 1
    #dificuldade
    while (dc == 1):
        n1 = 1
        n2 = 1
        n3 = 1
        print('escolha uma dificuldade entre 1, 2 ou 3')
        di = int(input('dificuldade: '))

        if (di == 1):
            n1 = 10
            n2 = 4
            n3 = 100
            dc = 0
            vida = 3
        if (di == 2):
            n1 = 50
            n2 = 6
            n3 = 100
            dc = 0
            vida = 2
        if (di == 3):
            n1 = 100
            n2 = 10
            n3 = 100
            dc = 0
            vida = 1
        if (di != 1 and di != 2 and di != 3):
            print('resposta inválida')
            count = 0
    #loop rodada
    
    while (count == 1):
        start_time=time.time()
        #escolha de sinal
        sm = randint(1,11)
        plu = "vidas"
        if (vida > 1):
            plu = "vidas"
        if (vida == 1):
            plu = "vida"
        print('você tem {0} {1}\n\n' .format(vida,plu))
        #soma
        if (sm >= 5):
            #soma
            x1 = randint(1,n1)
            x2 = randint(1,n1)
            print("digite a soma dos numeros",x1,"e",x2)
            x3 = x1 + x2
            r = int(input('a soma é: '))
            if (r == x3):
                end_time=time.time()-start_time
                print('resposta correta')
                pt += 1
                print(end_time)
                ti.append(end_time)
            else:
                end_time=time.time()-start_time
                print('resposta errada')
                vida -= 1
                print(end_time)
                ti.append(end_time)
        #multiplicaçao
        if (sm >= 10 and sm > 5):
            #multiplicaçao
            z1 = randint(1,n2)
            z2 = randint(1,n2)
            print("digite a multiplicaçao dos numeros",z1,"e",z2)
            z3 = z1 * z2
            rz = int(input('a multiplicaçao é: '))
            if (rz == z3):
                end_time=time.time()-start_time
                print('resposta correta')
                pt += 1
                print(end_time)
                ti.append(end_time)
            else:
                end_time=time.time()-start_time
                print('resposta errada')
                vida -= 1
                print(end_time)
                ti.append(end_time)
        if (sm == 11):
            #bonus
            y1 = randint(1,n3)
            y2 = randint(1,n3)
            y3 = randint(1,n3)
            print("Round Bonus\ndigite rapidamente o resultado da equaçao para ganhar uma vida:\n",y1,"*",y2,"+",y3)
            y4 = y1 * y2 + y3
            ry = int(input('o resultado é: '))
            if (ry == y4):
                end_time=time.time()-start_time
                print('resposta correta, você ganhou uma vida')
                pt += 3
                vida += 1
                print(end_time)
                ti.append(end_time)
            else:
                end_time=time.time()-start_time
                print('resposta errada, você nao será punido')
                print(end_time)
                ti.append(end_time)
        if(vida == 0):
            count = 0
    #jogar novamente ou parar
    else:
        pt = float(pt)
        tf = "%.1f" % statistics.mean(ti)
        tf = float(tf)
        print('você perdeu na dificuldade:',di)
        #print('sua pontuaçao foi:', (tf * 0.2) + (pt * 0.8))
        print('seus acertos foram:',pt)
        print('a média do seu tempo de resposta é:',"%.2f" % statistics.mean(ti))
        print('seu histórico de pontuaçao é:',hi)
        print('jogar novamente?')
        jn = input('s/n ')
        if (jn == 's'):
            clear_console()
            print('nova partida')
            hi.append(pt)

        if (jn == 'n'):
            vs = 0
            break
        elif (jn != 's'):
            vs = 0
            break