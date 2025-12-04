"""
   Docstring for understanding_while_loop module.
    Este modulo explica el uso del while loop en Python.

   utilizamos while loops para ejecutar un bloque de codigo
   mientras una condicion sea verdadera.

   estructura basica de un while loop:
    while condicion:
         bloque de codigo



"""
# ejemplo basico con un while
# verificar si un numero esta en un rango determinado(entre 10 y 20)
while True: #bucle infinito
    try:
         
         number = input("Ingresa un numero entre 10 y 20: ")
         number = int(number)
         if 10 <= number <= 20:
             print("Gracias! Has ingresado un numero valido.")
             break  # salir del bucle
         else:
             print("Numero invalido. Intenta de nuevo.")
    except ValueError:
         print("Entrada invalida. Por favor ingresa un numero entero.")
    except KeyboardInterrupt:
        print("\nProceso interrumpido por el usuario.")
        break
print("saliste del while yupi")wr