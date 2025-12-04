"""

"""

try:
    age = int(input("por favor ingresa tu edad: "))
    
except:
    age = -1
    print("tuviste un error al ingresar tu edad")

if age > 100:
    print("Eres mayor de edad")
elif age >= 18 and age <= 100:
    print("eres menor de edad")
elif age < 18 and age >= 0:
    print("eres menor de edad")
else:
    print("edad invalida")

print("hola charly")

"""
   hacer un programa que pregunte la edad de una persona y respenda lo siguiente:
   - Si la edad es menor o igual a 4, estonces la entrada es gratis
    - Si la edad es mayor a 4 pero menor o igual a 18, entonces la entrada cuesta $200
    - Si la edad es mayor a 18, entonces la entrada cuesta $400
"""

# multiple if
guisos = ["deshebrada", "asado", "salsa verde", "pozole"]
if "asado" in guisos:
    print("si tenemos asado")
else:
    print("no tenemos asado")
if "tamales" in guisos:
    print("si tenemos tamales")
else:
    print("no tenemos tamales")
if "deshebrada" in guisos:
    print("si tenemos deshebrada")
else:
    print("no tenemos deshebrada")

age = int(input("por favor ingresa tu edad: "))
if age <= 4:
    print("la entrada es gratis")
elif age > 4 and age <= 18:
    print("la entrada cuesta $200") 
elif age > 18:
    print("la entrada cuesta $400")