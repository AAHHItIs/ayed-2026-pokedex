from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No usar list de Python por debajo."""

    def __init__(self):
        self._cabeza = None
        self.cantidad = 0

    def esta_vacia(self):
        return self._cabeza is None

    def tamanio(self):
        return self.cantidad

    def insertar_al_inicio(self, dato):
        nuevo_nodo = Nodo(dato, self._cabeza)
        self._cabeza = nuevo_nodo
        self.cantidad += 1

    def insertar_al_final(self, dato):
        nuevo_nodo = Nodo(dato, None)
        if self._cabeza is None:
            self._cabeza = nuevo_nodo
        else:
            actual = self._cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.cantidad += 1

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError

    def eliminar(self, dato):
        if self._cabeza is None:
            return False
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente
            self.cantidad -= 1
            return True
        anterior = self._cabeza
        actual = self._cabeza.siguiente
        while actual is not None:
            if actual.dato == dato:
                anterior.siguiente = actual.siguiente
                self.cantidad -= 1
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        actual = self._cabeza
        while actual is not None:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def __iter__(self):
        actual = self._cabeza
        while actual is not None:
            yield actual.dato
            actual = actual.siguiente
