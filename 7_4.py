# -*- coding: utf-8 -*-
"""7-4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oHGiTz5AuMUxfyoDaPKZVSO5CPL3jKt7
"""

s = input("Ingrese una opción, recuerde ingresar una mayuscula")
if s == "A":
  print("Opción de registro")
elif s == "B":
  print("Opción de login")
else: 
  print("Opción no válida para el inicio de sesión")

nA = float(input("Ingrese un número A "))
nB = float(input("Ingrese un número B "))
suma = nA + nB
print("El resultado de la suma es: " , suma)
if nA >= nB:
  resta = nA - nB
else:
  resta = nB- nA
print("El resultado de la resta es: " , resta)
nC = float(input("Ingrese un número C "))
multip = resta * nC
print("El resultado de la multiplicación es: " , multip)
nD = float(input("Ingrese un número D "))
if nC < nD:
  d = nD / nC
else:
  d = nC / nD
print("El resultado de la división es: " , d)

for i in range(1, 100):
  if i%2 == 0:
    continue
  print("El número es impar: ", i)

n1 = float(input("Ingrese un número "))
n2 = float(input("Ingrese otro número "))
x=1
s1 = n1 + n2
sum = s1
while sum < 100:
  print("Suma" ,x , ": ", sum)
  if n1 >= 40 or n2 >= 40:
    break
  x += 1
  sum += s1
  if sum>=100:
    print("Suma" , x, ": ", sum)



cna = input("Ingrese una palabra que sea superior a 5 letras ")
s=0
for i in cna:
  s += 1
if s>=5:
  for i in cna:
    print(i)
  print(" la palabra insertada se compone de " , s , " caracteres")
else:
  print("La palabra que ha insertado no cumple con el minimo de 5 caracteres")