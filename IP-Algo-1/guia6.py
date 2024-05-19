def rel(): exec(f"""import {__name__}\nimport importlib\nimportlib.reload({__name__})\n""")
import math

"""
1.1. problema imprimir_hola_mundo () {
	requiere: { T rue }
	asegura: { imprime "Hola mundo!" por consola}
}
"""
def imprimir_hola_mundo() -> None:
	print("Hola mundo!")

"""
1.2. imprimir_un_verso(): 
que imprima un verso de una canción que vos elijas,
respetando los saltos de línea mediante el caracter \n.
"""
def imprimir_un_verso() -> None:
	print("> Oye, dime nena\n> ¿Dónde ves ahora algo en mí\n> ¿Que no detestes?")
	
	
"""
1.3. raizDe2(): que devuelva la raíz cuadrada de 2 con 4 decimales. Ver función round
"""
def raizDe2() -> float:
	return round(math.sqrt(2), 2)

"""
1.4. problema factorial_de_dos() : Z {
	requiere: { True }
	asegura: {res = 2!}
}
"""
def factorial_de_dos() -> int:
	return 2

"""
1.5. perimetro: que devuelva el perímetro de la circunferencia de radio 1.
Utilizar la biblioteca math mediante el comando import math y la constante math.pi

problema perimetro () : R {
	requiere: { True }
	asegura: {res = 2*π }
}
"""
def perimetro() -> float:
	return 2*math.pi
	
"""
2.1. problema imprimir_saludo (in nombre: String) {
	requiere: { True }
	asegura: {imprime "Hola < nombre >" por pantalla}
}
"""
def imprimir_saludo(nombre : str) -> None:
	print("Hola", nombre)
	
"""
2.2. raiz_cuadrada_de(numero): que devuelva la raíz cuadrada del número.
"""
def raiz_cuadrada_de(numero : int) -> float:
	return sqrt(numero)
	
"""
2.3. fahrenheit_a_celsius(temp_far): que convierta una temperatura en grados Fahrenheit a grados Celcius.

problema fahrenheit_a_celsius (in t: R) : R {
	requiere: { True }
	asegura: {res = ((t − 32) * 5)/9}
}
"""
def fahrenheit_a_celsius(t : float) -> float:
	return (t-32)*5/9
	
"""
2.4. imprimir_dos_veces(estribillo): que imprima dos veces el estribillo de una canción.
Nota: Analizar el comportamiento del operador (*) con strings.
"""
def imprimir_dos_veces(e : str) -> None:
	print(2*e)

"""
2.5. problema es_multiplo_de (in n: Z, in m:Z) : Bool {
	requiere: {m ̸= 0}
	asegura: {(res = true) <--> (existe un k ∈ Z tal que n = m × k)}
}
"""
def es_multiplo_de(n : int, m : int) -> bool:
	return n % m == 0
	
"""
2.6. es_par(numero): que indique si numero es par (usar la función es_multiplo_de()).
"""
def es_par(n : int) -> bool:
	return n % 2 == 0
	
"""
2.7. cantidad_de_pizzas(comensales, min_cant_de_porciones)
que devuelva la cantidad de pizzas que necesitamos para que cada
comensal coma como mínimo min_cant_de_porciones porciones de pizza.
Considere que cada pizza tiene 8 porciones y que se prefiere que sobren porciones.
"""
def cantidad_de_pizza(n_comensales : int, n_min_porciones : int) -> int:
	return math.ceil(n_comensales*n_min_porciones/8)


"""
3.1. alguno_es_0(numero1, numero2):
dados dos números racionales, decide si alguno de los dos es igual a 0.
"""
def alguno_es_0(x : int, y : int) -> bool:
	return  not (x and y)

"""
3.2. ambos_son_0(numero1, numero2):
dados dos números racionales, decide si ambos son iguales a 0.
"""
def ambos_son_0(x : int, y : int) -> bool:
	return  not (x or y)


"""
esta especificación está mal, seria mas bien "es_nombre_corto"
3.3. problema es_nombre_largo (in nombre: String) : Bool {
requiere: { True }
asegura: {(res = true) <--> (3 <= |nombre| <= 8)}
}
"""
def es_nombre_corto(nombre : str) -> bool:
	return 3 <= len(nombre) <= 8
	
"""
3.4. es_bisiesto(año): que indica si un año tiene 366 días.
Recordar que un año es bisiesto si es múltiplo de 400, o bien
es múltiplo de 4 pero no de 100.
"""
def es_bisiesto(y : int) -> bool:
	return (y % 400 == 0) or ( y % 4 == 0 and not y % 100 == 0)


""" 
4. En una plantación de pinos, de cada árbol se conoce la altura expresada en metros.
El peso de un pino se puede estimar a partir de la altura de la siguiente manera:
3 kg por cada centímetro hasta 3 metros,
2 kg por cada centímetro arriba de los 3 metros.
resolver este ejercicio usando las funciones de python min y max
"""
def peso_pino(m : int) -> int: 
	h = 100*m # altura en cm
	return 3*min([300, h]) + 2*max([0, h-300])

def es_peso_util(peso : int) -> bool:
	return bool(max([0, peso-399]) and min([peso-1001, 0]))

def sirve_pino(m : int) -> bool:
	return es_peso_util(peso_pino(m))


"""
5. Implementar los siguientes problemas de alternativa condicional (if/else).
Especificar sin usar ifthenelsefi.
"""

"""
5.1. devolver_el_doble_si_es_par(numero);
que devuelve el doble del número en caso de ser par y el mismo número en caso contrario.

especifico:
problema devolver_el_doble_si_es_par(in n : Z) : Z {
	requiere: {True}
	asegura: {n=0 (mod 2) --> res=2*n}
	asegura: {n=1 (mod 2) --> res=n}
}
"""
def devolver_el_doble_si_es_par(n : int) -> int:
	return 2*n if n % 2 == 0 else n

"""
5.2 devolver_valor_si_es_par_sino_el_que_sigue(numero);
que devuelve el mismo número si es par y sino el siguiente.

especifico:
devolver_valor_si_es_par_sino_el_que_sigue(in n : Z) : Z {
	requiere: {True}
	asegura: {n=0 (mod 2) --> res=n}
	asegura: {n=1 (mod 2) --> res=n+1}
}
"""
def devolver_valor_si_es_par_sino_el_que_sigue(n : int) -> int:
	return n if n % 2 == 0 else n+1

"""
5.4 lindo_nombre(nombre) que dado un nombre, si la longitud es igual o mayor a 5 devolver una frase que diga
Tu nombre tiene muchas letras! y sino, Tu nombre tiene menos de 5 caracteres.
"""
def lindo_nombre(nombre : str) -> str:
	if (len(nombre) >= 5):
		return "Tu nombre tiene muchas letras"
	return "Tu nombre tiene menos de 5 caracteres"
	
