A= int(input("Ingrese número 1 "))
B= int(input("Ingrese número 2 "))
C=int(input("Ingrese número 3 "))
D=int(input("Ingrese número 4 "))
suma= A +B
print("El resultado de la suma es", suma)
if A > B:
    resta1= A-B
    print("El resultado de la resta es", resta1)
    multiplicacion1= resta1*C
    print("El resultado de la multiplicación es", multiplicacion1)
else:
    resta2= B-A
    print("El resultado de la resta es", resta2)
    multiplicacion2=resta2*C
    print("El resultado de la multiplicación es", multiplicacion2)

if D>C:
    division1=D/C
    print("El resultado de la división es", division1)
else:
    division2=C/D
    print("El resultado de la división es", division2)


