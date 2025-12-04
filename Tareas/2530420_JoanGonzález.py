# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2

"""
Los tipos int y float en Python son tipos de datos numéricos que se utilizan para representar números.
El tipo int se utiliza para representar números enteros, es decir, números sin parte decimal (por ejemplo, -3, 0, 42). 
Por otro lado, el tipo float se utiliza para representar números de punto flotante, que son números que pueden tener una parte decimal (por ejemplo, -3.14, 0.0, 2.718).
La principal diferencia entre int y float radica en la presencia de la parte decimal.

Un booleano es un tipo de dato que puede tener uno de dos valores: True (verdadero) o False (falso).
Los booleanos se obtienen a partir de comparaciones entre valores utilizando 
operadores de comparación como == (igual a), != (diferente de), < (menor que), > (mayor que), <= (menor o igual que) y >= (mayor o igual que).
Por ejemplo, la expresión 5 > 3 evaluará a True, mientras que la expresión 2 == 4 evaluará a False.

Validar rangos y evitar la división entre cero es importante para garantizar la robustez y estabilidad de un programa.
Si un programa intenta dividir un número por cero, se producirá un error de ejecución que puede interrumpir el funcionamiento del programa.
Además, validar rangos ayuda a prevenir errores lógicos y asegura que los datos procesados estén dentro de los límites esperados, 
lo que puede evitar resultados incorrectos o comportamientos inesperados.
"""

# Problem 1: Temperature converter and range flag
"""
   Descripción:
Convierte una temperatura en grados Celsius (float) que ingrese el usuario a Fahrenheit y Kelvin. Además, 
determina un valor booleano is_high_temperature que sea true si la temperatura en 
Celsius es mayor o igual que 30.0 y false en caso contrario.
Validaciones:
- Verificar que temp_c pueda convertirse a float.
- No permitir temperaturas físicas imposibles en Kelvin (por ejemplo, temp_k < 0.0).
"""
def converter_temperature(temp_c_input):
    try:
        # Validar que temp_c pueda convertirse a float
        temp_c = float(temp_c_input)
    except ValueError:
        return "Error: The temperature entered is not a valid number."

    # Convertir a Fahrenheit y Kelvin
    temp_f = (temp_c * 9/5) + 32
    temp_k = temp_c + 273.15

    # Validación de temperatura física imposible
    if temp_k < 0.0:
        return "Error: The entered temperature corresponds to an impossible value in Kelvin (< 0.0)."

    # Determinar si es alta temperatura
    is_high_temperature = temp_c >= 30.0

    # Resultado en formato claro
    return {
        "Celsius": temp_c,
        "Fahrenheit": temp_f,
        "Kelvin": temp_k,
        "is_high_temperature": is_high_temperature
    }


entrada = input("Enter the temperature in °C: ")
resultado = convertir_temperatura(entrada)
print(resultado)



"""
Inputs: 
temp_c (float; temperatura en °C).

Outputs: 
temp_f (float; temperatura en °F), temp_k (float; temperatura en K), is_high_temperature (bool).

validations:
- temp_c debe ser convertible a float.
- temp_k no debe ser menor que 0.0.

Enteradas de prueba:
1. convert_temperature(25.0) -> (77.0, 298.15, False)
2. convert_temperature(30.0) -> (86.0, 303.15, True)
3. convert_temperature(-300.0) -> ValueError    
4. convert_temperature("abc") -> ValueError
"""

# Problem 2: Work hours and overtime payment
"""
   Descripción:
Calcula el pago total semanal de un trabajador. Hasta 40 horas se pagan a hourly_rate (float). 
Las horas extra (> 40) se pagan al 150% de la tarifa normal. Además, genera un booleano has_overtime que indique si el trabajador hizo horas extra.

Validaciones:
- hours_worked >= 0
- hourly_rate > 0
- Si alguno no cumple, mostrar "Error: invalid input".
"""
try:
    # Entrada de usuario
    hours_worked = float(input("Enter the hours worked: "))
    hourly_rate = float(input("Enter the hourly rate: "))

    # Validaciones
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        # Determinar si hay horas extra
        has_overtime = hours_worked > 40

        if has_overtime:
            # Pago normal por 40 horas
            normal_payment = 40 * hourly_rate
            # Pago extra al 150% de la tarifa normal
            extra_hours = hours_worked - 40
            extra_payment = extra_hours * (hourly_rate * 1.5)
            total_payment = normal_payment + extra_payment
        else:
            # Pago sin horas extra
            total_payment = hours_worked * hourly_rate

        # Resultados
        print(f"Total weekly payment: {total_payment}")
        print(f"Were there any overtime hours? {has_overtime}")

except ValueError:
    print("Error: invalid input")

