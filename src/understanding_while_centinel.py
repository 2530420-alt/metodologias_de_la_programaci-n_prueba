"""
   vamos a realizar un programa que sume numeros hasta que el usuario escribe la palabra "salir"

   El programa tambien debe decirme cuantos numeros ingreso el usuario, cual fue el minimo y cual fue el maximo.
"""
sum_of_numbers = 0.0
counter = 0
minimum = None
maximum = None

while True:
    print("Ingresa 'salir' para terminar el programa.")
    user_input = input("Ingresa un numero para sumar: ")

    # centinal
    if user_input == 'salir':
        break

    try:
        quantity = float(user_input)
    except ValueError:
        print("Entrada invalida. Por favor ingresa un numero valido.")
        continue
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break
    
    counter += 1 # counter = counter +1 # estructura de conteo
    sum_of_numbers += quantity # sum_of_numbers = sum_of_numbers + quantity # estructura de acumulacion

    if minimum is None or quantity < minimum:
        minimum = quantity
    
    if maximum is None or quantity > maximum:
        maximum = quantity

print("Sum ", sum_of_numbers)
print("counter", counter)
print("minimum", minimum)
print("maximum", maximum)