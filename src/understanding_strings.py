"""
   un string  es de manera sencilla una serie de caracteres.
   En python todo lo que se encuentre dentro de comillas simples '' o dobles comillas "" es considerado un string

          ""esto es un string""
          'esto tambien es un string'

          'le dije a un amigo , "¡python es mi lenguaje favorito!" 
          "el lenguaje 'python' lleva el nombre por Monty python,
          no por la serpiente
"""

name = "clase de programcion"
print(name)
print(name.title())
print(name)


"""

un metodo es una accion que python puede realizar en un fragmento de datos o sobre una variable.

el punto . despues de una variable seguida del metodo title() dice que se tiene que ejecutar el metodo title() de la variable name.

Todos los metodos van seguidos de parentesis porque en ocasiones necesitan informacion adicional para funcionar, lo cual iria dentro 
de los parentesis. 
En esta ocasion el metodo .title() no requiere informacion adicional para ejecutarse

"""

print(name.upper())
print(name.lower())




# concatenacion de strings
print("concatenacion de strings")
first_name = "charly"
last_name = "mercury"
full_name = first_name + " " + last_name
print(full_name)

print("Hola" + full_name.title() + "¡")

# concatenacion convencional
famous_person = "charly mercury"
quote = "python is love"

message = famous_person + "una vez dijo" + quote 
print(message)

# concatenacion con f-strings
message_f_strings = f"{famous_person} una vez dijo {quote}"
print(message_f_strings)

# actividad
"""
    1) elige un personaje famsoso e igualalo a una varibla del tipo string
    2) elige una frase famosa que haya dicho e iguala a una variable del tipo string
    3) genera un mensaje con las dos variables utilizando f-string
    4) inmprime el mensaje

"""

famous_person1 = "Neil armstrong"
quote1 = "un pequeño paso para el hombre, un gran salto para la humanidad"

message_f_strings = + f"{famous_person1} una vez dijo {quote1}"
print(message_f_strings)

# whitespaces
"""
whitespaces se refiere a cualquier caracter que no se imprime, es decir, un tabulador y finales de linea. Los whitespaces se 
utilizan comunmente para organizar las salidas(prints) de tal manera que sea mas amigable de leer o ver para los usuarios.
"""

# ejemplo
print("python")
print("\tPython") # tabulador
print("\t\tPython") # tabulador

# ejemplos salto de linea
print("languages: \n Python \n C \n Javascript")
print("carlos")
print("Tovar")

message = """
  
    Esta clase es de programación

    los alumnos son buena onda

                               Metodologias de la programación
"""
print(message)

# eliminacion de espacios en blanco
programming_languages = " Python "
print(programming_languages)
print(programming_language.lstrip())
print(programming_language.rstrip())
print(programming_language.strip())