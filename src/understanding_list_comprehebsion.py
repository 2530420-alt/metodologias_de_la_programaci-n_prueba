# list comprehensions
"""
   Una lista comprenhension combina el for loop
   en una sola linea de codigo y tambien, automaticamente
   agraga el nuevo elemento a la lista, es decir, sin utilizar el append
"""

squares = [num**2 for num in range(11)]
print(squares)

even_numbers_0_100 = list(range(0,101,2))
print(even_numbers_0_100)

# numeros pares utilizando list comprehension
even_list_compre = [value for value in range(0,101) if value%2 == 0]
print(even_list_compre)
