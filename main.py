from operaciones import mostrar_inventario

def main():
    inventario = []
    opc = 0 #Incializamos la variable opc en 0 para que el bucle while se ejecute al menos una vez

    while opc !=7:
        print("\n--- Menú Ferreteria ---")
        print("1.Carga de herramientas (Multiples ingresos)")
        print("2.Visualización de inventario")
        print("3.Consulta de stock")
        print("4.Reporte de faltantes")
        print("5.Alta nuevo producto")
        print("6.Actualización de stock(Venta/ingreso)")
        print("7.Salir")

        try:
            #Intentamos pedir la opcion y convertirla a numer
            opc = int(input("Ingrese una opción: "))

            if opc == 1:
                print("Ejecutando opción 1: Carga de herramientas (Multiples ingresos)")
            elif opc == 2:
                print("Ejecutando opción 2: Visualización de inventario")
                mostrar_inventario(inventario)
            elif opc == 3:
                print("Ejecutando opción 3: Consulta de stock")
            elif opc == 4:
                print("Ejecutando opción 4: Reporte de faltantes")
            elif opc == 5:
                print("Ejecutando opción 5: Alta nuevo producto")
            elif opc == 6:
                print("Ejecutando opción 6: Actualización de stock(Venta/ingreso)")
            elif opc == 7:
                print("Saliendo del sistema...")
            else:
                raise ValueError("Opción inválida. Por favor, ingrese un número entre 1 y 7.")
        except ValueError as e:
            #Atrapos el error y mostramos un mensaje de error al usuario
            print(f"Error: {e}. Intente nuevamente.")

#Ejecutamos el programa
main()
