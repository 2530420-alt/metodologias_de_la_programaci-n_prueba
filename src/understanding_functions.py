"""
   functions 
   Las funciones son bloques de codigo diseñados 
   para realizar una tarea especifico 

   cuando queremos realizar la tarea que se ha definido
   en una funcion, tenemos que llamar el nombre de
   la funcion responsable de esto.

   definicion es una funcion (Syntax)
   
   def name_of_functions(parameters)
        actions
"""
def greet_mauro():
    print("hola mauro, que gusto verte!!!")

def greet(username, msj):
    print(f"Hola", (username), (msj),"!!!")


# Argumentos
# greet_mauro()
# greet("Joan", "se te pegaron las cobijas")

"""
   vamos a realizar un programa que genere 
   el nombre completo de una persona

   Vamos a pasarle primer nombre, el segundo
   y el apellido

   La funcion debe generar el nombre completo
   y regresarlo
"""

def create_full_name(first_name,middle_name,Last_name):
    """
       Docstrings - Jorge this function creates the fullname
       of a person given its three names
    """
    full_name = f"{first_name} {middle_name} {Last_name}"
    return full_name.title()

user_first_name = input("escribe tu primer nombre: ").strip().lower()
user_middle_name = input("escribe tu segundo nombre: ").strip().lower()
user_Last_name = input("escribe tus apellidos: ").strip().lower()

# Argumentos posicionales -> positional Arguments
print(create_full_name(user_first_name,user_middle_name,user_Last_name))


# Argumentos clave -> Keyword Arguments
full_name_key = create_full_name(
    first_name=user_first_name,
    Last_name=user_middle_name,
    middle_name=user_Last_name
)
print(full_name_key)


# Parametros opcionales -> optional parameters


# Temas para estudiar a futuro
# args, kwargs
# abrir archivos csv, json, ymi, txt, xmi
# - sys
# cli 
# generadores, iteradores, yield
# testing -> 