palabra=input("diga una cadenas de texto (más de 5 caracteres): ")
x=0
for letra in palabra:
    x=x+1
if x<=5:
    print("la cadena tiene 5 o menos caracteres")
else:
    for letra in palabra:
        print(letra)
    print("el tamaño es de: ", x)
        


    
    
   
