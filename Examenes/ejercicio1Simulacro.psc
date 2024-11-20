Algoritmo ejercicio1Simulacro
	cantTempAltas <- 0
	cantTempModeradas <- 0
	cantTempNegativas <- 0
	bandera <- Verdadero
	// Hasta aca creo las variables a utilizar
	Mientras bandera==Verdadero Hacer
		Escribir 'Ingrese la temperatura'
		Leer temperatura
		Si temperatura==999 Entonces
			bandera = Falso
		SiNo
			Si temperatura > 30 y temperatura <=50 Entonces
				cantTempAltas <- cantTempAltas+1
			SiNo
				Si (temperatura>=0 y temperatura<=30) o temperatura==-1 Entonces
					cantTempModeradas <- cantTempModeradas+1
				SiNo
					Si temperatura<0 y temperatura <> -1 Entonces
						cantTempNegativas <- cantTempNegativas+1
					FinSi
				FinSi
			FinSi
		FinSi
	FinMientras
	Escribir "La cantidad de ciudades que registraron temperaturas altas son ",cantTempAltas
	Escribir "La cantidad de ciudades que registraron temperaturas moderadas son ",cantTempModeradas
	Escribir "La cantidad de ciudades que registraron temperaturas negativas son ",cantTempNegativas
FinAlgoritmo
