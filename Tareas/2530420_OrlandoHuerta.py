# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2
"""
- ¿Qué es una función en Python y para qué sirve?
En Python, una función es un bloque de código reutilizable que realiza una tarea específica.
Se define con la palabra clave , seguida del nombre de la función y, opcionalmente, parámetros entre paréntesis.
Las funciones tienen varios propósitos fundamentales:
• 	Reutilización de código: Evitan repetir instrucciones, ya que puedes llamar la función múltiples veces.
• 	Organización y claridad: Dividen un programa en partes más pequeñas y comprensibles.
• 	Modularidad: Facilitan la construcción de programas grandes a partir de piezas más simples.
• 	Mantenimiento: Si necesitas cambiar la lógica, lo haces en un solo lugar.
• 	Abstracción: Permiten ocultar detalles internos y enfocarse en el resultado.

- ¿Qué diferencia hay entre parámetros (definition) y argumentos (call)?
Parámetros (en la definición)
• 	Son variables que se declaran al definir una función.
• 	Actúan como “espacios reservados” para recibir valores cuando la función sea llamada.
• 	Se escriben dentro de los paréntesis después del nombre de la función.
Argumentos (en la llamada)
• 	Son los valores reales que se pasan a la función cuando se ejecuta.
• 	Ocupan el lugar de los parámetros y permiten que la función trabaje con datos concretos.

- ¿Por qué es útil separar la lógica en funciones reutilizables?
Beneficios principales
• 	Reutilización de código
• 	Evitas repetir las mismas instrucciones en diferentes partes del programa.
• 	Una vez definida la función, puedes llamarla tantas veces como quieras.
• 	Modularidad
• 	El programa se divide en piezas independientes, cada una con una responsabilidad clara.
• 	Esto facilita integrar funciones en proyectos más grandes, como módulos de un flujo industrial.
• 	Legibilidad y claridad
• 	El código se vuelve más fácil de leer y entender.
• 	Otros desarrolladores (o tú mismo en el futuro) pueden comprender rápidamente qué hace cada parte.
• 	Mantenimiento y escalabilidad
• 	Si necesitas cambiar la lógica, lo haces en un solo lugar.
• 	Esto reduce errores y facilita la evolución del sistema.
• 	Validación y control de errores
• 	Cada función puede incluir validaciones específicas (ejemplo: verificar que un número sea positivo).
• 	Esto asegura que los datos que entran al sistema sean correctos antes de continuar.
• 	Abstracción
• 	Permite ocultar detalles internos y enfocarse en el resultado.

- ¿Qué es un valor de retorno y por qué es mejor devolver resultados en lugar de solo imprimirlos?
Un valor de retorno es el resultado que una función devuelve al terminar su ejecución, usando la palabra clave "return" .
Ese valor puede ser almacenado en una variable, usado en cálculos posteriores o pasado a otra función.
Imprimir () muestra el resultado en pantalla, pero no lo devuelve para seguir trabajando con él.
Devolver () es más flexible y poderoso porque:
• 	Reutilización de resultados
• 	Puedes usar el valor en cálculos posteriores, guardarlo en variables o pasarlo a otras funciones.
• 	Ejemplo: calcular un área y luego usarla en un modelo de costos.
• 	Separación de lógica y presentación
• 	La función se encarga de la lógica (cálculo, validación).
• 	Tú decides después cómo mostrar o usar el resultado (imprimir, guardar en archivo, enviar a otro sistema).
• 	Composición de funciones
• 	Permite encadenar funciones: el resultado de una puede ser la entrada de otra.
• 	Pruebas y validación
• 	Es más fácil probar funciones que devuelven valores, porque puedes comparar el resultado esperado con el obtenido.
• 	Si solo imprimen, tendrías que analizar la salida en pantalla, lo cual es menos práctico.
"""
# Problem 1 Rectangle area and perimeter (basic functions)
"""
Descripción:
Define dos funciones:
- calculate_area(width, height): regresa el área de un rectángulo.
- calculate_perimeter(width, height): regresa el perímetro.
El código principal debe leer (o definir) los valores, llamar a las funciones y mostrar los resultados.
Validaciones:
- width > 0
- height > 0
- Si alguna condición no se cumple, mostrar "Error: invalid input" y no llamar a las funciones.
"""
def calculate_area(width, height):
    
    return width * height

