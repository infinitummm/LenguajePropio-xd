"""
Librería de Manipulación de Datos Tabulares - Motor Tabular Propio
==================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación desde cero en Python puro (sin Pandas ni NumPy)
para representación de Series, Tablas bidimensionales (DataFrames),
filtrado, ordenamiento, transformaciones, agrupamientos y lectura/escritura CSV.
"""

import math
from src.core.matematica_propia import VectorNum, Arreglo


class Serie:
    """
    Representa una columna de datos con tipado dinámico, nombre descriptivo
    y operaciones estadísticas vectoriales integradas.
    """

    def __init__(self, datos=None, nombre="columna"):
        self.nombre = nombre
        if isinstance(datos, (VectorNum, Arreglo)):
            self.arreglo = datos
        elif isinstance(datos, (list, tuple)):
            self.arreglo = VectorNum(datos)
        else:
            self.arreglo = VectorNum([datos] if datos is not None else [])

    @property
    def datos(self):
        return self.arreglo.datos

    def __len__(self):
        return len(self.arreglo)

    def __getitem__(self, idx):
        resultado = self.arreglo[idx]
        if isinstance(resultado, (VectorNum, Arreglo)):
            return Serie(resultado, nombre=self.nombre)
        return resultado

    def __setitem__(self, idx, val):
        self.arreglo[idx] = val

    def __repr__(self):
        return f"Serie(nombre='{self.nombre}', filas={len(self)}, datos={repr(self.datos[:5])}{'...' if len(self) > 5 else ''})"

    # Delegación de operaciones estadísticas
    def suma_xd(self): return self.arreglo.suma_xd()
    def promedio_xd(self): return self.arreglo.promedio_xd()
    def media_xd(self): return self.arreglo.promedio_xd()
    def mediana_xd(self): return self.arreglo.mediana_xd()
    def minimo_xd(self): return self.arreglo.minimo_xd()
    def maximo_xd(self): return self.arreglo.maximo_xd()
    def varianza_xd(self): return self.arreglo.varianza_xd()
    def desviacion_estandar_xd(self): return self.arreglo.desviacion_estandar_xd()
    def conteo_xd(self): return self.arreglo.conteo_xd()
    def cuartiles_xd(self): return self.arreglo.cuartiles_xd()


