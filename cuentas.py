# Solicitar el nombre para la lista o arreglo
nombre_lista = input("Ingresa el nombre para la lista o arreglo: ")
# Crear la lista vacía
lista_valores = []
# Inicializar la variable para almacenar el total
total = 0
# Solicitar el nombre asociado al valor y el valor en sí
while True:
    nombre = input("Ingresa el nombre asociado al valor (o escribe 'salir' para terminar): ")
    if nombre.lower() == "salir":
        break
    valor = float(input("Ingresa el valor: "))
    # Multiplicar el valor por 1.21 y agregar el par nombre-valor a la lista
    lista_valores.append((nombre, valor * 1.21))
    # Sumar el valor al total
    total += valor * 1.21
    total = round(total, 2)
# Imprimir la lista de valores
print(f"\n{nombre_lista}:")
for nombre, valor in lista_valores:
    print(f"{nombre}: {valor}")
# Imprimir el total
print(f"Total: {total}")