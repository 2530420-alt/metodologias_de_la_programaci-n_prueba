# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2
"""
   Una lista es una colección ordenada y mutable (modificable) de elementos, definida con corchetes []. 
   Una tupla es una colección ordenada pero inmutable (no modificable) de elementos, definida con paréntesis (). 
   Un diccionario es una colección de pares clave-valor no ordenada y mutable, que usa llaves {} para almacenar 
   y recuperar datos de manera eficiente mediante sus claves únicas

   Una lista mutable se puede modificar después de su creación, permitiendo añadir, 
   eliminar o cambiar elementos. Por otro lado, una tupla inmutable no puede ser alterada; 
   una vez que se crea, sus elementos no pueden modificarse ni eliminarse

   Los diccionarios asocian claves con valores al definirlos entre llaves {} con la sintaxis clave: 
   valor, donde cada par se separa con comas. Se accede a los valores usando la clave entre corchetes [clave] o el método {}.get(clave). 
   Para agregar o actualizar un par, se asigna un valor a una clave existente o nueva usando 
   el corchete [clave] = valor, lo que sobrescribe el valor si la clave ya existe
"""
# Problem 1: Shopping list basics (list operations)
"""
   Descripción:
Trabaja con una lista de productos (strings) y sus cantidades (enteros). El programa debe:
1) Crear una lista inicial de productos.
2) Permitir agregar un nuevo producto al final.
3) Mostrar la cantidad total de elementos en la lista.
4) Verificar si un producto específico está en la lista (booleano is_in_list).
"""
initial_items_text = input("Enter products and quantities separated by commas (example: 'apple:3, pear:5'): ").strip()

items = []
if not initial_items_text:
    print("Initial empty list. We will continue with an empty list.")
else:
    raw_items = [x.strip() for x in initial_items_text.split(",") if x.strip()]
    for element in raw_items:
        if ":" in element:
            product, qty = element.split(":", 1)
            product = product.strip()
            try:
                qty = int(qty.strip())
            except ValueError:
                print(f"Invalid amount for '{product}', 0 is assigned.")
                qty = 0
            items.append((product, qty))
        else:
            print(f"Invalid format in '{element}', is ignored.")


new_item = input("Enter new product and quantity (e.g., 'grapes:10'): ").strip()
if not new_item:
    print("Error: New product cannot be empty.")
else:
    if ":" in new_item:
        product, qty = new_item.split(":", 1)
        product = product.strip()
        try:
            qty = int(qty.strip())
        except ValueError:
            print(f"Invalid amount for '{product}', 0 is assigned.")
            qty = 0
        items.append((product, qty))
    else:
        print("Invalid format for new product. Must be 'name:quantity'.")

total_items = len(items)

search_item = input("Enter product to search for: ").strip()
if not search_item:
    print("Error: The product to search for cannot be empty.")
    is_in_list = False
else:
    is_in_list = any(product == search_item for product, qty in items)

print("Items list:", items)
print("Total items:", total_items)
print("Found item:", str(is_in_list).lower())

"""
inputs:
- initial_items_text (string; por ejemplo, "apple,banana,orange").
- new_item (string; producto a agregar).
- search_item (string; producto a buscar).

Outputs:
- "Items list:" <items_list>
- "Total items:" <len_list>
- "Found item:" true|false

Validations:
- initial_items_text no vacío tras strip().
- Separar la cadena por comas y eliminar espacios extra en cada elemento.
- new_item y search_item no vacíos.
- Manejar el caso de lista inicial vacía si el estudiante lo decide (documentar decisión).

Entradas de prueba:
1) initial_items_text = "apple:3, banana:2, orange:5"
    new_item = "grapes:10"
    search_item = "banana"
    Salidas esperadas:
    Items list: [('apple', 3), ('banana', 2), ('orange', 5), ('grapes', 10)]
    Total items: 4
    Found item: true
2) initial_items_text = "  "
    new_item = "kiwi:4"
    search_item = "mango"
    Salidas esperadas:
    Initial empty list. We will continue with an empty list.
    Items list: [('kiwi', 4)]
    Total items: 1
    Found item: false
3) initial_items_text = "milk:2, bread:1, eggs:12"
    new_item = ""   
    search_item = "bread"
    Salidas esperadas:
    Error: New product cannot be empty.
    Items list: [('milk', 2), ('bread', 1), ('eggs', 12)]
    Total items: 3
    Found item: true
"""
# Probblem 2 Points and distances with tuples
"""
Descripción:
Usa tuplas para representar dos puntos en un plano 2D: (x1, y1) y (x2, y2). El programa debe:
1) Crear dos tuplas point_a y point_b a partir de entradas numéricas.
2) Calcular la distancia euclidiana entre ambos puntos.
3) Crear una nueva tupla midpoint con el punto medio entre ellos.
Validaciones:
- Verificar que las 4 entradas se puedan convertir a float.
- No se requieren restricciones adicionales en el rango.
Salidas:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)
"""

