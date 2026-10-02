"""
Tabla de Símbolos y Sistema de Validación Semántica - MomoLang XD
================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Gestiona el contexto de ejecución, los identificadores en memoria,
funciones de usuario, sus tipos de datos y la detección preventiva de
errores semánticos (variables no declaradas, columnas inexistentes, tipos).
"""

from src.core.datos_propios import TablaMomo, SerieMomo, AgrupamientoMomo
from src.core.matematica_propia import VectorMomo


class ErrorSemantico(Exception):
    """Excepción personalizada para capturar y reportar errores semánticos con precisión."""

    def __init__(self, mensaje, linea=None, columna=None, tipo_error="ERROR_SEMANTICO"):
        self.mensaje = mensaje
        self.linea = linea
        self.columna = columna
        self.tipo_error = tipo_error
        
        pos_str = ""
        if linea is not None:
            pos_str = f" [Línea {linea}" + (f", Col {columna}" if columna is not None else "") + "]"
        
        super().__init__(f"[Error Semántico xd]{pos_str}: {mensaje}")


class SimboloFuncion:
    """Representa una función definida por el usuario en MomoLang XD."""

    def __init__(self, nombre, parametros, cuerpo_ctx, ambito_definicion):
        self.nombre = nombre
        self.parametros = parametros  # list of str
        self.cuerpo_ctx = cuerpo_ctx  # AST node of bloque
        self.ambito_definicion = ambito_definicion  # TablaSimbolos

    def __repr__(self):
        return f"MomoFuncion({self.nombre}({', '.join(self.parametros)}))"


class Simbolo:
    """Representa un identificador almacenado en la Tabla de Símbolos."""

    def __init__(self, nombre, valor, tipo="DESCONOCIDO", metadatos=None):
        self.nombre = nombre
        self.valor = valor
        self.tipo = tipo
        self.metadatos = metadatos or {}

    def __repr__(self):
        return f"Simbolo(nombre='{self.nombre}', tipo='{self.tipo}', valor={type(self.valor).__name__})"


class TablaSimbolos:
    """Entorno de ejecución con alcance léxico (scoping) y validaciones semánticas."""

    def __init__(self, padre=None):
        self.padre = padre
        self._simbolos = {}
        self.errores = []

    def crear_hijo(self):
        """Crea un nuevo alcance subordinado (para bloques, bucles y funciones)."""
        return TablaSimbolos(padre=self)

    def inferir_tipo(self, valor):
        """Determina la categoría de tipo de un valor en tiempo de ejecución."""
        if isinstance(valor, SimboloFuncion):
            return "FUNCION"
        elif isinstance(valor, TablaMomo):
            return "TABLA"
        elif isinstance(valor, AgrupamientoMomo):
            return "AGRUPAMIENTO"
        elif isinstance(valor, SerieMomo):
            return "SERIE"
        elif isinstance(valor, VectorMomo):
            return "VECTOR"
        elif isinstance(valor, bool):
            return "BOOLEANO"
        elif isinstance(valor, (int, float)):
            return "NUMERO"
        elif isinstance(valor, str):
            return "CADENA"
        elif valor is None:
            return "NULO"
        return "OBJETO"

    def definir(self, nombre, valor, tipo=None):
        """Registra o actualiza una variable en el alcance actual."""
        if tipo is None:
            tipo = self.inferir_tipo(valor)

        metadatos = {}
        if isinstance(valor, TablaMomo):
            metadatos["columnas"] = valor.columnas
            metadatos["num_filas"] = valor.num_filas

        simbolo = Simbolo(nombre, valor, tipo=tipo, metadatos=metadatos)
        self._simbolos[nombre] = simbolo
        return simbolo

    def asignar_existente_o_local(self, nombre, valor, tipo=None):
        """Actualiza la variable si ya existe en este scope o en padres; si no, la define localmente."""
        if nombre in self._simbolos:
            return self.definir(nombre, valor, tipo)
        if self.padre and self.padre.existe(nombre):
            return self.padre.asignar_existente_o_local(nombre, valor, tipo)
        return self.definir(nombre, valor, tipo)

    def definir_funcion(self, nombre, parametros, cuerpo_ctx):
        """Registra una función definida por el usuario."""
        func = SimboloFuncion(nombre, parametros, cuerpo_ctx, self)
        self.definir(nombre, func, tipo="FUNCION")
        return func

    def obtener_funcion(self, nombre, linea=None, columna=None):
        """Busca una función de usuario registrada."""
        if nombre in self._simbolos and isinstance(self._simbolos[nombre].valor, SimboloFuncion):
            return self._simbolos[nombre].valor
        if self.padre:
            return self.padre.obtener_funcion(nombre, linea, columna)
        return None

    def existe(self, nombre):
        """Verifica si un identificador está definido en el alcance actual o padres."""
        if nombre in self._simbolos:
            return True
        if self.padre:
            return self.padre.existe(nombre)
        return False

    def obtener(self, nombre, linea=None, columna=None):
        """Obtiene el valor de un símbolo o lanza ErrorSemantico si no existe."""
        if nombre in self._simbolos:
            return self._simbolos[nombre].valor
        if self.padre:
            return self.padre.obtener(nombre, linea, columna)

        variables_disponibles = list(self.obtener_todas_las_variables().keys())
        msg = f"La variable '{nombre}' no ha sido declarada ni cargada antes de usarse."
        if variables_disponibles:
            msg += f" Variables declaradas en este punto: {variables_disponibles}"
        
        raise ErrorSemantico(
            mensaje=msg,
            linea=linea,
            columna=columna,
            tipo_error="VARIABLE_NO_DEFINIDA"
        )

    def obtener_simbolo(self, nombre, linea=None, columna=None):
        """Obtiene el objeto Simbolo completo."""
        if nombre in self._simbolos:
            return self._simbolos[nombre]
        if self.padre:
            return self.padre.obtener_simbolo(nombre, linea, columna)
        
        raise ErrorSemantico(
            mensaje=f"La variable '{nombre}' no existe en la tabla de símbolos.",
            linea=linea,
            columna=columna,
            tipo_error="VARIABLE_NO_DEFINIDA"
        )

    def validar_columna_en_tabla(self, nombre_tabla, nombre_columna, linea=None, columna=None):
        """Comprueba que una columna exista en una tabla registrada."""
        simbolo_tabla = self.obtener_simbolo(nombre_tabla, linea, columna)
        if simbolo_tabla.tipo != "TABLA":
            raise ErrorSemantico(
                mensaje=f"Se esperaba una tabla en '{nombre_tabla}', pero es de tipo '{simbolo_tabla.tipo}'.",
                linea=linea,
                columna=columna,
                tipo_error="TIPO_INCOMPATIBLE"
            )

        columnas = simbolo_tabla.metadatos.get("columnas", [])
        if nombre_columna not in columnas:
            raise ErrorSemantico(
                mensaje=f"La columna '{nombre_columna}' no existe en la tabla '{nombre_tabla}'. Columnas disponibles: {columnas}",
                linea=linea,
                columna=columna,
                tipo_error="COLUMNA_INEXISTENTE"
            )

    def obtener_todas_las_variables(self):
        """Retorna un diccionario consolidado de todas las variables visibles."""
        resultado = {}
        if self.padre:
            resultado.update(self.padre.obtener_todas_las_variables())
        resultado.update(self._simbolos)
        return resultado
