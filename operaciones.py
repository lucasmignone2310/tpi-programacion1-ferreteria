#opc 2
def mostrar_inventario(inventario):
    """
    Recorre la lista de inventario y muestra los datos de cada producto.
    Si la lista está vacía, aborta la ejecución y notifica al usuario.
    """ 
    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return
    print("\n--- Inventario de la Ferretería ---")
    for producto in inventario:
        print(f"| Producto: {producto['nombre']} | Cantidad: {producto['cantidad']} | Precio: ${producto['precio']} |")
    print("-" * 40) #imprime una línea de separación para mejorar la legibilidad