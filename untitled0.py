# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ab9V91lY24umQEUJ3lO-WSKfQzMg1ce1
"""

num1= int(input("ingresa numero 1 "))
num2= int (input ("ingresa numero 2 "))

suma = num1+num2
print("el resultado de la suma es " , suma)

resta = num1-num2
print ("el resultado de la resta es " , resta)

division= num1/num2
print ("el resutado de la division es " , division)

multiplicación= num1*num2
print ("el resultado de la multiplicacion es " , multiplicación)

cort11= float(input("ingresa nota 1 de corte 1 "))
cort12= float(input("ingresa nota 2 de corte 1 "))
cort13= float (input("ingresa nota 3 de corte 1 "))
cort1=(cort11+cort12+cort13)/3

cort21= float(input("ingresa nota 1 de corte 2 "))
cort22= float(input("ingresa nota 2 de corte 2 "))
cort23= float (input("ingresa nota 3 de corte 2 "))
cort2=(cort21+cort22+cort23)/3

cort31= float(input("ingresa nota 1 de corte 3 "))
cort32= float(input("ingresa nota 2 de corte 3 "))
cort33= float (input("ingresa nota 3 de corte 3 "))
cort3=(cort31+cort32+cort33)/3
  
cortot=(cort1*0.2)+(cort2*0.2)+(cort3*0.6)
print("nota final es ", cortot)

pro1=float (input("ingresa valor producto 1 "))
pro2=float (input("ingresa valor producto 2 "))
pro3=float (input("ingresa valor producto 3 "))

iva1=pro1+(pro1*0.19)
iva2= pro2+(pro2*0.19)
iva3= pro3+(pro3*0.19)

tot=iva1+iva2+iva3
print ("el valor a pagar es " , tot)

