count = 1
while(count == 1):
    r3 = 0
    r = 0
    n1 = float(input('digite um valor: '))
    sin = input('(+, -, *, /, %, **, //)\ndigite qual operaçao quer realizar: ')
    n2 = float(input('digite outro valor: '))
    r = eval(f'{n1} {sin} {n2}')
    print(r)
    count = 2
    while(count == 2):
        sin2 = input('digite "C" para zerar ou (+, -, *, /, %, **, //)\ndigite qual operaçao quer realizar: ')
        if(sin2 == "C" or sin2 == "c"):
            count = 1
            print("\n\n")
            break
        n3 = float(input('digite um valor: '))
        r2 = eval(f'{r} {sin2} {n3}')
        print(r2)
        r = r2
print('acabou')
