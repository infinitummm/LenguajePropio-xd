"""
Librería Matemática y Estadística Propia - Motor Numérico Vectorial
===================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación desde cero en Python puro (sin NumPy ni SciPy)
para cálculo vectorial, operaciones elemento a elemento y estadística descriptiva.
"""

import math


class VectorNum:
    """
    Estructura vectorial unidimensional optimizada para operaciones numéricas,
    evaluación de máscaras booleanas y cálculo de descriptores estadísticos.
    """

    def __init__(self, elementos=None):
        if elementos is None:
            self._datos = []
        elif isinstance(elementos, VectorNum):
            self._datos = list(elementos._datos)
        elif isinstance(elementos, (list, tuple)):
            self._datos = list(elementos)
        else:
            self._datos = [elementos]

    @property
    def datos(self):
        """Retorna una referencia a la lista subyacente de datos."""
        return self._datos

    def __len__(self):
        return len(self._datos)

    def __getitem__(self, clave):
        if isinstance(clave, list):
            # Filtrado por máscara booleana o indexación posicional
            if clave and isinstance(clave[0], bool):
                return VectorNum([val for val, mascara in zip(self._datos, clave) if mascara])
            return VectorNum([self._datos[i] for i in clave])
        elif isinstance(clave, VectorNum):
            return self.__getitem__(clave._datos)
        elif isinstance(clave, slice):
            return VectorNum(self._datos[clave])
        return self._datos[clave]

    def __setitem__(self, clave, valor):
        self._datos[clave] = valor

    def __repr__(self):
        return f"VectorNum({repr(self._datos)})"

    # =========================================================================
    # Operaciones Aritméticas Elemento a Elemento (Vector / Escalar)
    # =========================================================================

    def sumar(self, otro):
        if isinstance(otro, VectorNum):
            if len(self) != len(otro):
                raise ValueError(f"Discrepancia dimensional: {len(self)} vs {len(otro)}")
            return VectorNum([a + b if a is not None and b is not None else None for a, b in zip(self._datos, otro._datos)])
        elif isinstance(otro, (int, float)):
            return VectorNum([a + otro if a is not None else None for a in self._datos])
        raise TypeError(f"Operación no soportada entre VectorNum y {type(otro).__name__}")

    def restar(self, otro):
        if isinstance(otro, VectorNum):
            if len(self) != len(otro):
                raise ValueError(f"Discrepancia dimensional: {len(self)} vs {len(otro)}")
            return VectorNum([a - b if a is not None and b is not None else None for a, b in zip(self._datos, otro._datos)])
        elif isinstance(otro, (int, float)):
            return VectorNum([a - otro if a is not None else None for a in self._datos])
        raise TypeError(f"Operación no soportada entre VectorNum y {type(otro).__name__}")

    def multiplicar(self, otro):
        if isinstance(otro, VectorNum):
            if len(self) != len(otro):
                raise ValueError(f"Discrepancia dimensional: {len(self)} vs {len(otro)}")
            return VectorNum([a * b if a is not None and b is not None else None for a, b in zip(self._datos, otro._datos)])
        elif isinstance(otro, (int, float)):
            return VectorNum([a * otro if a is not None else None for a in self._datos])
        raise TypeError(f"Operación no soportada entre VectorNum y {type(otro).__name__}")

    def dividir(self, otro):
        if isinstance(otro, VectorNum):
            if len(self) != len(otro):
                raise ValueError(f"Discrepancia dimensional: {len(self)} vs {len(otro)}")
            resultado = []
            for a, b in zip(self._datos, otro._datos):
                if a is None or b is None or b == 0:
                    resultado.append(float('nan'))
                else:
                    resultado.append(a / b)
            return VectorNum(resultado)
        elif isinstance(otro, (int, float)):
            if otro == 0:
                return VectorNum([float('nan') for _ in self._datos])
            return VectorNum([a / otro if a is not None else float('nan') for a in self._datos])
        raise TypeError(f"Operación no soportada entre VectorNum y {type(otro).__name__}")

    def potencia(self, exponente):
        return VectorNum([a ** exponente if a is not None else None for a in self._datos])

    def modulo(self, otro):
        if isinstance(otro, (int, float)):
            return VectorNum([a % otro if a is not None and otro != 0 else float('nan') for a in self._datos])
        elif isinstance(otro, VectorNum):
            return VectorNum([a % b if a is not None and b is not None and b != 0 else float('nan') for a, b in zip(self._datos, otro._datos)])
        raise TypeError("Operando no soportado para módulo.")

    # Sobrecarga de operadores estándar en Python
    def __add__(self, otro): return self.sumar(otro)
    def __radd__(self, otro): return self.sumar(otro)
    def __sub__(self, otro): return self.restar(otro)
    def __mul__(self, otro): return self.multiplicar(otro)
    def __rmul__(self, otro): return self.multiplicar(otro)
    def __truediv__(self, otro): return self.dividir(otro)
    def __pow__(self, exponente): return self.potencia(exponente)
    def __mod__(self, otro): return self.modulo(otro)

    # Métodos con sufijo _xd para compatibilidad
    def sumar_xd(self, otro): return self.sumar(otro)
    def restar_xd(self, otro): return self.restar(otro)
    def multiplicar_xd(self, otro): return self.multiplicar(otro)
    def dividir_xd(self, otro): return self.dividir(otro)
    def potencia_xd(self, exp): return self.potencia(exp)
    def modulo_xd(self, otro): return self.modulo(otro)

    # =========================================================================
    # Operadores Relacionales (Generación de Máscaras Booleanas)
    # =========================================================================

    def mayor_que_xd(self, val):
        return [x > val if x is not None and not (isinstance(x, float) and math.isnan(x)) else False for x in self._datos]

    def menor_que_xd(self, val):
        return [x < val if x is not None and not (isinstance(x, float) and math.isnan(x)) else False for x in self._datos]

    def mayor_igual_xd(self, val):
        return [x >= val if x is not None and not (isinstance(x, float) and math.isnan(x)) else False for x in self._datos]

    def menor_igual_xd(self, val):
        return [x <= val if x is not None and not (isinstance(x, float) and math.isnan(x)) else False for x in self._datos]

    def igual_a_xd(self, val):
        return [x == val for x in self._datos]

    def diferente_de_xd(self, val):
        return [x != val for x in self._datos]

    # =========================================================================
    # Descriptores Estadísticos y Reducciones
    # =========================================================================

    def obtener_validos_xd(self):
        """Retorna únicamente los valores numéricos válidos (excluye None y NaN)."""
        validos = []
        for x in self._datos:
            if x is not None and isinstance(x, (int, float)) and not math.isnan(x):
                validos.append(float(x) if isinstance(x, float) else x)
        return validos

    def suma_xd(self):
        validos = self.obtener_validos_xd()
        return sum(validos) if validos else 0

    def conteo_xd(self):
        return len(self.obtener_validos_xd())

    def promedio_xd(self):
        validos = self.obtener_validos_xd()
        if not validos:
            return float('nan')
        return sum(validos) / len(validos)

    def mediana_xd(self):
        validos = sorted(self.obtener_validos_xd())
        n = len(validos)
        if n == 0:
            return float('nan')
        mitad = n // 2
        if n % 2 == 1:
            return float(validos[mitad])
        return (validos[mitad - 1] + validos[mitad]) / 2.0

    def minimo_xd(self):
        validos = self.obtener_validos_xd()
        return min(validos) if validos else float('nan')

    def maximo_xd(self):
        validos = self.obtener_validos_xd()
        return max(validos) if validos else float('nan')

    def varianza_xd(self, muestral=True):
        validos = self.obtener_validos_xd()
        n = len(validos)
        if n <= 1:
            return 0.0
        media = self.promedio_xd()
        suma_cuadrados = sum((x - media) ** 2 for x in validos)
        denominador = (n - 1) if muestral else n
        return suma_cuadrados / denominador

    def desviacion_estandar_xd(self):
        return math.sqrt(self.varianza_xd())

    def percentil_xd(self, p):
        """Calcula el percentil p (0 <= p <= 100) mediante interpolación lineal."""
        validos = sorted(self.obtener_validos_xd())
        n = len(validos)
        if n == 0:
            return float('nan')
        if p <= 0:
            return float(validos[0])
        if p >= 100:
            return float(validos[-1])

        pos = (n - 1) * (p / 100.0)
        base = int(pos)
        fraccion = pos - base
        if base + 1 < n:
            return validos[base] + fraccion * (validos[base + 1] - validos[base])
        return float(validos[base])

    def cuartiles_xd(self):
        """Retorna (Q1, Q2/mediana, Q3, IQR)."""
        q1 = self.percentil_xd(25)
        q2 = self.percentil_xd(50)
        q3 = self.percentil_xd(75)
        iqr = q3 - q1 if not math.isnan(q3) and not math.isnan(q1) else float('nan')
        return q1, q2, q3, iqr


# Alias para retrocompatibilidad completa
Arreglo = VectorNum


# =============================================================================
# Funciones Utilitarias del Módulo
# =============================================================================

def crear_arreglo_xd(datos):
    """Crea una instancia de VectorNum a partir de un iterable."""
    return VectorNum(datos)

def rango_xd(inicio, fin=None, paso=1):
    """Genera una secuencia numérica en forma de VectorNum."""
    if fin is None:
        inicio, fin = 0, inicio
    valores = []
    actual = inicio
    while actual < fin if paso > 0 else actual > fin:
        valores.append(actual)
        actual += paso
    return VectorNum(valores)

def ceros_xd(n):
    """Crea un vector con n ceros."""
    return VectorNum([0] * n)

def unos_xd(n):
    """Crea un vector con n unos."""
    return VectorNum([1] * n)