"""
Inputs:
hours_worked (int; horas trabajadas en la semana), hourly_rate (float; tarifa por hora).

Outputs:
- "Regular pay:" <regular_pay>
- "Overtime pay:" <overtime_pay>
- "Total pay:" <total_pay>
- "Has overtime:" true|false

validations:
- hours_worked >= 0
- hourly_rate > 0

Entradas de prueba:
1. calculate_payment(35, 20.0) -> (700.0, False)
2. calculate_payment(45, 20.0) -> (950.0, True)
3. calculate_payment(-5, 20.0) -> "Error: invalid input"    
4. calculate_payment(40, -10.0) -> "Error: invalid input"
""" 
# Problem 3: Discount eligibility with booleans
"""
   Descripción:
Determina si un cliente obtiene un descuento en su compra. La regla es:
- Tiene descuento si:
  - is_student es true OR
  - is_senior es true OR
  - purchase_total >= 1000.0
Calcula también el total a pagar aplicando un 10% de descuento cuando sea elegible.

Validaciones:
- purchase_total >= 0.0
- Normalizar is_student_text e is_senior_text a mayúsculas y convertir a booleanos is_student, is_senior.
- Si el texto no es "YES" ni "NO", mostrar "Error: invalid input".
"""
try:
    # User inputs
    purchase_total = float(input("Enter the purchase total: "))
    is_student_text = input("Is the customer a student? (YES/NO): ").strip().upper()
    is_senior_text = input("Is the customer a senior? (YES/NO): ").strip().upper()

    # Validations
    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        # Convert to booleans
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        # Determine discount eligibility
        has_discount = is_student or is_senior or purchase_total >= 1000.0

        if has_discount:
            total_to_pay = purchase_total * 0.9  # Apply 10% discount
        else:
            total_to_pay = purchase_total

        # Results
        print(f"Eligible for discount?: {has_discount}")
        print(f"Total to pay: {total_to_pay}")

except ValueError:
    print("Error: invalid input")

"""
Inputs:
is_student_text (str; "YES" o "NO"), is_senior_text (str; "YES" o "NO"), purchase_total (float; total de la compra).

Outputs:
- "Has discount:" true|false
- "Total to pay:" <total_to_pay>

validations:
- purchase_total >= 0.0
- is_student_text e is_senior_text deben ser "YES" o "NO".

Entradas de prueba:
1. calculate_discount("YES", "NO", 800.0) -> (True, 720.0)
2. calculate_discount("NO", "YES", 500.0) -> (True, 450.0)
3. calculate_discount("NO", "NO", 1200.0) -> (True, 1080.0)
4. calculate_discount("NO", "NO", 800.0) -> (False, 800.0)
5. calculate_discount("MAYBE", "NO", 800.0) -> "Error: invalid input"
6. calculate_discount("YES", "NO", -100.0) -> "Error: invalid input"
"""

# Problem 4: Basic statistics of three integers
"""
   Descripción:
Lee tres números enteros y calcula: suma, promedio (float), valor máximo, 
valor mínimo y un booleano all_even que indique si los tres números son pares.

Validaciones:
- Verificar que los tres valores se puedan convertir a int.
- No se requieren restricciones adicionales (se permiten negativos).
"""
try:
    # User inputs
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    num3 = int(input("Enter the third integer: "))

    # Calculations
    total_sum = num1 + num2 + num3
    average = total_sum / 3.0
    maximum = max(num1, num2, num3)
    minimum = min(num1, num2, num3)
    all_even = (num1 % 2 == 0) and (num2 % 2 == 0) and (num3 % 2 == 0)

    # Results
    print(f"Sum: {total_sum}")
    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"All numbers even?: {all_even}")

except ValueError:
    print("Error: invalid input")

"""
Inputs:
num1 (int; primer número), num2 (int; segundo número), num3 (int; tercer número).

Outputs:
- "Sum:" <total_sum>
- "Average:" <average>
- "Max:" <maximum>
- "Min:" <minimum>
- "All even:" true|false

validations:
- Todos los valores deben ser convertibles a int.

Entradas de prueba:
1. basic_statistics(2, 4, 6) -> (12, 4.0, 6, 2, True)
2. basic_statistics(1, 3, 5) -> (9, 3.0, 5, 1, False)
3. basic_statistics(-2, 0, 2) -> (0, 0.0, 2, -2, True)
4. basic_statistics("a", 2, 3) -> ValueError
"""

