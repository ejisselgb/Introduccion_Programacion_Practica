	Algoritmo Validacion_de_numeros_pares
		Escribir "Capture 3 n�meros y valide si estos son un n�mero par. Ingresar numero entero: "
		Leer numero_ingresado
		intentos = 3
		
		Repetir
			Escribir numero_ingresado
			operacion = num % 2
			Si operacion == 0 Entonces
				Escribir  "El n�mero " num " es PAR"
			SiNo
				Escribir  "El n�mero " num " es IMPAR"
			Fin Si
			intentos = intentos
		Hasta Que intentos >= 3
FinAlgoritmo
