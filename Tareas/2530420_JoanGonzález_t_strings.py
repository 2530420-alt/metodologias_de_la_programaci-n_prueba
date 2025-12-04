# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2

"""
Un string (o cadena de caracteres) en Python es un tipo de dato que representa texto. 
Se define entre comillas simples ('...'), dobles ("..."), o triples ('''...''' o """ """) para cadenas multilínea.
- Los strings en Python son inmutables, lo que significa que no se pueden modificar directamente después de ser creados.
- Si intentas cambiar un carácter dentro de un string, obtendrás un error
- Puedes realizar diversas operaciones con strings, como concatenación, repetición, y acceso a caracteres individuales mediante índices.
- Python ofrece una amplia gama de métodos integrados para manipular strings, como .upper(), .lower(), .strip(), .replace(), entre otros.

Algunas operaciones básicas que se pueden realizar con strings en Python incluyen:
1. Concatenación: Unir dos o más strings usando el operador +.
    ejemplo: saludo = "Hola, " + "mundo!"
2. Obtener longitud: Usar la función len() para obtener el número de caracteres en un string.
    ejemplo: longitud = len(saludo)
3. Extraer sub-cadenas: Usar slicing para obtener una parte específica de un string.
    ejemplo: subcadena = saludo[0:4]  # Obtiene "Hola"
4. Buscar patrones: Usar el método .find() o expresiones regulares para buscar sub-cadenas dentro de un string.
    ejemplo: posicion = saludo.find("mundo")  # Devuelve la posición donde comienza "mundo"
5. Reemplazar texto: Usar el método .replace() para sustituir partes de un string por otras.
    ejemplo: nuevo_saludo = saludo.replace("mundo", "Python")  # Devuelve "Hola, Python!"

Validar y normalizar texto de entrada es crucial por varias razones:
1. Seguridad: La validación ayuda a prevenir ataques como inyección de código, asegurando que los datos ingresados sean seguros y no contengan elementos maliciosos.
2. Consistencia: La normalización garantiza que los datos se almacenen en un formato uniforme, facilitando su procesamiento y análisis posterior.
3. Experiencia del usuario: Validar entradas como correos electrónicos y contraseñas asegura que los usuarios proporcionen información correcta y útil, mejorando la interacción con la aplicación.
4. Evitar errores: La validación ayuda a detectar y corregir errores en la entrada de datos antes de que causen problemas en el sistema.
5. Cumplimiento de normas: En muchos casos, existen regulaciones que requieren la validación y normalización de ciertos tipos de datos, como información personal o financiera.
"""

# Problema 1: Full Name Formatter (name + initials)
""" 
    Este codigo solicita al usuario que ingrese su nombre completo (primer nombre, segundo nombre y apellido) 
    y luego valida que cada parte del nombre tenga al menos 2 caracteres.
"""
full_name = input("Enter your full name: ").strip()
name_parts = full_name.split()
if len(full_name) == 0 and len(name_parts) < 1 :
    print("Error: please enter your full name.")
elif len(name_parts[0]) < 2:
    print("Error: the first name must have at least 2 characters.")
elif len(name_parts[1]) < 2:
    print("Error: the second name must have at least 2 characters.")
elif len(name_parts[2]) < 2:
    print("Error: the last name must have at least 2 characters.")
elif len(name_parts) == 2:
    first_name = name_parts[0].title()
    last_name = name_parts[1].title()
    initial1 = first_name[0].upper()
    initial2 = last_name[0].upper()
    formatted_name = f"{first_name} {last_name}, {initial1},{initial2}."
    print("Formatted Name:", formatted_name)
else:
    first_name = name_parts[0].title()
    second_name = name_parts[1].title()
    last_name = name_parts[2].title()
    initial1 = first_name[0].upper()
    initial2 = second_name[0].upper()
    initial3 = last_name[0].upper()
    formatted_name = f"{first_name} {second_name} {last_name}, {initial1},{initial2},{initial3}."
    print("Formatted Name:", formatted_name)

