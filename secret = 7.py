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

    