class TablaDatos:
    """
    Estructura tabular bidimensional en memoria (equivalente a DataFrame)
    con soporte para operaciones relacionales, transformaciones y agrupamientos.
    """

    def __init__(self, columnas=None):
        self._columnas = {}
        if columnas:
            for nombre, valores in columnas.items():
                if isinstance(valores, Serie):
                    self._columnas[nombre] = list(valores.datos)
                elif isinstance(valores, (VectorNum, Arreglo)):
                    self._columnas[nombre] = list(valores.datos)
                elif isinstance(valores, (list, tuple)):
                    self._columnas[nombre] = list(valores)
                else:
                    self._columnas[nombre] = [valores]

    @property
    def columnas(self):
        return self._columnas

    @property
    def nombres_columnas(self):
        return list(self._columnas.keys())

    @property
    def numero_filas(self):
        if not self._columnas:
            return 0
        primera_columna = next(iter(self._columnas.values()))
        return len(primera_columna)

    def __len__(self):
        return self.numero_filas

    def __getitem__(self, clave):
        if isinstance(clave, str):
            if clave not in self._columnas:
                raise KeyError(f"La columna '{clave}' no existe en la TablaDatos.")
            return Serie(self._columnas[clave], nombre=clave)
        elif isinstance(clave, list):
            # Selección de múltiples columnas
            return self.seleccionar_xd(clave)
        raise TypeError("El acceso por clave requiere un nombre de columna (str) o lista de nombres.")

    def __setitem__(self, clave, valores):
        if isinstance(valores, Serie):
            lista_vals = list(valores.datos)
        elif isinstance(valores, (VectorNum, Arreglo)):
            lista_vals = list(valores.datos)
        elif isinstance(valores, (list, tuple)):
            lista_vals = list(valores)
        else:
            lista_vals = [valores] * self.numero_filas

        if self.numero_filas > 0 and len(lista_vals) != self.numero_filas:
            raise ValueError(f"Longitud de datos incompatible: {len(lista_vals)} vs {self.numero_filas} filas.")

        self._columnas[clave] = lista_vals

    def __repr__(self):
        encabezado = f"TablaDatos [{self.numero_filas} filas x {len(self._columnas)} columnas]:\n"
        columnas_info = "  Columnas: " + ", ".join(self.nombres_columnas) + "\n"
        filas_preview = []
        limite = min(5, self.numero_filas)
        for i in range(limite):
            fila_vals = [f"{col}: {repr(self._columnas[col][i])}" for col in self.nombres_columnas]
            filas_preview.append(f"  [{i}] " + ", ".join(fila_vals))
        if self.numero_filas > limite:
            filas_preview.append(f"  ... ({self.numero_filas - limite} filas más)")
        return encabezado + columnas_info + "\n".join(filas_preview)

    # =========================================================================
    # Operaciones de Selección, Filtrado y Transformación
    # =========================================================================

    def obtener_filas_xd(self):
        """Retorna una lista de diccionarios representando cada fila."""
        filas = []
        n_filas = self.numero_filas
        for i in range(n_filas):
            fila = {col: self._columnas[col][i] for col in self.nombres_columnas}
            filas.append(fila)
        return filas

    def seleccionar_xd(self, lista_columnas):
        """Genera una nueva tabla conservando únicamente las columnas indicadas."""
        nuevas = {}
        for col in lista_columnas:
            if col in self._columnas:
                nuevas[col] = list(self._columnas[col])
            else:
                raise KeyError(f"Columna '{col}' no encontrada en la tabla.")
        return TablaDatos(nuevas)

    def filtrar_xd(self, mascara):
        """Filtra los registros según una condición o máscara booleana."""
        if isinstance(mascara, (VectorNum, Arreglo)):
            mascara = mascara.datos

        nuevas = {col: [] for col in self.nombres_columnas}
        for i, condicion in enumerate(mascara):
            if condicion:
                for col in self.nombres_columnas:
                    nuevas[col].append(self._columnas[col][i])
        return TablaDatos(nuevas)

    def crear_columna_xd(self, nombre_columna, valores):
        """Añade o sobreescribe una columna calculada y retorna una nueva tabla."""
        nueva_tabla = TablaDatos({col: list(v) for col, v in self._columnas.items()})
        nueva_tabla[nombre_columna] = valores
        return nueva_tabla

    def ordenar_por_xd(self, columna, ascendente=True):
        """Ordena las filas según el valor de una columna especificada."""
        if columna not in self._columnas:
            raise KeyError(f"Columna de ordenamiento '{columna}' no encontrada.")

        filas = self.obtener_filas_xd()

        def clave_comparacion(f):
            valor = f[columna]
            if valor is None:
                return (1, 0)
            return (0, valor)

        filas_ordenadas = sorted(filas, key=clave_comparacion, reverse=not ascendente)
        nuevas = {col: [f[col] for f in filas_ordenadas] for col in self.nombres_columnas}
        return TablaDatos(nuevas)

    def renombrar_xd(self, mapeo_nombres):
        """Renombra columnas utilizando un diccionario {nombre_antiguo: nombre_nuevo}."""
        nuevas = {}
        for col, vals in self._columnas.items():
            nuevo_nombre = mapeo_nombres.get(col, col)
            nuevas[nuevo_nombre] = list(vals)
        return TablaDatos(nuevas)

    def eliminar_duplicados_xd(self, columnas_clave=None):
        """Elimina filas repetidas en la tabla."""
        if columnas_clave is None:
            columnas_clave = self.nombres_columnas

        vistos = set()
        filas_unicas = []
        for fila in self.obtener_filas_xd():
            clave = tuple(fila[c] for c in columnas_clave)
            if clave not in vistos:
                vistos.add(clave)
                filas_unicas.append(fila)

        nuevas = {col: [f[col] for f in filas_unicas] for col in self.nombres_columnas}
        return TablaDatos(nuevas)

    def eliminar_nulos_xd(self, columnas=None):
        """Descarta filas que contengan valores None o NaN en las columnas especificadas."""
        if columnas is None:
            columnas = self.nombres_columnas

        nuevas = {col: [] for col in self.nombres_columnas}
        for fila in self.obtener_filas_xd():
            tiene_nulo = False
            for col in columnas:
                val = fila[col]
                if val is None or (isinstance(val, float) and math.isnan(val)):
                    tiene_nulo = True
                    break
            if not tiene_nulo:
                for col in self.nombres_columnas:
                    nuevas[col].append(fila[col])
        return TablaDatos(nuevas)

    def rellenar_nulos_xd(self, valor_relleno, columnas=None):
        """Reemplaza valores nulos por un valor predeterminado."""
        if columnas is None:
            columnas = self.nombres_columnas

        nuevas = {}
        for col, vals in self._columnas.items():
            if col in columnas:
                nuevas[col] = [
                    valor_relleno if (v is None or (isinstance(v, float) and math.isnan(v))) else v
                    for v in vals
                ]
            else:
                nuevas[col] = list(vals)
        return TablaDatos(nuevas)

    # =========================================================================
    # Motor de Agrupamiento y Agregaciones (GroupBy)
    # =========================================================================

    def agrupar_por_xd(self, columnas_grupo):
        """Crea un objeto AgrupamientoTabla para realizar agregaciones."""
        if isinstance(columnas_grupo, str):
            columnas_grupo = [columnas_grupo]
        return AgrupamientoTabla(self, columnas_grupo)


