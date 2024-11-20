Algoritmo ejercicio2Simulacro
	suma <- 0
	mayorPeso = -99999
	menorPeso <- 99999
	nombreMenorPeso <- ""
	nombreMayorPeso <- ""
	Para contador<-1 Hasta 5 Con Paso 1 Hacer
		Escribir "Ingresa tu nombre"
		Leer nombre
		Escribir "Ingresa tu peso"
		Leer peso
		suma <- suma+peso
		Si peso>mayorPeso Entonces
			mayorPeso <- peso
			nombreMayorPeso <- nombre
		FinSi
		Si peso<menorPeso Entonces
			menorPeso <- peso
			nombreMenorPeso <- nombre
		FinSi
	FinPara
	promedio <- suma/5
	Escribir "El socio con menor peso es ",nombreMenorPeso," con un peso de ",menorPeso
	Escribir "El socio con mayor peso es ",nombreMayorPeso, " con ", mayorPeso
	Escribir "El promedio de pesos es ",promedio
FinAlgoritmo
