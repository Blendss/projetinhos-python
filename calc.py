count = 1
while(count == 1):
    r3 = 0
    r = 0
    n1 = float(input('digite um valor: '))
    sin = input('digite qual operaçao (+, -, *, /) quer realizar: ')
    n2 = float(input('digite outro valor: '))
    if(sin == "+"):
        r = n1 + n2
    elif(sin == "-"):
        r = n1 - n2
    elif(sin == "*"):
        r = n1 * n2
    elif(sin == "/"):
        r = n1 / n2
    print(r)
    count = 2
    while(count == 2):
        sin2 = input('digite "C" para zerar ou qual operaçao (+, -, *, /) quer realizar: ')
        if(sin2 == "C" or sin == "c"):
            count = 1
            print("\n\n")
            break
        n3 = float(input('digite um valor: '))
        if(sin2 == "+"):
            r2 = (r + n3) + r3
        elif(sin2 == "-"):
            r2 = (r - n3) + r3
        elif(sin2 == "*"):
            r2 = (r * n3) + r3
        elif(sin2 == "/"):
            r2 = (r / n3) + r3
        print(r2)
        r3 = r2
print('acabou')