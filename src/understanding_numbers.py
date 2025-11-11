# numbers

"""
    Intengers - enteros

    son numeros sin punto decimal,
    -infty, ..., -2, -1, 0, 1, 2,....,infty


    Ejemplo:
        


        # Tipado dinámico
        age = 23

    los podemos sumar (+) ,restar(-), multiplicar (*) y dividir(/).

    potencias (**2,**3, )

    modulo (dividendo%divisor)

"""

number_1 = 30
number_2 = 10

suma = number_1+number_2
difference= number_1-number_2
multiplication= number_1*number_2
division= number_1/number_2
modulo= number_1%number_2
power= number_1**2

print("suma: ", suma)
print("difference: ", difference)
print("multiplication: ", multiplication)
print("division: ", division)
print("modulo: ", modulo)
print("power: ", power)

print("la suma es del tipo", type(suma))
print("la difference es del tipo: ", type(difference))
print("la multiplication es del tipo: ", type(multiplication))
print("la division es del tipo: ", type(division))
print("el modulo es del tipo: ", type(modulo))
print("la power es del tipo: ", type(power))

### Imprimir la edad de alguien
age = 33
message = f"charly tiene {age} años"
print(message)

message = "charly tiene " + str(age) + " años."
print(message)