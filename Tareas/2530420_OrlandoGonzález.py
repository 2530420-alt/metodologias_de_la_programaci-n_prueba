# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2
"""
- ¿Qué es un bucle for y para qué se usa típicamente?
Un bucle for es una estructura de control en programación que permite ejecutar 
un bloque de código un número determinado de veces. 
Se utiliza típicamente para iterar sobre una secuencia, como una lista o un array, 
o para realizar una acción un número específico de veces, que se conoce de antemano

- ¿Qué es un bucle while y cuándo es más natural usarlo?
Un bucle while ejecuta un bloque de código repetidamente mientras 
una condición booleana sea verdadera. Es más natural usarlo cuando 
no se sabe de antemano cuántas veces se repetirá el bucle, como en el 
caso de esperar una entrada válida del usuario o procesar datos hasta 
que se cumpla una condición de finalización

- ¿Qué son un contador y un acumulador?
Un contador es una variable que incrementa su valor en una cantidad fija (generalmente 1) 
para llevar la cuenta de eventos o iteraciones. Un acumulador es una variable que se utiliza 
para sumar valores que pueden variar a lo largo del tiempo, para obtener un total. 
Ambos son variables que deben inicializarse, y se usan comúnmente en bucles para realizar cálculos

Definir bien la condición de salida en un algoritmo o programa es crucial porque garantiza 
que el proceso termine en el momento correcto y no se quede atrapado en un ciclo infinito.
"""

# Problem 1: Sum of range with for
"""
Descripción:
Calcula la suma de todos los enteros desde 1 hasta n (incluyendo n). 
Además, calcula la suma solo de los números pares en ese mismo rango usando un bucle for.
Validaciones:
- Verificar que n pueda convertirse a int.
- n >= 1; si no se cumple, mostrar "Error: invalid input"
"""
try:
    
    n = int(input("Enter n: "))

    
    if n < 1:
        print("Error: invalid input")
    else:
        
        total_sum = sum(range(1, n + 1))

        
        even_sum = 0
        for i in range(2, n + 1, 2):
            even_sum += i

        
        print("Sum 1..n:", total_sum)
        print("Even sum 1..n:", even_sum)

except ValueError:
    print("Error: invalid input")

"""
Inputs:
- n (int; límite superior del rango).

Outputs:
- "Sum 1..n:" <total_sum>
- "Even sum 1..n:" <even_sum>

Entradas de prueba:
Entrada:
n = 5

Salidas:
Sum 1..n: 15 (1+2+3+4+5)
Even sum 1..n: 6 (2+4)

Entrada:
n = 2

Salidas:
Sum 1..n: 3 (1+2)
Even sum 1..n: 2

Entrada:
n = "abc"

Salidas:
Error: Invalid input
"""
# Problem 2: Multiplication table with for
"""
Descripción:
Genera y muestra la tabla de multiplicar de un número base, desde 1 hasta un límite m. Por ejemplo, si base = 5 y m = 4, muestra:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
Validaciones:
- base y m convertibles a int.
- m >= 1; si no, "Error: invalid input".
"""
try:
    
    base = int(input("Enter base number: "))
    m = int(input("Enter limit m: "))

    
    if m < 1:
        print("Error: invalid input")
    else:
        
        for i in range(1, m + 1):
            result = base * i
            print(f"{base} x {i} = {result}")

except ValueError:
    print("Error: invalid input")

"""
Inputs:
- base (int)
- m (int; límite de la tabla)

Outputs:
- Línea por cada multiplicación:
  - "5 x 1 = 5"
  - "5 x 2 = 10"
  - etc.

Entradas de prueba
Entrada:
base = 5
m = 4

Salidas:
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20

Entrada:
base = 3
m = 1

Salidas:
3 x 1 = 3

Entrada:
base = 5
m = 0

Salidas:
Error: Invalid input
"""
# Problem 3: Average of numbers with while and sentinel
"""
Descripción:
Lee números uno por uno hasta que el usuario ingrese un valor sentinela (por ejemplo, -1). 
Calcula el promedio de los números válidos ingresados y la cantidad de números leídos. 
Si el usuario sólo ingresa el sentinela sin números válidos, muestra un mensaje de error.
Validaciones:
- Cada lectura debe intentar convertirse a float.
- Ignorar el sentinela en los cálculos.
"""


numbers = [] 
sentinel = -1

print("Enter numbers one by one. Enter -1 to finish:")

while True:
    try:
        value = float(input("Number: "))
        if value == sentinel:
            break
        numbers.append(value)
    except ValueError:
        print("Error: invalid number, please try again.")

# After loop, check if we have valid data
if not numbers:
    print("Error: no data")
else:
    count = len(numbers)
    average_value = sum(numbers) / count
    print("Count:", count)
    print("Average:", average_value)

"""
Inputs:
- number (float; se lee repetidamente).
- sentinel_value (fijo en el código, por ejemplo: -1).

Outputs:
- "Count:" <count>
- "Average:" <average_value>
- Si no se ingresan datos válidos:
  - "Error: no data"

Entradas de prueba
Entrada:
10, 20, 20, -1

Salidas:
Count: 3
Average: 20

Entrada:
100,-1

Salidas:
Count: 1
Average: 100

Entrada:
-1

Salidas:
Error: no data
"""
# Problem 4 Password attempts with while
"""
Descripción:
Implementa un sistema sencillo de intento de contraseña. 
Define en el código una contraseña correcta (por ejemplo, "admin123"). 
El usuario tiene un máximo de MAX_ATTEMPTS intentos para introducirla. 
Si acierta dentro del límite, mostrar un mensaje de éxito. 
Si agota los intentos, mostrar un mensaje de bloqueo.
Validaciones:
- MAX_ATTEMPTS > 0 (definido como constante en el código, por ejemplo 3).
- Contar correctamente los intentos.
"""