try:
    x1 = float(input("Enter x1: "))
    y1 = float(input("Enter y1: "))
    x2 = float(input("Enter x2: "))
    y2 = float(input("Enter y2: "))


    point_a = (x1, y1)
    point_b = (x2, y2)


    distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5

    
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

  
    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)

except ValueError:
    print("Error: All inputs must be convertible to float.")

"""
Inputs:
- x1, y1, x2, y2 (float; coordenadas de los puntos).

Outputs:
- "Point A:" (x1, y1)
- "Point B:" (x2, y2)
- "Distance:" <distance>
- "Midpoint:" (mx, my)

Entradas de prueba:
Entrada:
x1 = 1
y1 = 2
x2 = 4
y2 = 6

Salidas:
Point A: (1.0, 2.0)
Point B: (4.0, 6.0)
Distance: 5.0
Midpoint: (2.5, 4.0)

Entrada:
x1 = 0
y1 = 0
x2 = 0
y2 = 0

Salidas:
Point A: (0.0, 0.0)
Point B: (0.0, 0.0)
Distance: 0.0
Midpoint: (0.0, 0.0)

Entrada:
x1 = a
y1 = 2
x2 = 4
y2 = 6

Salidas:
Error: All inputs must be convertible to float.
"""
# problem 3 Product catalog with dictionary
"""
Descripción:
Administra un pequeño catálogo de productos usando un diccionario donde:
- clave: nombre del producto (string)
- valor: precio unitario (float)
El programa debe:
1) Crear un diccionario inicial con al menos 3 productos.
2) Leer el nombre de un producto y la cantidad a comprar.
3) Calcular el total a pagar si el producto existe.
4) Si el producto no existe, mostrar un mensaje de error.
Validaciones:
- quantity > 0.
- product_name no vacío tras strip().
- Verificar si product_name está en el diccionario (clave).
Salidas:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"
"""

catalog = {
    "apple": 0.5,
    "banana": 0.3,
    "orange": 0.7
}

try:
    
    product_name = input("Enter product name: ").strip()
    quantity = int(input("Enter quantity: "))

    
    if not product_name:
        print("Error: product name cannot be empty")
    elif quantity <= 0:
        print("Error: quantity must be greater than 0")
    elif product_name in catalog:
        unit_price = catalog[product_name]
        total_price = unit_price * quantity

        
        print("Unit price:", unit_price)
        print("Quantity:", quantity)
        print("Total:", total_price)
    else:
        print("Error: product not found")

except ValueError:
    print("Error: quantity must be an integer")