"""
Inputs:
full_name

Outputs:
Formatted Name or Error message

validations:
1. Check if the input is empty.
2. Check if each part of the name has at least 2 characters.

Entradas de prueba
Input: Joan Orlando Gonzalez
Output: Joan Orlando Gonzalez, J,O,G.
Input: Ana Maria Lopez
Output: Ana Maria Lopez, A,M,L.
Input: Luis Perez
Output: Luis Perez, L,P.
Input: A B C
Output: Error: the first name must have at least 2 characters.
"""
# Problem 2: Simple email validator (structure + domain)
"""
   Valida si una dirección de correo tiene un formato básico correcto:
    - Contiene exactamente un '@'.
    - Después del '@' debe haber al menos un '.'.
    - No contiene espacios en blanco.
    Si el correo es válido, también muestra el dominio (la parte después de '@').
"""
email = input("Enter your email address: ").strip()
if ' ' in email:
    print("Error: email address should not contain spaces.")
elif email.count('@') != 1:
    print("Error: email address must contain exactly one '@' symbol.")
else:
    local_part, domain_part = email.split('@')
    if '.' not in domain_part:
        print("Error: domain part must contain at least one '.' symbol.")
    else:
        print("Valid email address.")
        print("Domain:", domain_part)

"""
Inputs:
email_text (string).

Outputs:
Valid email address or Error message

validations:
1. Check for spaces in the email.
2. Check for exactly one '@' symbol.
3. Check for at least one '.' in the domain part.

Entradas de prueba:
Input: orlandowert4@gmail.com
Output: Valid email address. Domain: gmail.com
Input: jorge@hotmail.com
Output: Valid email address. Domain: hotmail.com
Input: luisyahoo.com
Output: Error: email address must contain exactly one '@' symbol.
Input: maria@@yahoo.com
Output: Error: email address must contain exactly one '@' symbol.
"""
# Problem 3: Palindrome checker (ignoring spaces and case)
"""
   Determina si una frase es un palíndromo, es decir, 
   se lee igual de izquierda a derecha y de derecha a izquierda, 
   ignorando espacios y mayúsculas/minúsculas
"""
phrase = input("Enter a phrase: ").strip()
normalized_phrase = phrase.replace(" ", "").lower()
if normalized_phrase == normalized_phrase[::-1]:
    print("The phrase is a palindrome.")
else:
    print("The phrase is not a palindrome.")

"""
Inputs: 
phrase (string).

Outputs:
Palindrome or Not Palindrome message

validations:
1. Normalize the phrase by removing spaces and converting to lowercase.

Entradas de prueba:
Input: sometemos
Output: The phrase is a palindrome
Input: Ana lava lana
Output: The phrase is a palindrome
Input: Hello World
Output: The phrase is not a palindrome
"""
# Problem 4: Sentence word stats (lengths and first/last word)
"""
   Descripción:
Dada una oración, el programa debe:
1) Normalizar espacios (quitar espacios al principio y al final).
2) Separar las palabras por espacios.
3) Mostrar:
   - Número total de palabras.
   - Primera palabra.
   - Última palabra.
   - Palabra más corta y más larga (por longitud).
"""
sentence = input("Enter a sentence: ").strip()
words = sentence.split()    
if len(words) == 0:
    print("Error: please enter a valid sentence.")
else:
    total_words = len(words)
    first_word = words[0]
    last_word = words[-1]
    shortest_word = min(words, key=len)
    longest_word = max(words, key=len)
    
    print("Total words:", total_words)
    print("First word:", first_word)
    print("Last word:", last_word)
    print("Shortest word:", shortest_word)
    print("Longest word:", longest_word)

"""
Inputs:
sentence (string).

Outputs:
Total words, First word, Last word, Shortest word, Longest word or Error message

validations:
1. Check if the input sentence is empty.

Entradas de prueba:
Input: The quick brown fox jumps over the lazy dog
Output: 
Total words: 9 
First word: The
Last word: dog
Shortest word: The
Longest word: jumps
Input: Hello World
Output:
Total words: 2
First word: Hello
Last word: World
Shortest word: Hello
Longest word: Hello
Input:
Output: Error: please enter a valid sentence.
"""

