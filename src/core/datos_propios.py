"""
Librería Datos Propios (Reemplazo propio de Pandas desde cero en español xd)
"""

import csv
import math
from src.core.matematica_propia import Arreglo

class Serie:
    """Clase Serie que representa una columna de datos con un nombre e índice xd"""
    def __init__(self, datos, nombre="columna"):
        self.nombre = nombre
        if isinstance(datos, Arreglo):
            self.arreglo = datos
        else:
            self.arreglo = Arreglo(datos)

    @property
    def datos(self):
        return self.arreglo.datos

    def __len__(self):
        return len(self.arreglo)

    def __getitem__(self, idx):
        res = self.arreglo[idx]
        if isinstance(res, Arreglo):
            return Serie(res, nombre=self.nombre)
        return res

    def __repr__(self):
        return f"Serie(nombre='{self.nombre}', datos={repr(self.datos)})"

    # Delegación de operaciones estadísticas a Arreglo con sufijo _xd
    def suma_xd(self): return self.arreglo.suma_xd()
    def promedio_xd(self): return self.arreglo.promedio_xd()
    def mediana_xd(self): return self.arreglo.mediana_xd()
    def minimo_xd(self): return self.arreglo.minimo_xd()
    def maximo_xd(self): return self.arreglo.maximo_xd()
    def desviacion_estandar_xd(self): return self.arreglo.desviacion_estandar_xd()
    def conteo_xd(self): return self.arreglo.conteo_xd()


