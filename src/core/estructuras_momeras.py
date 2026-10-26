"""
Librería de Estructuras de Datos Propias - estructuras_momeras
=============================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación 100% nativa en Python puro de estructuras de datos clásicas
para el lenguaje MomoLang XD:
- PilaMomera (LIFO: apilar, desapilar, tope, tamano).
- ColaMomera (FIFO: encolar, desencolar, frente, tamano).
- ListaMomera (Arreglo dinámico con indexación, inserción y recorrido).
- MapaMomero (Estructura asociativa clave-valor).
"""


class PilaMomera:
    """Estructura de datos LIFO (Last-In, First-Out) nativa de MomoLang XD."""

    def __init__(self, elementos_iniciales=None):
        self._items = list(elementos_iniciales) if elementos_iniciales else []

    def apilar(self, elemento):
        """Inserta un elemento en el tope de la pila."""
        self._items.append(elemento)
        return elemento

    def desapilar(self):
        """Extrae y retorna el elemento en el tope de la pila."""
        if self.esta_vacia():
            raise IndexError("Error en PilaMomera: no se puede desapilar de una pila vacia :v")
        return self._items.pop()

    def tope(self):
        """Consulta el elemento del tope sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("Error en PilaMomera: la pila esta vacia :v")
        return self._items[-1]

    def esta_vacia(self) -> bool:
        return len(self._items) == 0

    def tamano(self) -> int:
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(reversed(self._items))

    def __repr__(self):
        return f"PilaMomera(tope -> {self._items[::-1]})"

    def __str__(self):
        return f"[Pila :v | tam: {len(self._items)}, tope: {self._items[-1] if self._items else 'None'}]"


class ColaMomera:
    """Estructura de datos FIFO (First-In, First-Out) nativa de MomoLang XD."""

    def __init__(self, elementos_iniciales=None):
        self._items = list(elementos_iniciales) if elementos_iniciales else []

    def encolar(self, elemento):
        """Inserta un elemento al final de la cola."""
        self._items.append(elemento)
        return elemento

    def desencolar(self):
        """Extrae y retorna el primer elemento de la cola."""
        if self.esta_vacia():
            raise IndexError("Error en ColaMomera: no se puede desencolar de una cola vacia :v")
        return self._items.pop(0)

    def frente(self):
        """Consulta el elemento al frente de la cola sin retirarlo."""
        if self.esta_vacia():
            raise IndexError("Error en ColaMomera: la cola esta vacia :v")
        return self._items[0]

    def esta_vacia(self) -> bool:
        return len(self._items) == 0

    def tamano(self) -> int:
        return len(self._items)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def __repr__(self):
        return f"ColaMomera(frente -> {self._items})"

    def __str__(self):
        return f"[Cola :v | tam: {len(self._items)}, frente: {self._items[0] if self._items else 'None'}]"


class ListaMomera:
    """Lista dinámica mutable con indexación segura para MomoLang XD."""

    def __init__(self, elementos=None):
        if elementos is None:
            self._elementos = []
        elif isinstance(elementos, (list, tuple)):
            self._elementos = list(elementos)
        elif isinstance(elementos, ListaMomera):
            self._elementos = list(elementos._elementos)
        else:
            self._elementos = [elementos]

    def agregar(self, elemento):
        """Agrega un elemento al final de la lista."""
        self._elementos.append(elemento)
        return elemento

    def obtener(self, indice: int):
        """Obtiene el elemento en el índice dado con soporte de negativos."""
        idx = int(indice)
        if idx < -len(self._elementos) or idx >= len(self._elementos):
            raise IndexError(f"Indice {idx} fuera de limites para ListaMomera de tamano {len(self._elementos)}")
        return self._elementos[idx]

    def asignar(self, indice: int, valor):
        """Modifica el elemento en la posición especificada."""
        idx = int(indice)
        if idx < -len(self._elementos) or idx >= len(self._elementos):
            raise IndexError(f"Indice {idx} fuera de limites para asignacion en ListaMomera")
        self._elementos[idx] = valor
        return valor

    def eliminar(self, indice: int):
        """Elimina y retorna el elemento en el índice dado."""
        idx = int(indice)
        if idx < -len(self._elementos) or idx >= len(self._elementos):
            raise IndexError(f"Indice {idx} fuera de limites para eliminacion en ListaMomera")
        return self._elementos.pop(idx)

    def longitud(self) -> int:
        return len(self._elementos)

    def __len__(self):
        return len(self._elementos)

    def __getitem__(self, indice):
        return self.obtener(indice)

    def __setitem__(self, indice, valor):
        self.asignar(indice, valor)

    def __iter__(self):
        return iter(self._elementos)

    def __contains__(self, item):
        return item in self._elementos

    def __add__(self, otro):
        if isinstance(otro, ListaMomera):
            return ListaMomera(self._elementos + otro._elementos)
        elif isinstance(otro, list):
            return ListaMomera(self._elementos + otro)
        return NotImplemented

    def __repr__(self):
        return f"ListaMomera({self._elementos})"

    def __str__(self):
        return str(self._elementos)


class MapaMomero:
    """Estructura asociativa clave-valor (Diccionario / HashMap) para MomoLang XD."""

    def __init__(self, datos=None):
        self._tabla = {}
        if isinstance(datos, dict):
            self._tabla = dict(datos)
        elif isinstance(datos, (list, tuple)):
            for par in datos:
                if isinstance(par, (list, tuple)) and len(par) == 2:
                    self._tabla[par[0]] = par[1]

    def asignar(self, clave, valor):
        self._tabla[clave] = valor
        return valor

    def obtener(self, clave, por_defecto=None):
        if clave not in self._tabla:
            if por_defecto is not None:
                return por_defecto
            raise KeyError(f"La clave '{clave}' no existe en el MapaMomero. Claves disponibles: {list(self._tabla.keys())}")
        return self._tabla[clave]

    def eliminar(self, clave):
        if clave not in self._tabla:
            raise KeyError(f"No se puede eliminar la clave inexistente '{clave}'")
        return self._tabla.pop(clave)

    def claves(self):
        return list(self._tabla.keys())

    def valores(self):
        return list(self._tabla.values())

    def items(self):
        return list(self._tabla.items())

    def longitud(self) -> int:
        return len(self._tabla)

    def __len__(self):
        return len(self._tabla)

    def __getitem__(self, clave):
        return self.obtener(clave)

    def __setitem__(self, clave, valor):
        self.asignar(clave, valor)

    def __contains__(self, clave):
        return clave in self._tabla

    def __iter__(self):
        return iter(self._tabla)

    def __repr__(self):
        return f"MapaMomero({self._tabla})"

    def __str__(self):
        return str(self._tabla)
