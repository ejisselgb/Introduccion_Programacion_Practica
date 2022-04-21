num1=float(input("diga el número 1"))
num2=float(input("diga el número 2"))
suma=num1+num2
while suma<100:
    if num1<40 or num2<40:
        print (suma)
        suma=suma+num1+num2
    else:
        break