class TablaDatos:
    """Clase TablaDatos (DataFrame propio) para almacenamiento y manipulación de datos tabulares xd"""
    def __init__(self, columnas=None):
        self.columnas = {}
        if columnas:
            for k, v in columnas.items():
                if isinstance(v, Serie):
                    self.columnas[k] = list(v.datos)
                elif isinstance(v, Arreglo):
                    self.columnas[k] = list(v.datos)
                else:
                    self.columnas[k] = list(v)

    @property
    def nombres_columnas(self):
        return list(self.columnas.keys())

    @property
    def numero_filas(self):
        if not self.columnas:
            return 0
        primera_col = next(iter(self.columnas.values()))
        return len(primera_col)

    def __getitem__(self, item):
        if isinstance(item, str):
            if item not in self.columnas:
                raise KeyError(f"La columna '{item}' no existe en la TablaDatos.")
            return Serie(self.columnas[item], nombre=item)
        raise TypeError("El índice debe ser el nombre de una columna (str).")

    def __setitem__(self, key, value):
        if isinstance(value, Serie):
            val_list = list(value.datos)
        elif isinstance(value, Arreglo):
            val_list = list(value.datos)
        elif isinstance(value, list):
            val_list = list(value)
        else:
            val_list = [value] * self.numero_filas
        self.columnas[key] = val_list

    def __repr__(self):
        filas_str = [f"TablaDatos con {self.numero_filas} filas y {len(self.columnas)} columnas:"]
        filas_str.append("Columnas: " + ", ".join(self.nombres_columnas))
        return "\n".join(filas_str)

    # --- Métodos de Manipulación y Transformación ---

    def obtener_filas_xd(self):
        """Retorna las filas como una lista de diccionarios xd"""
        filas = []
        n_filas = self.numero_filas
        for i in range(n_filas):
            fila = {col: self.columnas[col][i] for col in self.columnas}
            filas.append(fila)
        return filas

    def seleccionar_xd(self, lista_columnas):
        """Retorna una nueva TablaDatos únicamente con las columnas seleccionadas xd"""
        nuevas_cols = {}
        for col in lista_columnas:
            if col in self.columnas:
                nuevas_cols[col] = list(self.columnas[col])
            else:
                raise KeyError(f"Columna '{col}' no encontrada en la tabla.")
        return TablaDatos(nuevas_cols)

    def filtrar_xd(self, mascara_booleana):
        """Filtra la tabla según una lista/máscara booleana xd"""
        if isinstance(mascara_booleana, Arreglo):
            mascara_booleana = mascara_booleana.datos

        nuevas_cols = {col: [] for col in self.columnas}
        for i, coincide in enumerate(mascara_booleana):
            if coincide:
                for col in self.columnas:
                    nuevas_cols[col].append(self.columnas[col][i])
        return TablaDatos(nuevas_cols)

    def crear_columna_xd(self, nombre_columna, valores):
        """Agrega o reemplaza una columna calculada xd"""
        nueva_tabla = TablaDatos({c: list(vals) for c, vals in self.columnas.items()})
        nueva_tabla[nombre_columna] = valores
        return nueva_tabla

    def ordenar_por_xd(self, columna, ascendente=True):
        """Ordena las filas según los valores de una columna xd"""
        if columna not in self.columnas:
            raise KeyError(f"Columna '{columna}' no existe.")

        filas = self.obtener_filas_xd()
        def clave_orden(f):
            v = f[columna]
            return (v is None, v)

        filas_ordenadas = sorted(filas, key=clave_orden, reverse=not ascendente)
        nuevas_cols = {col: [f[col] for f in filas_ordenadas] for col in self.columnas}
        return TablaDatos(nuevas_cols)

    def renombrar_xd(self, mapa_nombres):
        """Renombra columnas según un diccionario {viejo: nuevo} xd"""
        nuevas_cols = {}
        for col, vals in self.columnas.items():
            nuevo_nombre = mapa_nombres.get(col, col)
            nuevas_cols[nuevo_nombre] = list(vals)
        return TablaDatos(nuevas_cols)

    def eliminar_duplicados_xd(self, columnas_clave=None):
        """Elimina filas duplicadas xd"""
        if columnas_clave is None:
            columnas_clave = self.nombres_columnas

        filas = self.obtener_filas_xd()
        vistos = set()
        filas_unicas = []

        for f in filas:
            clave = tuple(f[col] for col in columnas_clave)
            if clave not in vistos:
                vistos.add(clave)
                filas_unicas.append(f)

        nuevas_cols = {col: [f[col] for f in filas_unicas] for col in self.columnas}
        return TablaDatos(nuevas_cols)

    def eliminar_nulos_xd(self, columnas=None):
        """Elimina filas que contengan valores None o NaN en las columnas especificadas xd"""
        if columnas is None:
            columnas = self.nombres_columnas

        filas = self.obtener_filas_xd()
        filas_limpias = []

        for f in filas:
            tiene_nulo = False
            for col in columnas:
                val = f[col]
                if val is None or (isinstance(val, float) and math.isnan(val)):
                    tiene_nulo = True
                    break
            if not tiene_nulo:
                filas_limpias.append(f)

        nuevas_cols = {col: [f[col] for f in filas_limpias] for col in self.columnas}
        return TablaDatos(nuevas_cols)

    def rellenar_nulos_xd(self, valor_relleno, columnas=None):
        """Reemplaza valores nulos por un valor predeterminado xd"""
        if columnas is None:
            columnas = self.nombres_columnas

        nuevas_cols = {}
        for col, vals in self.columnas.items():
            if col in columnas:
                nuevos_vals = []
                for v in vals:
                    if v is None or (isinstance(v, float) and math.isnan(v)):
                        nuevos_vals.append(valor_relleno)
                    else:
                        nuevos_vals.append(v)
                nuevas_cols[col] = nuevos_vals
            else:
                nuevas_cols[col] = list(vals)

        return TablaDatos(nuevas_cols)

    def agrupar_por_xd(self, columnas_agrupar):
        """Crea un objeto AgruparPor para operaciones de agregación xd"""
        if isinstance(columnas_agrupar, str):
            columnas_agrupar = [columnas_agrupar]
        return AgruparPor(self, columnas_agrupar)

    def resumen_xd(self):
        """Genera un diccionario con estadísticas descriptivas de cada columna xd"""
        resumen = {}
        for col in self.nombres_columnas:
            serie = self[col]
            validos = serie.arreglo.obtener_validos_xd()
            es_numerica = len(validos) > 0 and len(validos) == len([x for x in serie.datos if x is not None])
            if es_numerica:
                resumen[col] = {
                    "tipo": "numérica",
                    "conteo": serie.conteo_xd(),
                    "promedio": serie.promedio_xd(),
                    "mediana": serie.mediana_xd(),
                    "minimo": serie.minimo_xd(),
                    "maximo": serie.maximo_xd(),
                    "desviacion_estandar": serie.desviacion_estandar_xd()
                }
            else:
                conteo_valores = {}
                for x in serie.datos:
                    conteo_valores[str(x)] = conteo_valores.get(str(x), 0) + 1
                resumen[col] = {
                    "tipo": "categórica",
                    "conteo": len(serie.datos),
                    "valores_unicos": len(conteo_valores),
                    "frecuencias": conteo_valores
                }
        return resumen


