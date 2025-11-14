"""
   Las tuplas son listas de elementos que no puede ser cambiados en su tamaño. Las tuplas son listas inmutables.

   Ejemplo:
"""

# Rectangulo (largo, ancho)
rectangle_dimensions = (200, 50)
print("largo del rectangulo:", rectangle_dimensions[0]," mm")
print("ancho del rectangulo:", rectangle_dimensions[1]," mm")

for dimension in rectangle_dimensions:
    print(dimension)

"""
   No podemos modificar los elementos de una tupla, ni tampoco agregar/eliminar nuevos elementos. Lo que si podemos hacer 
   es cambiar la asignacion a una variable que almacena una tupla.
"""
rectangle_dimensions = (300, 150) # Tupla reasignada
print("nuevas dimensiones del rectangulo:")
for dimension in rectangle_dimensions:
    print(dimension)