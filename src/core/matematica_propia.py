"""
Librería Matemática y Estadística Propia - Motor Numérico MomoLang XD
======================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación 100% desde cero en Python puro (sin NumPy, SciPy ni Pandas).
Proporciona estructuras vectoriales unidimensionales, operaciones aritméticas
vectorizadas elemento a elemento, máscaras relacionales y cálculo de
estadísticas descriptivas nativas.
"""

import math


class VectorMomo:
    """
    Estructura vectorial propia optimizada para operaciones numéricas
    vectorizadas, evaluación de condiciones booleanas y cálculo de estadísticas.
    """

    def __init__(self, elementos=None):
        if elementos is None:
            self._datos = []
        elif isinstance(elementos, VectorMomo):
            self._datos = list(elementos._datos)
        elif isinstance(elementos, (list, tuple)):
            self._datos = list(elementos)
        else:
            self._datos = [elementos]

    @property
    def datos(self):
        """Retorna la lista de elementos en Python nativo."""
        return self._datos

    def __len__(self):
        return len(self._datos)

    def __iter__(self):
        return iter(self._datos)

    def __repr__(self):
        return f"VectorMomo({self._datos})"

    def __getitem__(self, clave):
        if isinstance(clave, slice):
            return VectorMomo(self._datos[clave])
        elif isinstance(clave, (list, tuple, VectorMomo)):
            elementos_clave = clave.datos if isinstance(clave, VectorMomo) else clave
            if elementos_clave and isinstance(elementos_clave[0], bool):
                if len(elementos_clave) != len(self._datos):
                    raise ValueError(
                        f"La longitud de la máscara booleana ({len(elementos_clave)}) "
                        f"no coincide con la longitud del vector ({len(self._datos)})."
                    )
                return VectorMomo([val for val, m in zip(self._datos, elementos_clave) if m])
            return VectorMomo([self._datos[i] for i in elementos_clave])
        return self._datos[clave]

    def __setitem__(self, clave, valor):
        self._datos[clave] = valor

    # -------------------------------------------------------------------------
    # Operaciones Vectorizadas Aritméticas (Elemento a Elemento o Escalar)
    # -------------------------------------------------------------------------

    def _operacion_binaria(self, otro, operacion_func, nombre_op="operación"):
        if isinstance(otro, VectorMomo):
            if len(self._datos) != len(otro._datos):
                raise ValueError(
                    f"Error de dimensiones en {nombre_op}: vector de longitud {len(self._datos)} "
                    f"con vector de longitud {len(otro._datos)}."
                )
            resultado = []
            for a, b in zip(self._datos, otro._datos):
                if a is None or b is None:
                    resultado.append(None)
                else:
                    resultado.append(operacion_func(a, b))
            return VectorMomo(resultado)
        else:
            resultado = []
            for a in self._datos:
                if a is None:
                    resultado.append(None)
                else:
                    resultado.append(operacion_func(a, otro))
            return VectorMomo(resultado)

    def __add__(self, otro):
        return self._operacion_binaria(otro, lambda a, b: a + b, "suma")

    def __radd__(self, otro):
        return self.__add__(otro)

    def __sub__(self, otro):
        return self._operacion_binaria(otro, lambda a, b: a - b, "resta")

    def __rsub__(self, otro):
        if isinstance(otro, VectorMomo):
            return otro.__sub__(self)
        return VectorMomo([otro - x if x is not None else None for x in self._datos])

    def __mul__(self, otro):
        return self._operacion_binaria(otro, lambda a, b: a * b, "multiplicación")

    def __rmul__(self, otro):
        return self.__mul__(otro)

    def __truediv__(self, otro):
        def division_segura(a, b):
            if b == 0:
                raise ZeroDivisionError("División por cero detectada en el cálculo vectorial.")
            return a / b
        return self._operacion_binaria(otro, division_segura, "división")

    def __rtruediv__(self, otro):
        def division_segura(a, b):
            if b == 0:
                raise ZeroDivisionError("División por cero detectada en el cálculo vectorial.")
            return a / b
        if isinstance(otro, VectorMomo):
            return otro.__truediv__(self)
        return VectorMomo([division_segura(otro, x) if x is not None else None for x in self._datos])

    def __mod__(self, otro):
        return self._operacion_binaria(otro, lambda a, b: a % b, "módulo")

    def __pow__(self, otro):
        return self._operacion_binaria(otro, lambda a, b: a ** b, "potencia")

    # -------------------------------------------------------------------------
    # Operaciones Relacionales (Producen Máscara Booleana para Filtrado)
    # -------------------------------------------------------------------------

    def _comparacion_binaria(self, otro, comp_func):
        if isinstance(otro, VectorMomo):
            res = [comp_func(a, b) if a is not None and b is not None else False 
                   for a, b in zip(self._datos, otro._datos)]
            return VectorMomo(res)
        else:
            res = [comp_func(a, otro) if a is not None else False for a in self._datos]
            return VectorMomo(res)

    def __gt__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a > b)

    def __ge__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a >= b)

    def __lt__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a < b)

    def __le__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a <= b)

    def __eq__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a == b)

    def __ne__(self, otro):
        return self._comparacion_binaria(otro, lambda a, b: a != b)

    # -------------------------------------------------------------------------
    # Algoritmos Estadísticos Nativos
    # -------------------------------------------------------------------------

    def _valores_numericos_validos(self):
        validos = []
        for x in self._datos:
            if x is not None and isinstance(x, (int, float)) and not isinstance(x, bool):
                validos.append(float(x))
        return validos

    def suma(self):
        validos = self._valores_numericos_validos()
        return sum(validos) if validos else 0.0

    def contar_papus(self):
        return sum(1 for x in self._datos if x is not None and x != "")

    def promedio(self):
        validos = self._valores_numericos_validos()
        if not validos:
            return 0.0
        return sum(validos) / len(validos)

    def media(self):
        return self.promedio()

    def mediana(self):
        validos = sorted(self._valores_numericos_validos())
        n = len(validos)
        if n == 0:
            return 0.0
        mitad = n // 2
        if n % 2 == 1:
            return validos[mitad]
        else:
            return (validos[mitad - 1] + validos[mitad]) / 2.0

    def el_mas_pro(self):
        validos = self._valores_numericos_validos()
        if not validos:
            return 0.0
        return max(validos)

    def maximo(self):
        return self.el_mas_pro()

    def el_mas_manco(self):
        validos = self._valores_numericos_validos()
        if not validos:
            return 0.0
        return min(validos)

    def minimo(self):
        return self.el_mas_manco()

    def desviacion_pro(self):
        validos = self._valores_numericos_validos()
        n = len(validos)
        if n <= 1:
            return 0.0
        prom = sum(validos) / n
        suma_cuadrados = sum((x - prom) ** 2 for x in validos)
        return math.sqrt(suma_cuadrados / (n - 1))


def sumar_papus(a, b):
    if isinstance(a, VectorMomo):
        return a + b
    elif isinstance(b, VectorMomo):
        return b + a
    return a + b


def multiplicacion(a, b):
    if isinstance(a, VectorMomo):
        return a * b
    elif isinstance(b, VectorMomo):
        return b * a
    return a * b


def resta(a, b):
    if isinstance(a, VectorMomo):
        return a - b
    return a - b


def division(a, b):
    if b == 0:
        raise ZeroDivisionError("Error: Intento de división por cero.")
    if isinstance(a, VectorMomo):
        return a / b
    return a / b
