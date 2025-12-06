# Joan Orlando Gonzalez Huerta  
# 2530420
# IM 1-2
"""
- ¿Qué es un CRUD y qué significan Create, Read, Update, Delete?
CRUD es un acrónimo que representa las cuatro operaciones básicas sobre datos: 
Create (Crear), Read (Leer), Update (Actualizar) y Delete (Eliminar). 
Estas operaciones son fundamentales en el manejo de información en bases de datos y aplicaciones.

se utilizó una list de dicts como estructura de datos.
¿Por qué una lista de diccionarios?
• 	Cada elemento (item) se representa como un diccionario con sus atributos:
{"id": "001", "name": "Laptop", "price": 1200.0}
• 	La lista permite almacenar múltiples elementos del mismo tipo y recorrerlos fácilmente con bucles para buscar, 
actualizar o eliminar.
• 	Así se logra un modelo muy parecido a una tabla de registros en una base de datos: cada fila es un diccionario, 
y la lista es la colección completa.

Usar funciones para organizar la lógica de un CRUD aporta varias ventajas clave que hacen el código más claro, 
modular y fácil de mantener
"""
# Problem: In-memory CRUD manager with functions  
"""
Descripción:
Implementa un programa en Python que gestione un conjunto de "items" en memoria mediante operaciones CRUD. Cada ítem puede representar, por ejemplo, un producto de inventario con los siguientes campos sugeridos:

- id (string o int, único)
- name (string)
- price (float)
- quantity (int)

El programa debe:

1) Definir una estructura de datos principal:
   - Opción A: dict item_id -> dict con datos del ítem.
   - Opción B: list de dicts, cada dict con campos id, name, price, quantity.
   (En comentarios, explica cuál opción escogiste y por qué.)

2) Definir FUNCIONES separadas para cada operación CRUD:
   - create_item(data_structure, item_id, name, price, quantity) -> bool o dict
   - read_item(data_structure, item_id) -> dict o None
   - update_item(data_structure, item_id, new_name, new_price, new_quantity) -> bool
   - delete_item(data_structure, item_id) -> bool
   - list_items(data_structure) -> list o simplemente imprime
   Puedes ajustar nombres y parámetros, pero debe quedar claro qué hace cada función y qué regresa.

3) Implementar un MENÚ en el código principal (main loop):
   Ejemplo de opciones:
   - 1) Create item
   - 2) Read item by id
   - 3) Update item by id
   - 4) Delete item by id
   - 5) List all items
   - 0) Exit

4) En el bucle principal:
   - Mostrar el menú.
   - Leer la opción.
   - Según la opción, pedir los datos necesarios (id, name, price, quantity).
   - Llamar a la función correspondiente.
   - Mostrar mensajes claros de resultado.
"""

items = {}

def create_item(data, item_id, name, price, quantity):
    """Create a new item if id does not exist."""
    item_id = str(item_id).strip()
    if not item_id:
        print("Error: invalid input (empty id)")
        return False
    try:
        price = float(price)
        quantity = int(quantity)
        if price < 0 or quantity < 0:
            print("Error: invalid input (negative values)")
            return False
    except ValueError:
        print("Error: invalid input (non-numeric values)")
        return False

    if item_id in data:
        print("Error: id already exists (no duplicates allowed)")
        return False

    data[item_id] = {"name": name.strip(), "price": price, "quantity": quantity}
    print("Item created")
    return True

def read_item(data, item_id):
    """Read item by id."""
    item_id = str(item_id).strip()
    if item_id in data:
        return data[item_id]
    else:
        return None

def update_item(data, item_id, new_name, new_price, new_quantity):
    """Update item if id exists."""
    item_id = str(item_id).strip()
    if item_id not in data:
        print("Item not found")
        return False
    try:
        new_price = float(new_price)
        new_quantity = int(new_quantity)
        if new_price < 0 or new_quantity < 0:
            print("Error: invalid input (negative values)")
            return False
    except ValueError:
        print("Error: invalid input (non-numeric values)")
        return False

    data[item_id]["name"] = new_name.strip()
    data[item_id]["price"] = new_price
    data[item_id]["quantity"] = new_quantity
    print("Item updated")
    return True

def delete_item(data, item_id):
    """Delete item if id exists."""
    item_id = str(item_id).strip()
    if item_id in data:
        del data[item_id]
        print("Item deleted")
        return True
    else:
        print("Item not found")
        return False

def list_items(data):
    """List all items."""
    if not data:
        print("Items list: (empty)")
    else:
        print("Items list:")
        for item_id, info in data.items():
            print(f"ID: {item_id}, Name: {info['name']}, Price: {info['price']}, Quantity: {info['quantity']}")