class AgrupamientoTabla:
    """Gestiona la división de una tabla en grupos para calcular agregaciones."""

    def __init__(self, tabla: TablaDatos, columnas_grupo: list):
        self.tabla = tabla
        self.columnas_grupo = columnas_grupo
        self.grupos = self._construir_grupos()

    def _construir_grupos(self):
        grupos = {}
        for fila in self.tabla.obtener_filas_xd():
            clave = tuple(fila[col] for col in self.columnas_grupo)
            if clave not in grupos:
                grupos[clave] = []
            grupos[clave].append(fila)
        return grupos

    def resumir_xd(self, **agregaciones):
        """
        Calcula agregaciones para cada grupo.
        Uso: agrupado.resumir_xd(total_ventas=("precio", "suma"), prom=("unidades", "promedio"))
        """
        filas_resultado = []

        for clave_grupo, filas in self.grupos.items():
            fila_res = {}
            for idx_col, col_name in enumerate(self.columnas_grupo):
                fila_res[col_name] = clave_grupo[idx_col]

            # Subtabla del grupo
            sub_cols = {col: [f[col] for f in filas] for col in self.tabla.nombres_columnas}
            sub_tabla = TablaDatos(sub_cols)

            for nuevo_nombre, espec in agregaciones.items():
                if isinstance(espec, tuple):
                    col_origen, funcion = espec
                else:
                    col_origen = None
                    funcion = espec

                if funcion in ["conteo", "contar", "contar_papus"]:
                    fila_res[nuevo_nombre] = len(filas)
                else:
                    serie = sub_tabla[col_origen]
                    if funcion in ["suma", "sumar_momos"]:
                        fila_res[nuevo_nombre] = serie.suma_xd()
                    elif funcion in ["promedio", "media"]:
                        fila_res[nuevo_nombre] = serie.promedio_xd()
                    elif funcion == "mediana":
                        fila_res[nuevo_nombre] = serie.mediana_xd()
                    elif funcion in ["minimo", "el_mas_manco"]:
                        fila_res[nuevo_nombre] = serie.minimo_xd()
                    elif funcion in ["maximo", "el_mas_pro"]:
                        fila_res[nuevo_nombre] = serie.maximo_xd()
                    elif funcion in ["desviacion", "desviacion_pro", "desviacion_estandar"]:
                        fila_res[nuevo_nombre] = serie.desviacion_estandar_xd()
                    elif funcion == "varianza":
                        fila_res[nuevo_nombre] = serie.varianza_xd()
                    else:
                        raise ValueError(f"Función de agregación no reconocida: '{funcion}'")

            filas_resultado.append(fila_res)

        if not filas_resultado:
            cols = {col: [] for col in self.columnas_grupo + list(agregaciones.keys())}
            return TablaDatos(cols)

        columnas_finales = {
            col: [f[col] for f in filas_resultado]
            for col in self.columnas_grupo + list(agregaciones.keys())
        }
        return TablaDatos(columnas_finales)