def calculate_perimeter(width, height):
    
    return 2 * (width + height)


try:
    
    width = float(input("Enter the width of the rectangle: "))
    height = float(input("Enter the height of the rectangle: "))

    
    if width > 0 and height > 0:
        area = calculate_area(width, height)
        perimeter = calculate_perimeter(width, height)
        print("Area:", area)
        print("Perimeter:", perimeter)
    else:
        print("Error: invalid input")

except ValueError:
    
    print("Error: invalid input")

"""
Inputs:
- width (float)
- height (float)

Outputs:
- "Area:" <area_value>
- "Perimeter:" <perimeter_value>

Entradas de prueba:
Entrada:
width: 5
height: 3

Salidas:
Area: 15
Perimeter: 16

Entrada:
width: 0.0001
height: 10

Salidas:
Area: 0.001
Perimeter: 20.0002

Entrada:
width: -5
height: 3

Salidas:
Error: Invalid input
"""
# Problem 2 Grade classifier (function with return string)
"""
Descripción:
Define una función classify_grade(score) que reciba una calificación numérica (0–100) y regrese una categoría:
- "A" si score >= 90
- "B" si 80 <= score < 90
- "C" si 70 <= score < 80
- "D" si 60 <= score < 70
- "F" si score < 60
El código principal debe llamar la función y mostrar el resultado.
Validaciones:
- 0 <= score <= 100
- Si no se cumple, mostrar "Error: invalid input" y no clasificar.
Salidas:
- "Score:" <score>
- "Category:" <grade_letter>
"""
def classify_grade(score):
   
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


try:
    score = float(input("Enter the grade (0-100): "))

    if 0 <= score <= 100:
        category = classify_grade(score)
        print("Score:", score)
        print("Category:", category)
    else:
        print("Error: invalid input")

except ValueError:
    
    print("Error: invalid input")

"""
Inputs:
- score (float o int)

Outputs:
- "Score:" <score>
- "Category:" <grade_letter>

Entradas de prueba:
Entrada:
Score: 85

Salidas:
Score: 85
Category: B

Entrada:
Score: 100

Salidas:
Score: 100
Category: A

Entrada:
Score: -5

Salidas:
Error: invalid input
"""
# Problem 3 List statistics function (min, max, average)
"""
Descripción:
Define una función summarize_numbers(numbers_list) que reciba una lista de números y regrese un diccionario con:
- "min": mínimo
- "max": máximo
- "average": promedio (float)
El código principal debe construir la lista (por ejemplo, a partir de texto separado por comas), 
llamar la función y mostrar los valores.
Validaciones:
- numbers_text no vacío tras strip().
- Lista no vacía después de la conversión.
- Todos los elementos deben poder convertirse a números; si alguno falla, mostrar "Error: invalid input".
"""
def summarize_numbers(numbers_list):
    
    return {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }


try:
    numbers_text = input("Enter numbers separated by commas: ").strip()

    if not numbers_text:
        print("Error: invalid input")
    else:
        try:
            numbers_list = [float(x) for x in numbers_text.split(",") if x.strip() != ""]

            if len(numbers_list) == 0:
                print("Error: invalid input")
            else:
                summary = summarize_numbers(numbers_list)
                print("Min:", summary["min"])
                print("Max:", summary["max"])
                print("Average:", summary["average"])
        except ValueError:
            print("Error: invalid input")

except Exception:
    print("Error: invalid input")
