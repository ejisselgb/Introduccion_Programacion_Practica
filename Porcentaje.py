print("Corte 1")
corte1n1= float(input("Ingrese nota 1 "))
corte1n2= float(input("Ingrese nota 2 "))
corte1n3= float(input("Ingrese nota 3 "))
corte1 = ((corte1n1 + corte1n2 + corte1n3)/3) * 0.2

print("Corte 2")
corte2n1= float(input("Ingrese nota 1 "))
corte2n2= float(input("Ingrese nota 2 "))
corte2n3= float(input("Ingrese nota 3 "))
corte2 = ((corte2n1 + corte2n2 + corte2n3)/3) * 0.2

print("Corte 3")
corte3n1=float(input("Ingrese nota 1 "))
corte3n2= float(input("Ingrese nota 2 "))
corte3n3= float(input("Ingrese nota 3 "))
corte3 = ((corte3n1 + corte3n2 + corte3n3)/3) * 0.6

notafinal= corte1 + corte2 +corte3
print("La nota final es ", float(notafinal))