from pasajero import Pasajero


class MiCola:
    """Cola (FIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos  -> [FRENTE, ..., FINAL, None, None]
    FRENTE -> datos[0]             (el primero que llegó: el único que sale)
    FINAL  -> datos[cantidad - 1]  (los nuevos se ponen detrás de él)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
    sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):                     # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La cola está llena")
            return False
        self.datos[self.cantidad] = pasajero          # se pone a la fila por detrás
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del FRENTE al FINAL
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):                # 0, 1, ..., cantidad-1  (hacia adelante)
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del frente al final -------
    def desencolar(self):
        if self.cantidad == 0:
            return None
        
        pasajero_salido = self.datos[0]

        for i in range(self.cantidad - 1):
            self.datos[i] = self.datos[i + 1]
            
        self.datos[self.cantidad - 1] = None
        self.cantidad = self.cantidad - 1
        return pasajero_salido

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos != -1:
            self.datos[pos].destino = nuevo_destino
            self.datos[pos].asiento = nuevo_asiento
            return True
        return False

    def eliminar_por_numero(self, numero):
        if self.buscar(numero) == -1:
            return False

        total_elementos = self.cantidad
        encontrado = False
        for _ in range(total_elementos):
            p = self.desencolar()
            if p.numero == numero:
                encontrado = True
            else:
                self.encolar(p)
        return encontrado

    def copiar(self):
        cola_copia = MiCola(self.capacidad)
        for i in range(self.cantidad):
            p = self.datos[i]
            cola_copia.datos[cola_copia.cantidad] = Pasajero(p.numero, p.nombre, p.cedula, p.edad, p.fecha_vuelo, p.destino, p.asiento)
            cola_copia.cantidad = cola_copia.cantidad + 1
        return cola_copia

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        if self.cantidad == 0:
            return True
        else:
            return False

    def ordenar_ascendente(self):
        if self.cantidad <= 1:
            return
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero > self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def ordenar_descendente(self):
        if self.cantidad <= 1:
            return
        for i in range(self.cantidad - 1):
            for j in range(self.cantidad - 1 - i):
                if self.datos[j].numero < self.datos[j + 1].numero:
                    aux = self.datos[j]
                    self.datos[j] = self.datos[j + 1]
                    self.datos[j + 1] = aux

    def busqueda_binaria(self, numero):
        inicio = 0
        fin = self.cantidad - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.datos[medio].numero == numero:
                return medio 
            elif self.datos[medio].numero < numero:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1