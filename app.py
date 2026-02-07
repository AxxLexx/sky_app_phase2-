import json
import os

FILE = "clientes.json"

def cargar():
    if not os.path.exists(FILE):
        return {}
    with open(FILE, "r") as f:
        return json.load(f)

def guardar(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def crear_cliente():
    nombre = input("Nombre del cliente: ")
    servicio = input("Servicio contratado: ")
    data = cargar()
    data[nombre] = {"servicios": [servicio]}
    guardar(data)
    print("Cliente creado correctamente")

def modificar_cliente():
    nombre = input("Nombre del cliente: ")
    servicio = input("Nuevo servicio: ")
    data = cargar()
    if nombre in data:
        data[nombre]["servicios"].append(servicio)
        guardar(data)
        print("Cliente modificado")
    else:
        print("Cliente no encontrado")

def consultar_cliente():
    nombre = input("Nombre del cliente: ")
    data = cargar()
    print(data.get(nombre, "Cliente no encontrado"))

def eliminar_cliente():
    nombre = input("Nombre del cliente: ")
    data = cargar()
    if nombre in data:
        del data[nombre]
        guardar(data)
        print("Cliente eliminado")
    else:
        print("Cliente no encontrado")

while True:
    print("\n--- Sistema Sky ---")
    print("1. Crear cliente")
    print("2. Modificar cliente")
    print("3. Consultar cliente")
    print("4. Eliminar cliente")
    print("5. Salir")

    opcion = input("Opción: ")

    if opcion == "1":
        crear_cliente()
    elif opcion == "2":
        modificar_cliente()
    elif opcion == "3":
        consultar_cliente()
    elif opcion == "4":
        eliminar_cliente()
    elif opcion == "5":
        break
    else:
        print("Opción inválida")