"""
Inputs:
- numbers_text (string; por ejemplo, "10,20,30")
- Internamente: numbers_list (list of float o int)

Outputs:
- "Min:" <min_value>
- "Max:" <max_value>
- "Average:" <average_value>

Entradas de prueba:
Entrada:
numbers_text = "1, 2, 3, 4, 5"

Salidas:
Min: 1.0
Max: 5.0
Average: 3.0

Entrada:
numbers_text = "7"

Salidas:
Min: 7.0
Max: 7.0
Average: 7.0

Entrada:
numbers_text = ""

Salidas:
Error: invalid input
"""
# Problem 4 Apply discount list (pure function)
"""
Descripción:
Define una función apply_discount(prices_list, discount_rate) que:
- reciba una lista de precios (float) y una tasa de descuento (por ejemplo, 0.10 para 10%)
- regrese una nueva lista con los precios ya descontados (no modificar la lista original).
El código principal debe:
- Crear una lista de precios.
- Llamar a la función.
- Mostrar la lista original y la nueva lista con descuento.
Validaciones:
- prices_text no vacío y lista resultante no vacía.
- Todos los precios > 0.
- 0 <= discount_rate <= 1; si no, "Error: invalid input".
"""
def apply_discount(prices_list, discount_rate):
    """Apply a discount to each price and return a new list."""
    return [price * (1 - discount_rate) for price in prices_list]


try:
    
    prices_text = input("Enter prices separated by commas: ").strip()
    discount_text = input("Enter discount rate (e.g., 0.10 for 10%): ").strip()

    
    if not prices_text or not discount_text:
        print("Error: invalid input")
    else:
        try:
            
            prices_list = [float(x) for x in prices_text.split(",") if x.strip() != ""]
            discount_rate = float(discount_text)

            
            if len(prices_list) == 0 or any(p <= 0 for p in prices_list):
                print("Error: invalid input")
            elif not (0 <= discount_rate <= 1):
                print("Error: invalid input")
            else:
                discounted_list = apply_discount(prices_list, discount_rate)
                print("Original prices:", prices_list)
                print("Discounted prices:", discounted_list)
        except ValueError:
            print("Error: invalid input")

except Exception:
    print("Error: invalid input")
"""
Inputs:
- prices_text (string; por ejemplo, "100,200,300")
- discount_rate (float, entre 0 y 1)

Outputs:
- "Original prices:" <original_list>
- "Discounted prices:" <discounted_list>

Entradas de prueba:
Entrada:
prices_text = "100, 200, 300"
discount_rate = 0.10

Salidas:
Original prices: [100.0, 200.0, 300.0]
Discounted prices: [90.0, 180.0, 270.0]

Entrada:
prices_text = "100"
discount_rate = 0

Salidas:
Original prices: [100.0]
Discounted prices: [100.0]

Entrada:
prices_text = ""
discount_rate = 0.10

Salidas:
Error: invalid input
"""
# Problem 5 Greeting function with default parameters
"""
Descripción:
Define una función greet(name, title="") que:
- Concatene opcionalmente el título antes del nombre (por ejemplo, "Dr. Alice", "Eng. Bob").
- Regrese el mensaje: "Hello, <full_name>!"
Si title está vacío, solo usar el nombre. El código principal debe llamar a la función usando argumentos posicionales y nombrados.
Validaciones:
- name no vacío tras strip().
- title puede estar vacío, pero si no lo está, también se normaliza con strip().
"""
def greet(name, title=""):
    
    name = name.strip()
    title = title.strip()

    
    if not name:
        return None

    
    if title:
        full_name = f"{title} {name}"
    else:
        full_name = name

    return f"Hello, {full_name}!"


try:
    
    name_input = input("Enter the name: ").strip()
    title_input = input("Enter the title (optional): ").strip()

    
    greeting = greet(name_input, title_input)

    if greeting:
        print("Greeting:", greeting)
    else:
        print("Error: invalid input")

except Exception:
    print("Error: invalid input")
