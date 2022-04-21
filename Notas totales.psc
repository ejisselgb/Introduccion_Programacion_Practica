	Algoritmo Notas_del_estudiante
		Escribir "Ingresar en el sistema las notas del estudiante"
		Escribir "ingresar la nota 1 para quices: " 
		Leer Quiz_1
		Escribir "ingresar la nota 2 para quices: " 
		Leer Quiz_2
		Escribir "ingresar la nota 3 para quices: " 
		Leer Quiz_3
		operacion=(Quiz_1*0.06)+(Quiz_2*0.06)+(Quiz_3*0.06)
		Nota_quices<-operacion
		Escribir "Nota total para quices: " Nota_quices
		Escribir "ingresar la nota 1 para parciales: " 
		Leer Parciales_1
		Escribir "ingresar la nota 2 para parciales: " 
		Leer Parciales_2
		Escribir "ingresar la nota 3 para parciales: " 
		Leer Parciales_3
		operacion=(Parciales_1*0.16)+(Parciales_2*0.16)+(Parciales_3*0.16)
		Nota_parciales<-operacion
		Escribir "Nota total para parciales: " Nota_parciales 
		Escribir "ingresar la nota 1 para tareas: " 
		Leer Tarea_1
		Escribir "ingresar la nota 2 para tareas: " 
		Leer Tarea_2
		operacion=(Tarea_1*0.15)+(Tarea_2*0.15)
		Nota_tareas<-operacion
		Escribir "Nota total para tareas: " Nota_tareas 
		operacion=Nota_tareas+Nota_parciales+Nota_quices
		Nota_total<-operacion
		Escribir "Nota total del curso: " Nota_total 
FinAlgoritmo
