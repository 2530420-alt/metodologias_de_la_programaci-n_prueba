# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2
"""
- ¿Qué es la serie de Fibonacci?
La serie de Fibonacci es una sucesión matemática en la que cada número 
se obtiene sumando los dos anteriores, comenzando típicamente con 0 y 1.

Se pide generar los primeros n elementos de la serie.
Es decir, si n = 5 , se deben calcular los 5 primeros términos de la sucesión
"""
# Problem: Fibonacci series up to n terms
"""
Descripción:
Implementa un programa que calcule y muestre la serie de Fibonacci hasta n términos, donde n es ingresado por el usuario. La serie debe comenzar en 0 y 1, por lo que:

- Si n = 1 → salida: 0  
- Si n = 2 → salida: 0, 1  
- Si n = 7 → salida: 0, 1, 1, 2, 3, 5, 8  
El programa debe:
1) Leer n desde la entrada estándar.  
2) Validar n.  
3) Generar la serie de Fibonacci con un bucle (for o while).  
4) Imprimir los términos en una sola línea, separados por espacios o comas.
Validaciones:
- n debe poder convertirse a entero.
- n >= 1.
- (Opcional) n <= 50 para evitar series demasiado grandes; si no se cumple, mostrar "Error: invalid input".
- Si la validación falla, NO calcular la serie.
"""
def fibonacci_series(n):
    
    series = []
    a, b = 0, 1
    for i in range(n):
        series.append(a)
        a, b = b, a + b
    return series

try:
    
    n_text = input("Enter the number of terms (1–50): ").strip()

    
    if not n_text.isdigit():
        print("Error: invalid input")
    else:
        n = int(n_text)

        
        if n < 1 or n > 50:
            print("Error: invalid input")
        else:
            series = fibonacci_series(n)
            print("Number of terms:", n)
            print("Fibonacci series:", ", ".join(str(x) for x in series))

except Exception:
    print("Error: invalid input")
"""
Inputs:
- n (int; número de términos de la serie a generar).

Outputs:
- "Number of terms:" <n> (opcional)
- "Fibonacci series:" <term_1> <term_2> ... <term_n>

Entradas de prueba:
Entrada:
n = 5

Salidas:
Number of terms: 5
Fibonacci series: 0, 1, 1, 2, 3

Entrada:
n = 1

Salidas:
Number of terms: 1
Fibonacci series: 0

Entrada:
n = 0

Salidas:
Error: invalid input
"""
# Conclusión 
"""
Cómo te ayudó el uso de un bucle para generar la serie?
1. Generación controlada de términos
• El bucle permite iterar exactamente n veces, produciendo los primeros n términos de la serie.
• Así se asegura que la salida tenga la longitud solicitada, ni más ni menos.
2. Simplicidad en la implementación
• Con un bucle, la lógica se reduce a actualizar dos variables (a y b) en cada paso:
a, b = 0, 1
for i in range(n):
    series.append(a)
    a, b = b, a + b
• Esto refleja directamente la definición matemática de Fibonacci sin necesidad de llamadas recursivas.
3. Eficiencia
• La versión iterativa con bucle es más rápida y consume menos memoria que la recursiva, 
porque no genera múltiples llamadas anidadas ni necesita manejar una pila de ejecución profunda.
• Cada término se calcula una sola vez y se guarda en la lista.
4. Flexibilidad
• 	El bucle se adapta fácilmente a validaciones:
• 	Si n=1, se ejecuta una sola iteración y devuelve 0.
• 	Si n=2, devuelve 0,1.
• 	También permite detener el cálculo en cualquier momento si se desea limitar la serie.
Por qué es importante manejar bien los casos especiales n = 1 y n = 2?
1. Definición matemática
- La serie de Fibonacci se construye sumando los dos términos anteriores.
- Sin embargo, para n=1 y n=2, no existen dos términos previos completos.
- Por eso, se deben tratar como casos base:
- n=1 -> [0]
- n=2 ->[0,1]
2. Evitar errores de índice
- Si no se manejan estos casos, el programa intentará acceder a posiciones inexistentes en la lista o variables no inicializadas.
- Ejemplo: intentar calcular F(2)=F(1)+F(0) sin haber definido correctamente los primeros valores puede causar errores.
3. Claridad en la salida
- Los usuarios esperan que el programa muestre exactamente los términos solicitados.
- Si n=1, debe aparecer solo el primer término (0).
- Si n=2, deben aparecer los dos primeros términos (0, 1).
- Esto asegura consistencia y confianza en el resultado.
"""
# Refencias
"""
https://www.w3schools.com/python/python_for_loops.asp
https://realpython.com/python-for-loop/
https://www.datacamp.com/es/tutorial/loops-python-tutorial
https://realpython.com/python-while-loop/
https://www.w3schools.com/python/python_while_loops.asp
"""
# url github
"""
https://github.com/2530420-alt/metodologias_de_la_programaci-n_prueba#
git@github.com:2530420-alt/metodologias_de_la_programaci-n_prueba.git

la neta no sabia cual poner, así que puse los dos
"""
