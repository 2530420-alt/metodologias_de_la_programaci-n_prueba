# SLICING
players = ["cr7","messi","travis","chicharito","michael"]
print(players[0:3])
# Slice es trabajar con un grupo especifico de datos de una lista
print(players[1:4])
print(players[:4])
print(players[2:])

print(players[-3:])

print(players[-3:-1])

# Slicing en for
players = ["cr7","messi","travis","chicharito","michael"]
first_three_players = players[0:3]
print("first three players:", first_three_players)


print("Aqui vienen los tres mejores del salon:")
for player in players[0:3]:
    print(player.upper())

# Copia de listas
my_food = ["pizza","gorditas de jaumave","machacado"]
# copy_of_food = my_food manera erronea de copiar una lista
copy_of_food_1 = my_food[:]
copy_of_food_2 = my_food.copy()
copy_of_food_3 = list(my_food)

# modificndo elementos
cars = ["bwm", "porch", "masda", "totoya", "ford"]
cars[0]= "bmw"
cars[1]= "porshe"
cars[2]= "mazda"
cars[3]= "toyota"