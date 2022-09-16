H = []
count = 1
while(count == 1):
    r = 0
    n1 = float(input('digite um valor: '))
    sin = input('(+, -, *, /, %, **, //)\ndigite qual operaçao quer realizar: ')
    n2 = float(input('digite outro valor: '))
    r = eval(f'{n1} {sin} {n2}')
    H.append(['{0} {1} {2}'.format(n1,sin,n2),'={0}'.format(r)])
    print(r,'\n')
    count = 2
    while(count == 2):
        sin2 = input('digite "C" para zerar, "H" para ver o histórico ou (+, -, *, /, %, **, //)\ndigite qual operaçao quer realizar: ')
        if(sin2 == "C" or sin2 == "c"):
            count = 1
            print("\n\n")
            break
        if(sin2 == "H" or sin2 == "h"):
            for x in H:
                print(*x, sep="\n")
            count = 1
            print("\n")
            break
        n3 = float(input('digite um valor: '))
        r2 = eval(f'{r} {sin2} {n3}')
        print(r2,'\n')
        H.append(['{0} {1} {2}'.format(r,sin2,n3),'={0}'.format(r2)])
        r = r2
print('acabou')