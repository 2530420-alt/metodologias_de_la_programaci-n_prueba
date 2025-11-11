magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']
print(magicians[0], magicians[1], magicians[2], magicians[3])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print("\n")
    print(f"{magician.title()}, ese fue un gran hechizo!")
    print("\n")

print("Gracias a todos, fue un gran espectáculo!")

"""
   Identacion:

       Python utiliza la identacion para determinar cuando una linea de codigo esta conectada
       a la linea anterior. La identacion es un espacio en blanco al comienzo de una linea de codigo.

    Basicamente, se utilizan 4 espacios en blanco para obligarnos a escribir codigo ordenado y estructurado.

"""

# No olvidemos identar (donde se necesita)
# Ejemolo
magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']
for magician in magicians:
# print(magician)  # Esto causara un error de identacion
    print(magician)  # Esto esta correctamente identado

# Identation error
magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']
for magician in magicians:
    print(magician)
#print(f"Gracias a {magician}, fue un gran espectáculo!") esto es una error
    print(f"Gracias {magician}, fue un gran espectáculo!")


# Identacion Innecesaria


# Logical error
magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']
for magician in magicians:
    print(magician)
    print(f"Gracias {magician}, fue un gran espectáculo!")
print("Gracias a todos, fue un gran espectáculo!")  # Esto no debe estar identado

# Error de sintaxis
magicians = ['ron', 'harry', 'hermione', 'snape', 'draco']
for magician in magicians:
    print(magician)
    