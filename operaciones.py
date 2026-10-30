#opc 2
def mostrar_inventario(inventario):
    """
    Recorre la lista de inventario y muestra los datos de cada producto.
    Si la lista está vacía, aborta la ejecución y notifica al usuario.

    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas
    """ 
    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return
    print("\n--- INVENTARIO DE LA FERRETERÍA ---")
    for producto in inventario:
        print(f"| Producto: {producto['herramienta']} | Cantidad: {producto['cantidad']} |")
    print("-" * 40) #imprime una línea de separación para mejorar la legibilidad

#opc 1

def cargar_herramientas(inventario):
    """
    Permite al usuario ingresar múltiples productos al inventario.
    Cada producto se guarda en un diccionario validando nombres (no vacíos, no duplicados)
    y cantidades (enteros mayores o iguales a cero).

    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas.
        
    Raises:
        ValueError: Lanzado intencionalmente si las validaciones de negocio fallan, 
                    pero es capturado internamente por los bloques try/except para reintentar.
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
    for _ in range(cant_a_cargar): # _ variable de descarte (no se necesita usar el valor de la variable)
        print("-" * 40) #imprime una línea de separación para mejorar la legibilidad
    #Validamos el nombre de la herramienta para que no sea vacío y no se repita en el inventario
        while True:
            try:
                herramienta = input("Ingrese el nombre de la herramienta: ").strip()
                if not herramienta:
                    raise ValueError("El nombre de la herramienta no puede estar vacío.")
                #Verificamos si la herramienta ya existe en el inventario para evitar duplicados ignorando diferencias de mayúsculas y minúsculas
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
        print(f"[+] La herramienta '{herramienta}' ha sido agregada al inventario con {cantidad} unidades.")
        print("-" * 40)


#opc 3

def consultar_stock(inventario):
    """
    Busca una herramienta por su nombre y muestra su stock actual.
    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas.
    Raises:
        ValueError: Si el nombre ingresado está vacío (se delega el manejo a main.py).
    """

    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return
    print("\n--- CONSULTA DE STOCK ---")
    herramienta = input("Ingrese el nombre de la herramienta a consultar: ").strip()
    # Si el input está vacío, lanzamos el error para que main.py aborte y vuelva al menú
    if not herramienta:
        raise ValueError("El nombre de la herramienta no puede estar vacío.")
    # Búsqueda secuencial ignorando diferencias de mayúsculas y minúsculas
    for producto in inventario:
        if producto['herramienta'].lower() == herramienta.lower():
            # Imprimimos usando el nombre original formateado del diccionario
            print(f"\n[+] Stock disponible de '{producto['herramienta']}': {producto['cantidad']} unidades.")
            print("-" * 40)
            return
    # Si el bucle termina sin ejecutar el return, asumimos que no existe
    print(f"\n[-] La herramienta '{herramienta}' no se encuentra en el catálogo.")
    print("-" * 40)

#opc 4

def reporte_agotados(inventario):
    """
    Filtra y muestra las herramientas del catálogo cuyo stock es exactamente cero.
    Informa al usuario si el inventario está vacío o si no hay productos agotados.

    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas.
    """
    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return
    print("\n--- REPORTE DE AGOTADOS ---")

    hay_faltantes = False

    for producto in inventario:
        if producto['cantidad'] == 0:
            hay_faltantes = True
            print(f"| Producto: {producto['herramienta']} | Cantidad: {producto['cantidad']} |")

    if not hay_faltantes:
        print("\n[+] No hay productos agotados en el inventario.")

    print("-" * 40)

#opc 5

def alta_producto(inventario):
    """
    Agrega una única herramienta nueva al inventario validando las reglas de negocio.
    Delega el manejo de errores (entradas vacías, duplicados, datos inválidos) a main.py.

    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas.
        
    Raises:
        ValueError: Si el nombre está vacío, el producto ya existe, o el stock es negativo.
    """
    print("\n--- ALTA DE NUEVO PRODUCTO ---")
    herramienta = input("Ingrese el nombre de la herramienta: ").strip()
    if not herramienta:
        raise ValueError("[!] El nombre de la herramienta no puede estar vacío.")

    for producto in inventario:
        if producto['herramienta'].lower() == herramienta.lower():
            raise ValueError("[!] La herramienta ya existe en el inventario.")

    cantidad = int(input(f"Ingrese el stock inicial de la herramienta '{herramienta}': "))
    
    if cantidad < 0:
        raise ValueError("[!] El stock inicial no puede ser negativo.")

    inventario.append({'herramienta': herramienta, 'cantidad': cantidad})
    print(f"[+] La herramienta '{herramienta}' ha sido agregada al inventario con {cantidad} unidades.")

    print("-" * 40)

#opc 6

def actualizar_stock(inventario):
    """
    Actualiza el stock de una herramienta existente (venta o ingreso).
    Respeta un orden estricto de validaciones, abortando ante el primer error.

    Args:
        inventario (list): Lista de diccionarios con el catálogo de herramientas.
        
    Raises:
        ValueError: Si el nombre está vacío, las unidades son <= 0, o la venta supera el stock.
    """
#Verificamos que el inventario no esté vacío antes de continuar
    if not inventario:
        print("\n[!] El inventario está vacío actualmente.")
        return
    
    print("\n--- ACTUALIZACIÓN DE STOCK ---")
#Validamos que el nombre de la herramienta no esté vacío
    herramienta = input("Ingrese el nombre de la herramienta a actualizar: ").strip()
    if not herramienta:
        raise ValueError("[!] El nombre de la herramienta no puede estar vacío.")
    #Buscamos si la herramienta existe en el inventario y guardamos su referencia para actualizarla
    producto_encontrado = None
    for producto in inventario:
        if producto['herramienta'].lower() == herramienta.lower():
            producto_encontrado = producto
            break

    if not producto_encontrado:
        print(f"\n[-] La herramienta '{herramienta}' no se encuentra en el catálogo.")
        print("-" * 40)
        return

    print(f"[+] Stock actual de '{producto_encontrado['herramienta']}': {producto_encontrado['cantidad']} unidades.")
#Solicitamos al usuario el tipo de movimiento (venta o ingreso) y validamos que sea '1' o '2'
    tipo_de_movimento = input("Ingrese '1' para venta o '2' para ingreso de stock: ").strip()

    if tipo_de_movimento not in ['1', '2']:
        print("[!] Opción inválida. Debe ingresar '1' para venta o '2' para ingreso de stock.")
        print("-" * 40)
        return

    #Pedimos una sola vez la cantidad a vender o ingresar y validamos que sea un número entero mayor que cero

    unidades = int(input("Ingrese la cantidad a vender o ingresar: "))

    if unidades <= 0:
        raise ValueError("[!] La cantidad debe ser un número entero mayor que cero.")


    if tipo_de_movimento == '1': #Venta    
        if unidades > producto_encontrado['cantidad']:
            raise ValueError(f"[!] No hay suficiente stock para realizar la venta. Stock disponible: {producto_encontrado['cantidad']} unidades.")
        producto_encontrado['cantidad'] -= unidades
        accion = "Venta"
    else: #Ingreso  
        producto_encontrado['cantidad'] += unidades
        accion = "Ingreso"
        
    print(f"[+] {accion} exitoso Stock actualizado de '{producto_encontrado['herramienta']}': {producto_encontrado['cantidad']} unidades.")
    print("-" * 40)