"""
Inputs:
- name (string)
- title (string opcional)

Outputs:
- "Greeting:" <greeting_message>

Entradas de prueba:
Entrada:
name = "Alice"
title = ""

Salidas:
Greeting: Hello, Alice!

Entrada:
name = "   Alice   "
title = "   Dr.   "

Salidas:
Greeting: Hello, Dr. Alice!

Entrada:
name = ""
title = "Dr."

Salidas:
Error: invalid input
"""
# Problem 6 Factorial function (iterative or recursive)
"""
Descripción:
Define una función factorial(n) que regrese n! (n factorial). 
Puedes implementarla de forma iterativa (con for) o recursiva, pero debes documentar tu elección en comentarios. 
El código principal debe:
- Leer/definir n.
- Validar n.
- Llamar a factorial(n).
- Mostrar el resultado.
Validaciones:
- n entero.
- n >= 0.
- Opcional: limitar n a un máximo razonable (por ejemplo n <= 20) para evitar números demasiado grandes; 
si no se cumple, mostrar "Error: invalid input".
"""
def factorial(n):
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


try:
    
    n_text = input("Enter a non-negative integer (max 20): ").strip()

    
    if not n_text.isdigit():
        print("Error: invalid input")
    else:
        n = int(n_text)

        if n < 0 or n > 20:
            print("Error: invalid input")
        else:
            fact_value = factorial(n)
            print("n:", n)
            print("Factorial:", fact_value)

except Exception:
    print("Error: invalid input")
"""
Inputs:
- n (int)

Outputs:
- "n:" <n>
- "Factorial:" <factorial_value>

Entradas de prueba:
Entrada:
n = 5

Salidas:
n: 5
Factorial: 120

Entrada:
n = 0

Salidas:
n: 0
Factorial: 1

Entrada.
n = -3

Salidas:
Error: invalid input
"""
# Conclusión 
"""
¿Cómo las funciones ayudan a organizar y reutilizar el código?
• Encapsulación de tareas: Una función agrupa instrucciones que cumplen un propósito específico, 
evitando que el programa sea un bloque desordenado.
• Claridad: Los nombres de las funciones describen lo que hacen, lo que facilita leer y entender el flujo del programa.
• Modularidad: Permite dividir un programa grande en piezas pequeñas y manejables, cada una con su propia responsabilidad.

¿Qué ventajas tiene devolver valores con return en lugar de solo imprimir?
Diferencia esencial
• Print(): Muestra información en pantalla, útil para depuración o interacción con el usuario, 
pero no devuelve nada que pueda usarse en cálculos posteriores.
• Return: Devuelve un valor al programa, lo que permite almacenarlo, procesarlo, 
reutilizarlo o combinarlo en otras operaciones.

¿Cómo el uso de parámetros y valores por defecto hace el código más flexible?
Parámetros: flexibilidad al recibir datos
• Generalización: Una función puede trabajar con distintos valores sin necesidad de reescribirla.
• Reutilización: El mismo bloque de código sirve para múltiples casos.
• Adaptabilidad: Permite que la función se integre en diferentes contextos.

Valores por defecto: simplicidad y versatilidad
• Opcionalidad: El usuario puede omitir parámetros si no necesita personalizar el comportamiento.
• Menos errores: Evita tener que pasar siempre todos los argumentos.
• Comportamiento estándar: Define un valor común que se usa automáticamente si no se especifica otro.
"""
# Referencias
"""
https://ellibrodepython.com/funciones-en-python
https://www.youtube.com/watch?v=9k91jETchkI
https://ebac.mx/blog/funciones-de-python
https://www.w3schools.com/python/python_functions.asp
https://aprendeconalf.es/docencia/python/manual/funciones/
"""
# url github
"""
https://github.com/2530420-alt/metodologias_de_la_programaci-n_prueba#
git@github.com:2530420-alt/metodologias_de_la_programaci-n_prueba.git

la neta no sabia cual poner, así que puse los dos
"""