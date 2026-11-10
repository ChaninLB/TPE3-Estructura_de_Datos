from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


# ------------------------- funciones de apoyo ✅ -------------------------
def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver, extras = False):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")
    if extras:
        print(" 10. Ordenar asc     11. Ordenar desc     12. Busqueda binaria")



# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if pila.apilar(pasajero):                  # 2. LLAMAR
                print("  ✓ Apilado: ahora es el tope") # 3. MOSTRAR
        elif op == "2":
            pila.listar()
        elif op == "3":
            p = pila.desapilar()
            if p:
                print(f"Salio del tope: {p}")
                tope_actual = pila.ver_tope()
                if tope_actual:
                    print(f"Nuevo tope: {tope_actual.nombre} ({tope_actual.numero})")
                else:
                    print("La pila ahora esta vacia")
            else:
                print("La pila esta vacia no hay elementos para desapilar")
        elif op == "4":
            p = pila.ver_tope()
            if p:
                print(f"Tope actual: {p}")
            else:
                print("pila vacia")
        elif op == "5":
            num = leer_entero("Ingrese numero de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"Encontrado en la posicion [{pos}]: {pila.datos[pos]}")
            else:
                print("Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("Ingrese número de pasajero a modificar: ")
            nuevo_destino = input("Nuevo destino: ").strip()
            nuevo_asiento = input("Nuevo asiento: ").strip().upper()
            if pila.modificar(num, nuevo_destino, nuevo_asiento):
                print("Pasajero modificado exitosamente")
            else:
                print("No se encontro el pasajero")
        elif op == "7":
            num = leer_entero("Ingrese numero de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print(f"Pasajero {num} eliminado correctamente")
            else:
                print("No se encontro el pasajero en la pila")
        elif op == "8":
            pila_copia = pila.copiar()
            print("Listado Pila Copiad:")
            pila_copia.listar()
        elif op == "9":
            print(f"Longitud: {pila.longitud()} Esta vacia: {pila.esta_vacia()}")
        elif op == "C":
            for p in datos_prueba():
                pila.apilar(p)
            print("Datos de prueba apilados")
        elif op == "0":
            break
        else:
            print("  Opcion no valida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente", extras = True)
        op = input("Opción: ").strip().upper()

        if op == "1":                                  # ✅ ejemplo resuelto
            pasajero = leer_pasajero()                 # 1. LEER
            if cola.encolar(pasajero):                 # 2. LLAMAR
                print("  ✓ Encolado: está al final")   # 3. MOSTRAR
        elif op == "2":
            cola.listar()
        elif op == "3":
            p = cola.desencolar()
            if p:
                print(f"Salió del frente: {p}")
                frente_actual = cola.ver_frente()
                if frente_actual:
                    print(f"Nuevo frente: {frente_actual.nombre} ({frente_actual.numero})")
                else:
                    print("La cola ahora está vacia")
            else:
                print("La cola está vacia (no hay elementos para desencolar)")
        elif op == "4":
            p = cola.ver_frente()
            if p:
                print(f"Frente actual: {p}")
            else:
                print("cola vacia")
        elif op == "5":
            num = leer_entero("Ingrese numero de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f"Encontrado en la posicion [{pos}]: {cola.datos[pos]}")
            else:
                print("Pasajero no encontrado")
        elif op == "6":
            num = leer_entero("Ingrese numero de pasajero a modificar: ")
            nuevo_destino = input("Nuevo destino: ").strip()
            nuevo_asiento = input("Nuevo asiento: ").strip().upper()
            if cola.modificar(num, nuevo_destino, nuevo_asiento):
                print("Pasajero modificado exitosamente")
            else:
                print("No se encontro el pasajero")
        elif op == "7":
            num = leer_entero("Ingrese numero de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print(f"Pasajero {num} eliminado correctamente")
            else:
                print("No se encontro el pasajero en la cola")
        elif op == "8":
            cola_copia = cola.copiar()
            print("Listado de la Cola Copiada:")
            cola_copia.listar()
        elif op == "9":
            print(f"Longitud: {cola.longitud()} Esta vacia: {cola.esta_vacia()}")
        elif op == "10":
            cola.ordenar_ascendente()
            print("Cola ordenada ascendentemente por numero de pasajero")
            cola.listar()
        elif op == "11":
            cola.ordenar_descendente()
            print("Cola ordenada descendentemente por numero de pasajero")
            cola.listar()
        elif op == "12":
            num = leer_entero("Ingrese numero de pasajero para busqueda binaria: ")
            pos = cola.busqueda_binaria(num)
            if pos != -1:
                print(f"Busqueda Binaria Encontrado en la posicion [{pos}]: {cola.datos[pos]}")
            else:
                print("Pasajero no encontrado")
        elif op == "C":
            for p in datos_prueba():
                cola.encolar(p)
            print("Datos de prueba encolados")
        elif op == "0":
            break
        else:
            print("Opción no válida")


# ---------------------- MENÚ PRINCIPAL ✅ ----------------------
def main():
    while True:
        print("\n===== TAREA PILAS Y COLAS · PASAJEROS ✈ =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()