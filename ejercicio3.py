num1= int(input("Ingrese el número 1 "))
num2= int(input("Ingrese el número 2 "))
suma= num1+num2
print("El resultado de la suma es ", suma)
sumatotal= 0
while sumatotal < 100:
 if num1 < 40 and num2 < 40:
    sumatotal=sumatotal+num1+num2 
    print(sumatotal)
    
 else:  
    break