# Problem 5: Loan eligibility (income and debt ratio)
"""
   Descripción:
Determina si una persona es elegible para un préstamo con base en:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)
La regla es:
- debt_ratio = monthly_debt / monthly_income
- eligible es true si:
  - monthly_income >= 8000.0 AND
  - debt_ratio <= 0.4 AND
  - credit_score >= 650

Validaciones:
- monthly_income > 0.0 (evitar división entre cero).
- monthly_debt >= 0.0
- credit_score >= 0
- Si no se cumple, mostrar "Error: invalid input".
"""
try:
    # User inputs
    monthly_income = float(input("Enter monthly income: "))
    monthly_debt = float(input("Enter monthly debt: "))
    credit_score = int(input("Enter credit score: "))

    # Validations
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        # Calculate debt ratio
        debt_ratio = monthly_debt / monthly_income

        # Determine eligibility
        eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)

        # Results
        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible for loan?: {eligible}")

except ValueError:
    print("Error: invalid input")

"""
Inputs:
monthly_income (float; ingreso mensual), monthly_debt (float; deuda mensual), credit_score (int; puntaje de crédito).

Outputs:
- "Eligible:" true|false
- debt_ratio (float; ratio de deuda).

validations:
- monthly_income > 0.0
- monthly_debt >= 0.0
- credit_score >= 0

Entradas de prueba:
1. check_loan_eligibility(9000.0, 3000.0, 700) -> (True)
2. check_loan_eligibility(7000.0, 2000.0, 700) -> (False)
3. check_loan_eligibility(9000.0, 4000.0, 600) -> (False)
4. check_loan_eligibility(0.0, 2000.0, 700) -> "Error: invalid input"
5. check_loan_eligibility(9000.0, -100.0, 700) -> "Error: invalid input"
6. check_loan_eligibility(9000.0, 2000.0, -50) -> "Error: invalid input"
"""

# Problem 6: Body Mass Index (BMI) and category flag
"""
   Descripción:
Calcula el índice de masa corporal (BMI) de una persona con la fórmula:
- bmi = weight_kg / (height_m * height_m)
Además, genera booleanos para indicar:
- is_underweight (bmi < 18.5)
- is_normal (18.5 <= bmi < 25.0)
- is_overweight (bmi >= 25.0)

Validaciones:
- weight_kg > 0.0
- height_m > 0.0
- Si no se cumple, mostrar "Error: invalid input".
""" 
try:
    # User inputs
    weight_kg = float(input("Enter weight in kilograms: "))
    height_m = float(input("Enter height in meters: "))

    # Validations
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        # BMI calculation
        bmi = weight_kg / (height_m * height_m)

        # Boolean flags
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0

        # Results
        print(f"BMI: {bmi}")
        print(f"Underweight?: {is_underweight}")
        print(f"Normal?: {is_normal}")
        print(f"Overweight?: {is_overweight}")

except ValueError:
    print("Error: invalid input")
"""
Inputs:
weight_kg (float; peso en kg), height_m (float; altura en m).

Outputs:
- "BMI:" <bmi>
- "Is underweight:" true|false
- "Is normal:" true|false
- "Is overweight:" true|false

validations:
- weight_kg > 0.0
- height_m > 0.0

Entradas de prueba:
1. calculate_bmi(60.0, 1.7) -> (20.76, False, True, False)
2. calculate_bmi(50.0, 1.8) -> (15.43, True, False, False)
3. calculate_bmi(80.0, 1.6) -> (31.25, False, False, True)
4. calculate_bmi(-70.0, 1.7) -> "Error: invalid input"
5. calculate_bmi(70.0, 0.0) -> "Error: invalid input"
"""

# Conclusión
"""
El manejo de números en Python es esencial porque constituye la base de casi cualquier aplicación que requiera cálculos, 
mediciones o análisis de datos. Los tipos numéricos ( y ) permiten representar cantidades discretas y continuas de 
manera precisa y flexible.
• 	Cálculos básicos y avanzados: Desde operaciones aritméticas simples hasta algoritmos matemáticos complejos, 
los números son indispensables.
• 	Modelado de datos reales: Los enteros representan conteos exactos (ej. cantidad de productos), 
mientras que los flotantes permiten trabajar con valores aproximados o continuos (ej. precios, medidas científicas).
• 	Automatización y simulación: Muchas aplicaciones industriales, financieras y científicas dependen de cálculos numéricos 
para simular escenarios y tomar decisiones.
• 	Interoperabilidad: Python facilita la integración de números con librerías especializadas (NumPy, Pandas, SciPy), 
ampliando su uso en análisis de datos, inteligencia artificial y estadística.
• 	Validación y robustez: Manejar correctamente los tipos numéricos evita errores de precisión, 
divisiones inválidas o resultados inesperados, garantizando programas más confiables.
"""

# Referencias
"""
https://www.pythondeep.com/tutoriales/enteros-y-floats-en-python/
https://realpython.com/python-data-types/
https://www.tutorialsteacher.com/python/python-number-type
https://docs.python.org/3/library/stdtypes.html
https://python-academy.org/en/guide/numeric-data-types
"""
