from itertools import count


cadena=input("Ingrese cadena de texto ")
tam_cad= len(cadena)
if tam_cad>5:
    for i in cadena:
        print(i)
             
else:
    print("Tamaño de cadena muy corto")
    exit()
 