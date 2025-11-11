# Listas
# Una lista es una coleccion ordenada y mutable de elementos
# Se pueden crear listas utilizando corchetes [] y separando los elementos con comas.
fruits = ["manzana", "banana", "cereza"]
print(fruits) # salida: ['manzana', 'banana', 'cereza']

print(fruits[0].upper()) # salida: manzana
print(fruits[1].title()) # salida: banana
print(fruits[2].lower()) # salida: cereza

# print(fruits[3]) # IndexError: list index out of range    

# Acceder al ultimo elemento de una lista
print(fruits[-1].capitalize()) # salida: Cereza
print(fruits[-2]) # salida: banana
print(fruits[-3]) # salida: manzanas

message = f"Mi fruta favorita es la {fruits[0].title()}"
print(message) # salida: Mi fruta favorita es la Manzana

my_favorite_fruit = fruits[1].title()
print(f"My favorite fruit is {my_favorite_fruit}") # salida: My favorite fruit is Banana

"""
   Agregar elementos a una lista
   append(): agrega un elemento al final de la lista
   el metodo append() toma un solo argumento: el elemento que se va a agregar a la lista
"""
print("\n Agregar elementos a una lista; metodod append() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
motorcycles.append("ducati")
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki', 'ducati']

"""
   Agregar elementos a una lista
   - insert(): agrega un elemento en una posicion especifica de la lista
   El metodo insert() toma dos argumentos: el indice donde se desea insertar el elemento y el elemento a insertar.
"""
print("\n Agregar elementos a una lista; metodo insert() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, "ducati") 
print(motorcycles) # salida: ['ducati', 'honda', 'yamaha', 'suzuki']
print(motorcycles[0].title()) # salida: Ducati
motorcycles.insert(2, "bmw") 
print(motorcycles) # salida: ['ducati', 'honda', 'bmw

"""
   eliminar elementos de una lista
        - del: elimina un elemento de una lista en una posicion especifica
   La declaracion del toma el indice del elemento que se desea eliminar como argumento.
"""
print("\n Eliminar elementos de una lista; declaracion del \n")
motorcycles = ["honda", "yamaha", "suzuki"]     
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles) # salida: ['honda', 'suzuki']

"""
   Eliminar elementos de una lista
        - pop(): elimina el ultimo elemento de una lista y lo devuelve
   El metodo pop() no requiere argumentos y elimina el ultimo elemento de la lista.
"""

print("\n Eliminar elementos de una lista; metodo pop() \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles) # salida: ['honda', 'yamaha']
print(f"la motocicleta que se elimino es: {popped_motorcycle.title()}") # salida: la motocicleta que se elimino es: Suzuki

"""
   Eliminar elementos de una lista
        - pop(index): elimina un elemento en una posicion especifica y lo devuelve
   El metodo pop(index) toma un argumento: que es el indice del elemento que se desea eliminar y devuelve el elemento eliminado.
"""
print("\n Eliminar elementos de una lista; metodo pop(index) \n")
motorcycles = ["honda", "yamaha", "suzuki"]
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki']
first_motorcycle = motorcycles.pop(0)  
print(motorcycles) # salida: ['yamaha', 'suzuki']
print(f"La primera motocicleta que tuve fue una {first_motorcycle.title()}") # salida: La primera motocicleta que tuve fue una Honda

"""
   Eliminar elementos de una lista
        - remove(): elimina la primera aparicion de un valor especifico en una lista
   El metodo remove(value) toma un argumento: que es el valor del elemento que se desea eliminar
"""
print("\n Eliminar elementos de una lista; metodo remove() \n")
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
print(motorcycles) # salida: ['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove("yamaha")  
print(motorcycles) # salida: ['honda', 'suzuki', 'ducati']

names = ["Alice", "Bob", "Charlie", "Diana", "christina"]
print(names) # salida: ('Alice', 'Bob', 'Charlie', 'Diana', 'christina')
deleted_name = input("\nIngrese el nombre que desea eliminar de la lista: ")
names.remove(deleted_name)
print(names)

"""
   
   Ordenar listas

   metodo de listas sort(): ordena una lista de forma permanente en orden alfabetico

"""
cars = ["bmw", "audi", "toyota", "subaru"]
cars.sort()
print(cars) # salida: ['audi', 'bmw', 'subaru', 'toyota']   

"""
   Metodo reverse
"""

motorcycles = ["Mortalica", "Honda", "ducati"]
print(motorcycles)
motorcycles.reverse()
print(motorcycles)

"""
   Cantidad de elementos en una lista
   len(): devuelve la cantidad de elementos en una lista
"""

cars = ["bmw", "audi", "toyota", "subaru"]
print("\n Metodo built-in len()")
print(len(cars)) # salida: 4

"""
   Metodo built-in 
   sorted(): Ordena una lista temporalmente sin modificar la lista original
"""

favorite_students = ["Carlos", "Jose", "Emiliano", "Jorge"]
print(favorite_students) # salida: ['Carlos', 'Jose', 'Emiliano', 'Jorge']
print(sorted(favorite_students)) # salida: ['Carlos', 'Emiliano', 'Jorge', 'Jose']


   