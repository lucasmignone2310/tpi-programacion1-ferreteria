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
        print(f"| Producto: {producto['herramienta']} | Cantidad: {producto['cantidad']} |")
    print("-" * 40) #imprime una línea de separación para mejorar la legibilidad

#opc 1

def cargar_herramientas(inventario):
    """
    Permite al usuario ingresar multiples productos/herramientas al inventario.
    Cada producto/herramienta se guarda en un diccionario con sus respectivos datos.
    """
    print("\n--- ALTA DE HERRAMIENTAS ---")
    #Solicitamos al usuario la cantidad de herramientas a cargar y validamos que sea un número entero mayor que cero
    while True:
        try:
            cant_a_cargar = int(input("Ingrese la cantidad de herramientas a cargar: "))
            if cant_a_cargar <= 0:
                raise ValueError("La cantidad de herramientas a cargar debe ser un número entero mayor que cero.")
            break
        except ValueError as e:
            #Captura el error de int() como el raise manual anterior y muestra un mensaje de error al usuario
            print(f"Error: {e}. Intente nuevamente.")
    #cargar cada herramienta en el inventario
    for _ in range(cant_a_cargar):
        print("-" * 40) #imprime una línea de separación para mejorar la legibilidad
       #Validamos el nombre de la herramienta para que no sea vacío y no se repita en el inventario
        while True:
            try:
                herramienta = input("Ingrese el nombre de la herramienta: ").strip()
                if not herramienta:
                    raise ValueError("El nombre de la herramienta no puede estar vacío.")
                #Verificamos si la herramienta ya existe en el inventario para evitar duplicados
                duplicado = False 
                for producto in inventario:
                    if producto['herramienta'].lower() == herramienta.lower():
                        duplicado = True
                        break
                if duplicado:
                    raise ValueError("La herramienta ya existe en el inventario. No se puede agregar duplicados.")
                break #Si pasa todas las validaciones el nombre es valido.
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")
        #Validamos el stock
        while True:
            try:
                cantidad = int(input(f"Ingrese el stock inicial de la herramienta '{herramienta}': "))  
                if cantidad < 0:
                    raise ValueError("El stock inicial no puede ser negativo.")
                break
            except ValueError as e:
                print(f"Error: {e}. Intente nuevamente.")

        #Guardamos la herramienta en el inventario como un diccionario con sus datos
        inventario.append({'herramienta': herramienta, 'cantidad': cantidad})
        print(f"La herramienta '{herramienta}' ha sido agregada al inventario con {cantidad} unidades.")  