# Problem 5: Password strength classifier
"""
   Descripción:
Clasifica una contraseña como "weak", "medium" o "strong" según reglas mínimas (puedes afinarlas, pero documéntalas en los comentarios).

Ejemplo de reglas:
- Weak: longitud < 8 o todo en minúsculas o muy simple.
- Medium: longitud >= 8 y mezcla de letras (mayúsculas/minúsculas) o dígitos.
- Strong: longitud >= 8 y contiene al menos:
  - una letra mayúscula,
  - una letra minúscula,
  - un dígito,
  - un símbolo no alfanumérico (por ejemplo, !, @, #, etc.)
"""
password = input("Enter your password: ").strip()
if len(password) < 8:
    print("Password strength: weak")
else:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)
    
    if has_upper and has_lower and has_digit and has_symbol:
        print("Password strength: strong")
    else:
        print("Password strength: medium")
"""
Inputs:
password (string).

Outputs:
Password strength: weak, medium, or strong

validations:
1. Check the length of the password.
2. Check for the presence of uppercase letters, lowercase letters, digits, and symbols.

Entradas de prueba:
Input: password123
Output: Password strength: medium
Input: Passw0rd!
Output: Password strength: strong
Input: 12345
Output: Password strength: weak
Input: weakpass
Output: Password strength: weak
"""
# Problem 6: Product label formatter (fixed-width text)
"""
   Descripción:
Dado el nombre de un producto y su precio, genera una etiqueta en una sola línea con el siguiente formato:

Product: <NAME> | Price: $<PRICE>

La cadena completa debe tener exactamente 30 caracteres:
- Si es más corta, rellena con espacios al final.
- Si es más larga, recorta hasta 30 caracteres.

Validaciones:
- product_name no vacío tras strip().
- price_value debe poder convertirse a un número positivo.
"""
product_name = input("Enter product name: ").strip()
price_input = input("Enter product price: ").strip()
if len(product_name) == 0:
    print("Error: product name cannot be empty.")
else:
    try:
        price_value = float(price_input)
        if price_value < 0:
            print("Error: price must be a positive number.")
        else:
            label = f"Product: {product_name} | Price: ${price_value:.2f}"
            if len(label) < 30:
                label = label.ljust(30)
            else:
                label = label[:30]
            print("Formatted Label:", label)
    except ValueError:
        print("Error: price must be a valid number.")
"""

Inputs:
product_name (string), price_input (string).

Outputs:
Formatted Label or Error message

validations:
1. Check if product_name is empty.
2. Check if price_input can be converted to a positive float.

Entradas de prueba:
Input: Widget, 19.99
Output: Formatted Label: Product: Widget | Price: $19.99
Input: Trapos, 25.5
Output: Formatted Label: Product: Trapos | Price: $25.50
Input: , 10.0
Output: Error: product name cannot be empty.
Input: Gadget, -5
Output: Error: price must be a positive number.
Input: Thingamajig, abc
Output: Error: price must be a valid number.
"""
# Conclusión
"""
El manejo de strings en Python es fundamental porque los textos son uno de los tipos de datos más usados en la programación. 
Desde la interacción con el usuario hasta el procesamiento de archivos y datos en la web, las cadenas de caracteres permiten 
representar, transformar y comunicar información de manera flexible.
• 	Interacción con el usuario: La mayoría de las entradas y salidas en programas se realizan en forma de texto.
• 	Procesamiento de datos: Strings permiten limpiar, dividir, unir y analizar información, 
lo que es esencial en tareas como análisis de datos, procesamiento de lenguaje natural o validación de entradas.
• 	Versatilidad: Python ofrece métodos integrados (, , , , etc.) 
que simplifican operaciones complejas sin necesidad de librerías externas.
• 	Integración: El manejo de strings es clave para trabajar con formatos comunes (JSON, CSV, HTML) y 
para la comunicación entre sistemas.
• 	Robustez: Validar y manipular correctamente cadenas evita errores, mejora la seguridad y 
garantiza que los programas sean confiables.
"""

# Referencias
"""
https://www.w3schools.com/python/python_strings.asp
https://www.tutorialspoint.com/python/python_strings.htm
https://www.programiz.com/python-programming/string
https://realpython.com/python-strings/
https://docs.python.org/3/library/string.html
"""
