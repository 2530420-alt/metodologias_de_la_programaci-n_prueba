"""
Las listas tambien pueden almacenar numeros y de hecho, es una de las formas mas comunes de utilizar listas en Python.
python ofrece muchas formas de trabajar con listas de numeros, incluyendo funciones integradas que facilitan el analisis de datos numericos.
"""
# Por ejemplo, funcion range() genera una serie de numeros en un rango especifico.
# La funcion range() comienza en 0 de forma predeterminada, y se incrementa en 1, y termina en el numero especificado menos 1.

numbers = list(range(10))
print(numbers)  # Salida: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(type(numbers))  # Salida: <class 'list'>  

# Podemos realizar lo mismo con un for loop
for number in range(10):
    print(number)

print("numeros del 1 al 4")
for num in range(1,5):
    print(num)

print("numeros impares")
for odd_num in range(1, 10, 2):
    print(odd_num)

print("numeros pares")
for even_num in range(2, 11, 2):
    print(even_num)

# Lista del cuadrado de los numeros del 1 al 10
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# metodos bult-in para trabajar con listas de numeros
print("\n Metodos bult-in para trabajar con listas de numeros")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"minimo: {min(digits)}")  # Salida: minimo: 0
print(f"maximo: {max(digits)}")  # Salida: maximo: 9
print(f"suma: {sum(digits)}")    # Salida: suma: 45 

squares = [num**2 for num in range(11)]
print(squares)