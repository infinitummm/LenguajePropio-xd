"""
Librería Matemática Propia (Reemplazo propio de NumPy desde cero en español xd)
"""

import math

class Arreglo:
    """
    Clase Arreglo que representa vectores y matrices numéricas unidimensionales o bidimensionales.
    """
    def __init__(self, datos):
        if isinstance(datos, Arreglo):
            self.datos = list(datos.datos)
        elif isinstance(datos, (list, tuple)):
            self.datos = list(datos)
        else:
            self.datos = [datos]

    def __len__(self):
        return len(self.datos)

    def __getitem__(self, idx):
        if isinstance(idx, list):
            # Filtrado por máscara booleana o lista de índices
            if idx and isinstance(idx[0], bool):
                return Arreglo([elem for elem, mask in zip(self.datos, idx) if mask])
            return Arreglo([self.datos[i] for i in idx])
        return self.datos[idx]

    def __setitem__(self, idx, val):
        self.datos[idx] = val

    def __repr__(self):
        return f"Arreglo({repr(self.datos)})"

    # --- Operaciones Aritméticas Elemento a Elemento ---

    def sumar_xd(self, otro):
        if isinstance(otro, Arreglo):
            return Arreglo([a + b for a, b in zip(self.datos, otro.datos)])
        elif isinstance(otro, (int, float)):
            return Arreglo([a + otro for a in self.datos])
        raise TypeError("Operando no soportado para suma xd")

    def restar_xd(self, otro):
        if isinstance(otro, Arreglo):
            return Arreglo([a - b for a, b in zip(self.datos, otro.datos)])
        elif isinstance(otro, (int, float)):
            return Arreglo([a - otro for a in self.datos])
        raise TypeError("Operando no soportado para resta xd")

    def multiplicar_xd(self, otro):
        if isinstance(otro, Arreglo):
            return Arreglo([a * b for a, b in zip(self.datos, otro.datos)])
        elif isinstance(otro, (int, float)):
            return Arreglo([a * otro for a in self.datos])
        raise TypeError("Operando no soportado para multiplicación xd")

    def dividir_xd(self, otro):
        if isinstance(otro, Arreglo):
            return Arreglo([a / b if b != 0 else float('nan') for a, b in zip(self.datos, otro.datos)])
        elif isinstance(otro, (int, float)):
            if otro == 0:
                return Arreglo([float('nan') for _ in self.datos])
            return Arreglo([a / otro for a in self.datos])
        raise TypeError("Operando no soportado para división xd")

    def potencia_xd(self, exponente):
        return Arreglo([a ** exponente for a in self.datos])

    def modulo_xd(self, otro):
        if isinstance(otro, (int, float)):
            return Arreglo([a % otro for a in self.datos])
        return Arreglo([a % b for a, b in zip(self.datos, otro.datos)])

    # Sobrecarga de operadores habituales en Python
    def __add__(self, otro): return self.sumar_xd(otro)
    def __sub__(self, otro): return self.restar_xd(otro)
    def __mul__(self, otro): return self.multiplicar_xd(otro)
    def __truediv__(self, otro): return self.dividir_xd(otro)
    def __pow__(self, otro): return self.potencia_xd(otro)
    def __mod__(self, otro): return self.modulo_xd(otro)

    # --- Comparaciones Relacionales (Máscaras Booleanas) ---

    def mayor_que_xd(self, val):
        return [a > val if a is not None else False for a in self.datos]

    def menor_que_xd(self, val):
        return [a < val if a is not None else False for a in self.datos]

    def igual_a_xd(self, val):
        return [a == val for a in self.datos]

    def diferente_de_xd(self, val):
        return [a != val for a in self.datos]

    def mayor_igual_xd(self, val):
        return [a >= val if a is not None else False for a in self.datos]

    def menor_igual_xd(self, val):
        return [a <= val if a is not None else False for a in self.datos]

    # --- Reducciones Estadísticas ---

    def obtener_validos_xd(self):
        """Retorna solo valores numéricos válidos (sin None ni NaN) xd."""
        res = []
        for x in self.datos:
            if x is not None and isinstance(x, (int, float)) and not math.isnan(x):
                res.append(x)
        return res

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
        else:
            return (validos[mitad - 1] + validos[mitad]) / 2.0

    def minimo_xd(self):
        validos = self.obtener_validos_xd()
        return min(validos) if validos else float('nan')

    def maximo_xd(self):
        validos = self.obtener_validos_xd()
        return max(validos) if validos else float('nan')

    def varianza_xd(self):
        validos = self.obtener_validos_xd()
        if len(validos) <= 1:
            return 0.0
        prom = self.promedio_xd()
        return sum((x - prom) ** 2 for x in validos) / (len(validos) - 1)

    def desviacion_estandar_xd(self):
        return math.sqrt(self.varianza_xd())


# --- Funciones Auxiliares del Módulo ---

def crear_arreglo_xd(datos):
    """Crea un Arreglo a partir de una lista o secuencia xd"""
    return Arreglo(datos)

def rango_xd(inicio, fin=None, paso=1):
    """Genera un Arreglo numérico en un rango xd"""
    if fin is None:
        inicio, fin = 0, inicio
    val = inicio
    res = []
    while val < fin:
        res.append(val)
        val += paso
    return Arreglo(res)

def ceros_xd(n):
    """Crea un Arreglo de ceros de tamaño n xd"""
    return Arreglo([0] * n)