"""
Inputs:
- product_name (string).
- quantity (int; cantidad a comprar).

Outputs:
- Si el producto existe:
  - "Unit price:" <unit_price>
  - "Quantity:" <quantity>
  - "Total:" <total_price>
- Si el producto no existe:
  - "Error: product not found"

Entradas de prueba:
Entrada:
product_name = "apple"
quantity = 4

Salidas:
Unit price: 0.5
Quantity: 4
Total: 2.0

Entrada:
product_name = " banana " 
quantity = 1

Salidas:
Unit price: 0.3
Quantity: 1
Total: 0.3

Entrada:
product_name = "grape"
quantity = 2

Salidas:
Error: product not found
"""
# Problem 4 Student grades with dict and list
"""
Descripción:
Administra las calificaciones de un grupo usando un diccionario:
- clave: nombre del estudiante (string)
- valor: lista de calificaciones (list of float)
El programa debe:
1) Crear un diccionario con al menos 3 estudiantes, cada uno con una lista de calificaciones.
2) Leer el nombre de un estudiante.
3) Calcular el promedio de sus calificaciones.
4) Indicar si el estudiante está aprobado (average >= 70.0) con un booleano is_passed.
Validaciones:
- student_name no vacío tras strip().
- Verificar si student_name es una clave en el diccionario.
- Verificar que la lista de calificaciones no esté vacía antes de calcular el promedio.
Salidas:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"
"""

students = {
    "Alice": [85.0, 90.0, 78.0],
    "Bob": [60.0, 72.0, 68.0],
    "Charlie": [95.0, 88.0, 92.0]
}


student_name = input("Enter student name: ").strip()


if not student_name:
    print("Error: student name cannot be empty")
elif student_name not in students:
    print("Error: student not found")
else:
    grades = students[student_name]
    if not grades:
        print("Error: no grades available for this student")
    else:
        average = sum(grades) / len(grades)
        is_passed = average >= 70.0

       
        print("Grades:", grades)
        print("Average:", average)
        print("Passed:", str(is_passed).lower())
"""
Inputs:
- student_name (string)

Outputs:
- Si el estudiante existe:
  - "Grades:" <grades_list>
  - "Average:" <average>
  - "Passed:" true|false
- Si el estudiante no existe:
  - "Error: student not found"

Entradas de prueba:
Entrada:
student_name = "Alice"

Salidas:
Grades: [85.0, 90.0, 78.0]
Average: 84.33333333333333
Passed: true

Entrada:
student_name = "Bob"

Salidas:
Grades: [60.0, 72.0, 68.0]
Average: 66.66666666666667
Passed: false

Entrada:
student_name = "Daniel"

Salidas:
Error: student not found
"""
# Problem 5 Word frequency counter (list + dict)
"""
Descripción:
Cuenta la frecuencia de cada palabra en una oración usando:
- Una lista de palabras.
- Un diccionario donde:
  - clave: palabra (string)
  - valor: frecuencia (int)
El programa debe:
1) Leer una oración.
2) Convertirla a minúsculas y separarla en una lista de palabras.
3) Construir un diccionario de frecuencias.
4) Mostrar el diccionario completo y la palabra más frecuente.
Validaciones:
- sentence no vacía tras strip().
- Manejar signos de puntuación simples si el estudiante decide hacerlo (documentar su decisión, por ejemplo usando replace()).
- Verificar que la lista de palabras no esté vacía.
Salidas:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)
"""

sentence = input("Enter a sentence: ").strip()


if not sentence:
    print("Error: sentence cannot be empty")
else:
    
    sentence = sentence.lower()

    
    sentence = sentence.replace(",", "").replace(".", "")

    
    words_list = sentence.split()

    if not words_list:
        print("Error: words list is empty")
    else:
        
        freq_dict = {}
        for word in words_list:
            if word in freq_dict:
                freq_dict[word] += 1
            else:
                freq_dict[word] = 1

      
        most_common_word = max(freq_dict, key=freq_dict.get)

       
        print("Words list:", words_list)
        print("Frequencies:", freq_dict)
        print("Most common word:", most_common_word)

