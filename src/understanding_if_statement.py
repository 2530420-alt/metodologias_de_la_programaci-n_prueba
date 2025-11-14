cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())


# El condicional es el corazon de un if
# condicional true
car = "bmw"
print(car == "bmw")  # True

# condicional false
car = "audi"    
print(car == "bmw")  # False

# posible solucion a entradas del usuario
car = "Audi"
print(car.lower() == "audi")  # True

# Operador relacional != para determinar desigualdad
requested_topping = "mushrooms"
if requested_topping != "anchovies":
    print("Hold the anchovies!")

# Comparaciones numericas
age = 18 # entero
print(age == 18)  # True

answer = 17
if answer != 42:
    print("esa no es la respuesta correcta. Intenta de nuevo!")

Age = 20
print(Age < 21)  # True
print(Age <= 21)  # True
print(Age > 21)  # False
print(Age >= 21)  # False

# Multiples condiciones
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) # False
print(age_0 >= 21 or age_1 >= 18) # True

# Operacion or
print(age_0 >= 21 or age_1 >= 21)  # True
print(age_0 >= 23 or age_1 >= 21)  # False

"""
   Para verificar si un valor se encuentra en una lista, utilizamos la palabra reservada in
"""
motorcycles = ["honda", "yamaha", "suzuki", "ducati"]
moto_charly_wants = "ducati"
print(moto_charly_wants in motorcycles)  # True}
moto_charly_wants = "italica"
print(moto_charly_wants in motorcycles)  # False

"""
    Para verificar si un valor no se encuentra en una lista, utilizamos la palabra reservada not in
"""

banned_users = ["Jorge", "Carlos", "Moyra", "Luz", "hots"]
user = "Ana"
print(user not in banned_users)  # True
print("Jorge" not in banned_users)  # False

# Booleanos
game_active = True
can_edit = False

"""
   if statement

   sintaxis:
    if condition:
         do something
    
    if condition:
         do something
    else:
         do something else
"""
age = input("\n Cual es tu edad?: ")
print(age)

if int(age) >= 18:
    print("Eres lo suficientemente mayor para votar!")
else:
    print("Lo siento, eres muy joven para votar.")