class AgruparPor:
    """Clase AgruparPor para realizar agrupamientos y agregaciones en datos tabulares xd"""
    def __init__(self, tabla, columnas_agrupar):
        self.tabla = tabla
        self.columnas_agrupar = columnas_agrupar
        self.grupos = {}
        self._construir_grupos_xd()

    def _construir_grupos_xd(self):
        filas = self.tabla.obtener_filas_xd()
        for f in filas:
            clave = tuple(f[col] for col in self.columnas_agrupar)
            if clave not in self.grupos:
                self.grupos[clave] = []
            self.grupos[clave].append(f)

    def resumir_xd(self, **especificaciones_agregacion):
        """
        Calcula agregaciones por grupo.
        Ejemplo: resumir_xd(ingreso_total=('ingreso', 'suma'), ingreso_promed=('ingreso', 'promedio')) xd
        """
        resultado_cols = {col: [] for col in self.columnas_agrupar}
        for alias in especificaciones_agregacion:
            resultado_cols[alias] = []

        for clave, filas_grupo in self.grupos.items():
            for idx, col in enumerate(self.columnas_agrupar):
                resultado_cols[col].append(clave[idx])

            for alias, (col_origen, funcion_agg) in especificaciones_agregacion.items():
                valores = [f[col_origen] for f in filas_grupo if f[col_origen] is not None]
                arr = Arreglo(valores)

                if funcion_agg in ("suma", "sum"):
                    val_agg = arr.suma_xd()
                elif funcion_agg in ("promedio", "media", "mean"):
                    val_agg = arr.promedio_xd()
                elif funcion_agg in ("mediana", "median"):
                    val_agg = arr.mediana_xd()
                elif funcion_agg in ("minimo", "min"):
                    val_agg = arr.minimo_xd()
                elif funcion_agg in ("maximo", "max"):
                    val_agg = arr.maximo_xd()
                elif funcion_agg in ("desviacion_estandar", "std"):
                    val_agg = arr.desviacion_estandar_xd()
                elif funcion_agg in ("conteo", "count"):
                    val_agg = len(filas_grupo)
                else:
                    raise ValueError(f"Función de agregación desconocida: '{funcion_agg}' xd")

                resultado_cols[alias].append(val_agg)

        return TablaDatos(resultado_cols)


# --- Funciones IO de Archivos (CSV) desde Cero ---

def _convertir_valor_xd(val_str):
    """Parsea cadenas a int, float, bool o None xd"""
    v = val_str.strip()
    if not v or v.lower() in ("null", "none", "nan", "na"):
        return None
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    try:
        if "." in v:
            return float(v)
        return int(v)
    except ValueError:
        return v

def cargar_csv_xd(ruta_archivo, separador=",", encabezado=True):
    """Carga un archivo CSV y retorna una TablaDatos propia desde cero xd"""
    columnas_datos = {}
    with open(ruta_archivo, mode="r", encoding="utf-8-sig") as f:
        reader = csv.reader(f, delimiter=separador)
        filas = list(reader)

    if not filas:
        return TablaDatos()

    if encabezado:
        nombres_cols = [c.strip() for c in filas[0]]
        filas_datos = filas[1:]
    else:
        nombres_cols = [f"col_{i}" for i in range(len(filas[0]))]
        filas_datos = filas

    for idx, col in enumerate(nombres_cols):
        vals = [_convertir_valor_xd(fila[idx]) if idx < len(fila) else None for fila in filas_datos]
        columnas_datos[col] = vals

    return TablaDatos(columnas_datos)

def guardar_csv_xd(tabla, ruta_archivo, separador=","):
    """Guarda una TablaDatos en un archivo CSV desde cero xd"""
    with open(ruta_archivo, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f, delimiter=separador)
        writer.writerow(tabla.nombres_columnas)
        for fila in tabla.obtener_filas_xd():
            writer.writerow([fila[col] for col in tabla.nombres_columnas])