# Alias para retrocompatibilidad
AgruparPor = AgrupamientoTabla


# =============================================================================
# Motor CSV Propio desde Cero (Parser de Texto con Autómata de Estados)
# =============================================================================

def _parsear_linea_csv(linea: str, delimitador: str = ",") -> list:
    """Parsea una línea de texto CSV respetando comillas y caracteres de escape."""
    campos = []
    actual = []
    en_comillas = False
    i = 0
    longitud = len(linea)

    while i < longitud:
        char = linea[i]
        if char == '"':
            if en_comillas and i + 1 < longitud and linea[i + 1] == '"':
                actual.append('"')
                i += 1
            else:
                en_comillas = not en_comillas
        elif char == delimitador and not en_comillas:
            campos.append("".join(actual).strip())
            actual = []
        else:
            actual.append(char)
        i += 1

    campos.append("".join(actual).strip())
    return campos


def _inferir_tipo_dato(valor_str: str):
    """Convierte cadenas a tipos numéricos (int, float) o conserva la cadena."""
    val = valor_str.strip()
    if val == "" or val.lower() in ["none", "null", "nan"]:
        return None
    try:
        if "." in val:
            return float(val)
        return int(val)
    except ValueError:
        try:
            return float(val)
        except ValueError:
            return val


def cargar_csv_xd(ruta_archivo: str, delimitador: str = ",") -> TablaDatos:
    """Lee un archivo CSV sin librerías externas y lo carga en una TablaDatos."""
    with open(ruta_archivo, mode="r", encoding="utf-8") as f:
        lineas = [l.rstrip("\r\n") for l in f if l.strip()]

    if not lineas:
        return TablaDatos()

    encabezados = _parsear_linea_csv(lineas[0], delimitador)
    columnas = {h: [] for h in encabezados}

    for linea in lineas[1:]:
        valores = _parsear_linea_csv(linea, delimitador)
        for h, v in zip(encabezados, valores):
            columnas[h].append(_inferir_tipo_dato(v))

    return TablaDatos(columnas)


def guardar_csv_xd(tabla: TablaDatos, ruta_salida: str, delimitador: str = ","):
    """Exporta una TablaDatos a formato CSV estándar."""
    with open(ruta_salida, mode="w", encoding="utf-8") as f:
        encabezado = delimitador.join(tabla.nombres_columnas) + "\n"
        f.write(encabezado)

        for fila in tabla.obtener_filas_xd():
            linea_vals = []
            for col in tabla.nombres_columnas:
                val = fila[col]
                if val is None:
                    linea_vals.append("")
                elif isinstance(val, str) and (delimitador in val or '"' in val or "\n" in val):
                    escapado = val.replace('"', '""')
                    linea_vals.append(f'"{escapado}"')
                else:
                    linea_vals.append(str(val))
            f.write(delimitador.join(linea_vals) + "\n")
