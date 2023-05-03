Algoritmo ejercicio4
	Definir l1,l2,l3 Como Real
	Escribir "Ingrese un lado"
	leer l1
	Escribir "Ingrese un segundo lado"
	leer l2
	Escribir "Ingrese un tercer lado"
	leer l3
	si l1 = l2 y l1 = l3 Entonces
		Escribir "El triangulo es Equilatero"
	FinSi
	
	si l1 =n2 y l1 <> l3 Entonces
		Escribir "El triangulo es isoseles"
	FinSi
	
	si l2 = l3 y l2 <> l1 Entonces
		Escribir "El triangulo es isosceles"
	FinSi
	
	si l3 = l1 y l3 <> l2 Entonces
		Escribir "El triangulo es isosceles"
	FinSi
	
	si l1 <> l2 y l1 <> l3 y l2 <> l3 Entonces
		Escribir "El triangulo es escaleno"
	FinSi
	
	perimetro = l1 + l2 + l3
	Escribir "El perimetro es ",perimetro
	heron= (l1 + l2 +l3)/2
	area= raiz(heron*(heron - l1)*(heron-l2)*(heron-l3))
	Escribir "El area es: ",area
FinAlgoritmo