def menu():
    while True:
        print("\n--- CRUD Menu ---")
        print("1. Create item")
        print("2. Read item by id")
        print("3. Update item by id")
        print("4. Delete item by id")
        print("5. List all items")
        print("0. Exit")

        option = input("Choose an option: ").strip()

        if option == "1":
            item_id = input("Enter item id: ")
            name = input("Enter item name: ")
            price = input("Enter item price: ")
            quantity = input("Enter item quantity: ")
            create_item(items, item_id, name, price, quantity)

        elif option == "2":
            item_id = input("Enter item id to read: ")
            item = read_item(items, item_id)
            if item:
                print(f"ID: {item_id}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")
            else:
                print("Item not found")

        elif option == "3":
            item_id = input("Enter item id to update: ")
            new_name = input("Enter new name: ")
            new_price = input("Enter new price: ")
            new_quantity = input("Enter new quantity: ")
            update_item(items, item_id, new_name, new_price, new_quantity)

        elif option == "4":
            item_id = input("Enter item id to delete: ")
            delete_item(items, item_id)

        elif option == "5":
            list_items(items)

        elif option == "0":
            print("Exiting program...")
            break

        else:
            print("Error: invalid option")

if __name__ == "__main__":
    menu()

"""
Entradas:
- option (string o int; opción de menú).
- item_id (string o int).
- name (string).
- price (float).
- quantity (int).

Validaciones:
- option debe ser una de las opciones definidas (por ejemplo 0–5).
- item_id no vacío tras strip().
- price y quantity deben ser números válidos:
  - price >= 0.0
  - quantity >= 0
- Si falla alguna validación, mostrar "Error: invalid input" y NO realizar la operación.
- En CREATE:
  - Si el id ya existe, decide una política (por ejemplo, no permitir duplicados) y documenta tu elección.
- En READ/UPDATE/DELETE:
  - Si el id no existe, mostrar "Item not found".

Salidas:
- Mensajes tipo:
  - "Item created"
  - "Item updated"
  - "Item deleted"
  - "Item not found"
  - "Items list:" y luego la lista de elementos (formato libre pero legible).

Entradas de prueba:
 1) Normal
Flujo completo: Create → Read → Update → Delete
- Entrada:
- Create: id="101", name="Laptop", price=1200.0, quantity=10
- Read: id="101"
- Update: id="101", new_name="Gaming Laptop", new_price=1500.0, new_quantity=8
- Delete: id="101"
Salidas
Item created
ID: 101, Name: Laptop, Price: 1200.0, Quantity: 10
Item updated
Item deleted

2) Border (casos límite)
- Caso A: cantidad mínima válida
- Create: id="200", name="Mouse", price=25.0, quantity=0
Salidas:
Item created

3) Error (entradas inválidas)
- Caso A: opción de menú inválida
- Input: option="9"
Salidas
Error: invalid option
"""
# Conclusión
"""
El hecho de separar cada operación del CRUD en funciones independientes aporta claridad y eficiencia al programa.
1. Modularidad
• 	Cada operación (create_items, read_items, update_items, delete_items, list_items) tiene su propia función.
• 	Esto evita mezclar lógica y hace que cada bloque tenga una responsabilidad única.
• 	Ejemplo: si quieres cambiar cómo se valida un precio, solo modificas create_item y update_item, sin tocar el resto del código.
2. Reutilización
- Las funciones pueden usarse en distintos contextos: menú de texto, pruebas automáticas, o incluso integrarse en una API.
- No necesitas reescribir la lógica, basta con llamar a la función.
3. Mantenimiento
- Si surge un error en una operación, puedes depurar la función correspondiente sin afectar las demás.
- También facilita agregar nuevas validaciones o campos en el futuro.

Ventajas de usar un diccionario o una lista de diccionarios
Usar un diccionario 
• 	Acceso directo por clave: buscar, actualizar o eliminar un ítem es inmediato.
• 	Evita duplicados: como las claves son únicas, no se pueden crear dos ítems con el mismo id.
• 	Estructura clara: cada id apunta a un diccionario con los atributos del ítem.
Usar una lista de diccionarios 
• 	Orden natural: los ítems se almacenan en el orden en que se crean, útil para listados secuenciales.
• 	Flexibilidad: puedes recorrer la lista y aplicar filtros o búsquedas personalizadas.
• 	Similar a una tabla: cada diccionario es como una fila con columnas (id, name, price, quantity).

Cómo podrías extender este CRUD a un sistema más grande (por ejemplo, guardando datos en archivos o bases de datos)
1. Guardar en archivos
• 	Archivos de texto (CSV, JSON)
2. Usar una base de datos ligera (SQLite)
3. Migrar a bases de datos más grandes (MySQL, PostgreSQL, MongoDB)
4. Extensiones adicionales
• 	Interfaz gráfica o web: conectar el CRUD con una GUI (Tkinter, PyQt) o un framework web (Flask, Django).
"""
# Referencias
"""
https://aprendepython.es/core/datastructures/lists/
https://www.w3schools.com/python/python_dictionaries.asp
https://ellibrodepython.com/funciones-en-python
https://www.youtube.com/watch?v=9k91jETchkI
"""
# url github
"""
https://github.com/2530420-alt/metodologias_de_la_programaci-n_prueba#
git@github.com:2530420-alt/metodologias_de_la_programaci-n_prueba.git

la neta no sabia cual poner, así que puse los dos
"""