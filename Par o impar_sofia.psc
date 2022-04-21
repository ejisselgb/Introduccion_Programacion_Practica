	Algoritmo Validacion_de_numeros_pares
		Escribir "Capture 3 números y valide si estos son un número par. Ingresar numero entero: "
		Leer numero_ingresado
		intentos = 3
		
		Repetir
			Escribir numero_ingresado
			operacion = num % 2
			Si operacion == 0 Entonces
				Escribir  "El número " num " es PAR"
			SiNo
				Escribir  "El número " num " es IMPAR"
			Fin Si
			intentos = intentos
		Hasta Que intentos >= 3
FinAlgoritmo