MAX_ATTEMPTS = 3


if MAX_ATTEMPTS <= 0:
    print("Error: MAX_ATTEMPTS must be greater than 0")
else:
    
    CORRECT_PASSWORD = "admin123"

    attempts = 0
    success = False

    while attempts < MAX_ATTEMPTS:
        password = input("Enter password: ")
        attempts += 1

        if password == CORRECT_PASSWORD:
            print("Login success")
            success = True
            break
        else:
            print("Incorrect password. Attempts left:", MAX_ATTEMPTS - attempts)

    if not success:
        print("Account locked")
"""
Inputs:
- user_password (string; se lee en cada intento).

Outputs:
- Si acierta:
  - "Login success"
- Si falla todos los intentos:
  - "Account locked"

Entradas de prueba:
Entrada:
User inputs: "admin123" 

Salidas:
Login success

Entrada:
User inputs: "wrong1", "wrong2", "admin123"

Salidas:
Incorrect password. Attempts left: 2
Incorrect password. Attempts left: 1
Login success

Entrada:
User inputs: "wrong1", "wrong2", "wrong3"

Salidas:
Incorrect password. Attempts left: 2
Incorrect password. Attempts left: 1
Incorrect password. Attempts left: 0
Account locked
"""
# Problem 5 Simple menu with while
"""
Descripción:
Implementa un menú de texto que se repite hasta que el usuario seleccione la opción de salir. Ejemplo de menú:
1) Show greeting
2) Show current counter value
3) Increment counter
0) Exit
El programa debe ejecutar la acción correspondiente a cada opción y volver a mostrar el menú hasta que se elija 0.
Validaciones:
- Normalizar option (por ejemplo, convertir a int con manejo de error).
- Asegurar que sólo 0,1,2,3 sean aceptadas como válidas.
"""


counter = 0  

while True:
    
    print("\nMenu:")
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    option_text = input("Select an option: ").strip()

    try:
        option = int(option_text)  
    except ValueError:
        print("Error: invalid option")
        continue

    if option == 0:
        print("Bye!")
        break
    elif option == 1:
        print("Hello!")
    elif option == 2:
        print("Counter:", counter)
    elif option == 3:
        counter += 1
        print("Counter incremented")
    else:
        print("Error: invalid option")

"""
Inputs:
- option (string o int; elección del usuario).

Outputs:
- Mensajes según la opción:
  - "Hello!" para saludo.
  - "Counter:" <counter_value> para mostrar contador.
  - "Counter incremented" al incrementar.
  - "Bye!" al salir.
- Para opciones inválidas:
  - "Error: invalid option"

Entradas de pruebas:
Entrada:
Option = 1   → Show greeting
Option = 2   → Show counter value
Option = 3   → Increment counter
Option = 2   → Show counter value
Option = 0   → Exit

salidas:
Hello!
Counter: 0
Counter incremented
Counter: 1
Bye!

Entrada:
Option = 0

Salidas:
Bye!
"""
# Problem 6 Pattern printing with nested loops
"""
Descripción:
Usa bucles for anidados para imprimir un patrón de asteriscos en forma de triángulo rectángulo. Por ejemplo, para n = 4:
*
**
***
****
Validaciones:
- n convertible a int.
- n >= 1; si no, "Error: invalid input".
"""

n_text = input("Enter n: ").strip()

try:
    n = int(n_text)  
    if n < 1:
        print("Error: invalid input")
    else:
        
        for i in range(1, n + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
except ValueError:
    print("Error: invalid input")
"""
Inputs:
- n (int; número de filas del patrón).

Outputs:
- Patrón línea por línea:
  - "*"
  - "**"
  - "***"
  - "****"

Entradas de prueba:
Entrada:
n = 4

Salidas:
*
**
***
****

Entrada:
n = 1

Salidas:
*

Entrada:
n = 0

Salidas:
Error: invalid input
"""
# Conclusión 
"""
El manejo de bucles en Python es esencial porque permite automatizar tareas repetitivas, 
reducir código redundante y hacer que los programas sean más eficientes y fáciles de mantener.
• 	Eficiencia: Los bucles evitan escribir múltiples líneas de código para operaciones repetitivas, ahorrando tiempo y esfuerzo.
• 	Flexibilidad:
• 	El bucle  es ideal para recorrer colecciones (listas, tuplas, diccionarios, cadenas) y aplicar operaciones a cada elemento.
• 	El bucle  es útil cuando la repetición depende de una condición lógica que puede variar dinámicamente.
• 	Automatización: Permiten procesar grandes volúmenes de datos, generar patrones, validar entradas o 
ejecutar cálculos sin intervención manual.
• 	Escalabilidad: Gracias a los bucles, los programas pueden adaptarse fácilmente a diferentes tamaños de datos o 
escenarios sin necesidad de modificar la lógica principal.
• 	Base de algoritmos: Son la piedra angular de estructuras más complejas como búsquedas, ordenamientos, 
simulaciones y algoritmos matemáticos.
"""

# Referencias
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