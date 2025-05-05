from math import *

while True:
    da_esli = input("введите нет если не хотите решыть квадратное уровнение ")

    if da_esli == "нет":
        shislo1 = int(input("введите первое число "))
        shislo2 = int(input("введите второе число "))
        znak_deistva = (input("введите знак для действий между числами "))

        while True:
            if znak_deistva == '+' :
                rezultat = shislo1 + shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '-' :
                rezultat = shislo1 - shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '*' :
                rezultat = shislo1 * shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '/' :
                rezultat = shislo1 / shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '//' :
                rezultat = shislo1 // shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '**' :
                rezultat = shislo1 ** shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            elif znak_deistva == '%' :
                rezultat = shislo1 % shislo2
                print(shislo1 ,znak_deistva ,shislo2 , "=" , rezultat )
            shislo1 = int(input("введите первое число "))
            shislo2 = int(input("введите второе число "))
            znak_deistva = (input("введите знак для действий между числами "))
    else:
        argyment_a = int(input("введите аргумент a "))
        argyment_b = int(input("введите аргумент b "))
        argyment_c = int(input("введите аргумент c "))
        print(f"{argyment_a}x2 + {argyment_b}x + {argyment_c} = 0")
        D = argyment_b**2 - 4*argyment_a*argyment_c
        print("дискрименант" , D)

        if D < 0:
            print("корней нету ")
        elif D == 0:
            x = -argyment_b / (-2*argyment_a)
            print("x =" , x)
        elif D > 0:
            x1 = (-argyment_b + sqrt(D)) / (2 * argyment_a)
            print("x1 = " , x1)
            x2 = (-argyment_b - sqrt(D)) / (2 * argyment_a)
            print("x2 = " , x2)
    calkulator_konec = input("введите 'продолжыть' для продолжения ")        
    if calkulator_konec == "продолжыть":
        break

    