"""
Inputs:
- sentence (string)

Outputs:
- "Words list:" <words_list>
- "Frequencies:" <freq_dict>
- "Most common word:" <word> (si hay empate, cualquier una es válida)

Entradas de prueba:
Entrada:
sentence = "The cat and the dog."

Salidas:
Words list: ['the', 'cat', 'and', 'the', 'dog']
Frequencies: {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
Most common word: the

Entrada:
sentence = "Hello"

Salidas:
Words list: ['hello']
Frequencies: {'hello': 1}
Most common word: hello

Entrada:
sentence = "" 

Salidas:
Error: sentence cannot be empty
"""
# Problem 6 Simple contact book (dictionary CRUD)
"""
Descripción:
Implementa un mini "contact book" usando un diccionario donde:
- clave: nombre de contacto (string)
- valor: número de teléfono (string)
El programa debe:
1) Crear un diccionario inicial con algunos contactos.
2) Leer una acción action_text ("ADD", "SEARCH" o "DELETE").
3) Según la acción:
   - "ADD": lee name y phone, agrega o actualiza el contacto.
   - "SEARCH": lee name y muestra el teléfono si existe.
   - "DELETE": lee name y elimina el contacto si existe.
4) Mostrar un mensaje indicando el resultado de la operación.
Validaciones:
- Normalizar action_text a mayúsculas.
- Verificar que action_text sea una de las tres opciones válidas.
- name no vacío tras strip().
- Para "ADD": phone no vacío tras strip().
Salidas:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"
"""

contacts = {
    "Alice": "123-456-7890",
    "Bob": "987-654-3210",
    "Charlie": "555-555-5555"
}


action_text = input("Enter action (ADD, SEARCH, DELETE): ").strip().upper()


if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    
    name = input("Enter contact name: ").strip()
    if not name:
        print("Error: name cannot be empty")
    else:
        if action_text == "ADD":
            phone = input("Enter phone number: ").strip()
            if not phone:
                print("Error: phone cannot be empty")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                del contacts[name]
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")
"""
Inputs:
- action_text (string; "ADD", "SEARCH" o "DELETE").
- name (string; depende de la acción).
- phone (string; solo para "ADD")

Outputs:
- Para "ADD":
  - "Contact saved:" name, phone
- Para "SEARCH":
  - Si existe: "Phone:" <phone>
  - Si no existe: "Error: contact not found"
- Para "DELETE":
  - Si existe: "Contact deleted:" name
  - Si no existe: "Error: contact not found"

Entradas de pruebas:
Entrada:
action_text = "ADD"
name = "David"
phone = "111-222-3333"

Salidas:
Contact saved: David 111-222-3333

Entrada:
action_text = "SEARCH"
name = " Alice "

Salidas:
Phone: 123-456-7890

Entrada:
action_text = "UPDATE"

Salidas:
Error: invalid action
"""
# Conclusión
"""
El dominio de listas, tuplas y diccionarios en Python es esencial porque representan 
las estructuras de datos más utilizadas para organizar, almacenar y manipular información de manera eficiente.
• 	Listas (): Permiten manejar colecciones dinámicas y ordenadas de elementos, ideales para datos que cambian con frecuencia.
• 	Tuplas (): Ofrecen colecciones ordenadas pero inmutables, útiles para garantizar 
que ciertos datos no se modifiquen accidentalmente, aportando seguridad y estabilidad.
• 	Diccionarios (): Facilitan el acceso rápido a valores mediante claves, 
lo que resulta fundamental en aplicaciones que requieren búsquedas eficientes, como catálogos, configuraciones o registros.
En conjunto, estas estructuras permiten:
• 	Representar datos de manera clara y flexible.
• 	Optimizar el rendimiento en operaciones de búsqueda, inserción y actualización.
• 	Construir algoritmos y programas más robustos, escalables y fáciles de mantener.
• 	Resolver problemas reales en áreas como análisis de datos, desarrollo web, inteligencia artificial y automatización.
"""

# Referencias
"""
https://www.w3schools.com/python/python_lists.asp
https://aprendepython.es/core/datastructures/lists/
https://www.w3schools.com/python/python_tuples.asp
https://www.w3schools.com/python/python_dictionaries.asp
"""
# url github
"""
https://github.com/2530420-alt/metodologias_de_la_programaci-n_prueba#
git@github.com:2530420-alt/metodologias_de_la_programaci-n_prueba.git

la neta no sabia cual poner, así que puse los dos
"""