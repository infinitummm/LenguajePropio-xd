"""
Librería de Manipulación de Datos Tabulares - Motor Tabular MomoLang XD
======================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación 100% desde cero en Python puro (sin Pandas ni NumPy)
para Series, Tablas bidimensionales (TablaMomo), filtrado, ordenamiento,
creación de columnas, agrupamientos (GroupBy) y lectura/escritura de CSV.
"""

import os
from src.core.matematica_propia import VectorMomo


def inferir_tipo_valor(texto):
    """Convierte cadenas a tipos de Python nativos (int, float, o conserva str/None)."""
    if texto is None:
        return None
    val_limpio = texto.strip()
    if val_limpio == "":
        return None
    # Intento de entero
    try:
        if val_limpio.startswith("+") or val_limpio.startswith("-"):
            signo = val_limpio[0]
            resto = val_limpio[1:]
            if resto.isdigit():
                return int(val_limpio)
        elif val_limpio.isdigit():
            return int(val_limpio)
    except ValueError:
        pass
    # Intento de float
    try:
        return float(val_limpio)
    except ValueError:
        pass
    # Valor booleano
    if val_limpio.lower() in ("true", "verdadero", "si"):
        return True
    if val_limpio.lower() in ("false", "falso", "no"):
        return False
    return val_limpio


def parsear_csv_propio(contenido_csv, separador=","):
    """
    Autómata de estados finitos propio para parsear CSV.
    Maneja comillas dobles, comillas escapadas (""), comas internas y saltos de línea.
    """
    filas = []
    fila_actual = []
    campo_actual = []
    en_comillas = False
    i = 0
    n = len(contenido_csv)

    while i < n:
        char = contenido_csv[i]

        if en_comillas:
            if char == '"':
                # Comilla escapada: ""
                if i + 1 < n and contenido_csv[i + 1] == '"':
                    campo_actual.append('"')
                    i += 1
                else:
                    en_comillas = False
            else:
                campo_actual.append(char)
        else:
            if char == '"':
                en_comillas = True
            elif char == separador:
                fila_actual.append("".join(campo_actual).strip())
                campo_actual = []
            elif char == chr(13):
                # Posible CRLF
                if i + 1 < n and contenido_csv[i + 1] == chr(10):
                    i += 1
                fila_actual.append("".join(campo_actual).strip())
                campo_actual = []
                if fila_actual and any(c != "" for c in fila_actual):
                    filas.append(fila_actual)
                fila_actual = []
            elif char == chr(10):
                fila_actual.append("".join(campo_actual).strip())
                campo_actual = []
                if fila_actual and any(c != "" for c in fila_actual):
                    filas.append(fila_actual)
                fila_actual = []
            else:
                campo_actual.append(char)
        i += 1

    # Último campo si no terminó en salto de línea
    if campo_actual or fila_actual:
        fila_actual.append("".join(campo_actual).strip())
        if any(c != "" for c in fila_actual):
            filas.append(fila_actual)

    return filas


class SerieMomo:
    """Representa una columna individual de datos con nombre y vector numérico/objeto."""

    def __init__(self, datos=None, nombre="columna"):
        self.nombre = nombre
        if isinstance(datos, VectorMomo):
            self.vector = datos
        elif isinstance(datos, (list, tuple)):
            self.vector = VectorMomo(list(datos))
        else:
            self.vector = VectorMomo([datos] if datos is not None else [])

    @property
    def datos(self):
        return self.vector.datos

    def __len__(self):
        return len(self.vector)

    def __iter__(self):
        return iter(self.vector)

    def __repr__(self):
        return f"SerieMomo(nombre='{self.nombre}', n={len(self.vector)})"

    def __getitem__(self, idx):
        res = self.vector[idx]
        if isinstance(res, VectorMomo):
            return SerieMomo(res, nombre=self.nombre)
        return res

    def __setitem__(self, idx, val):
        self.vector[idx] = val

    # Métodos estadísticos delegados al VectorMomo
    def suma(self):
        return self.vector.suma()

    def promedio(self):
        return self.vector.promedio()

    def media(self):
        return self.vector.media()

    def mediana(self):
        return self.vector.mediana()

    def el_mas_pro(self):
        return self.vector.el_mas_pro()

    def el_mas_manco(self):
        return self.vector.el_mas_manco()

    def desviacion_pro(self):
        return self.vector.desviacion_pro()

    def contar_papus(self):
        return self.vector.contar_papus()


class TablaMomo:
    """
    Estructura tabular bidimensional en Python puro (DataFrame propio)
    con operaciones nativas para MomoLang XD.
    """

    def __init__(self, datos_dict=None):
        self._columnas = {}
        self._num_filas = 0

        if datos_dict:
            for col_nombre, col_datos in datos_dict.items():
                if isinstance(col_datos, SerieMomo):
                    self._columnas[col_nombre] = col_datos
                else:
                    self._columnas[col_nombre] = SerieMomo(col_datos, nombre=col_nombre)
            if self._columnas:
                primera = next(iter(self._columnas.values()))
                self._num_filas = len(primera)

    @property
    def columnas(self):
        return list(self._columnas.keys())

    @property
    def num_filas(self):
        return self._num_filas

    def __len__(self):
        return self._num_filas

    def __contains__(self, nombre_col):
        return nombre_col in self._columnas

    def __getitem__(self, clave):
        if isinstance(clave, str):
            if clave not in self._columnas:
                raise KeyError(f"La columna '{clave}' no existe en la tabla. Columnas disponibles: {self.columnas}")
            return self._columnas[clave]
        elif isinstance(clave, list):
            # Selección de lista de columnas
            return self.escojo_a(clave)
        elif isinstance(clave, VectorMomo):
            # Filtrado por máscara booleana
            return self.but_te_enteras_que(clave)
        raise TypeError(f"Tipo de clave no soportado para TablaMomo: {type(clave)}")

    def __setitem__(self, nombre_col, valores):
        self.el_futuro_es_hoy_oiste_viejo(nombre_col, valores)

    # -------------------------------------------------------------------------
    # Métodos con Nombres de Momos (Operaciones Centrales del DSL)
    # -------------------------------------------------------------------------

    @classmethod
    def pasa_el_pack(cls, ruta_archivo, separador=","):
        """Carga un archivo CSV utilizando el parser de autómata finito propio."""
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"No se encontro el archivo CSV: '{ruta_archivo}' xd")

        with open(ruta_archivo, 'r', encoding='utf-8', errors='replace') as f:
            contenido = f.read()

        filas = parsear_csv_propio(contenido, separador=separador)
        if not filas:
            return cls({})

        encabezados = [h.strip() for h in filas[0]]
        columnas_datos = {h: [] for h in encabezados}

        for fila in filas[1:]:
            for col_idx, enc in enumerate(encabezados):
                if col_idx < len(fila):
                    val = inferir_tipo_valor(fila[col_idx])
                else:
                    val = None
                columnas_datos[enc].append(val)

        return cls(columnas_datos)

    def subir_al_grupo(self, ruta_archivo, separador=","):
        """Exporta la tabla a un archivo CSV formateando comillas según sea necesario."""
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

        with open(ruta_archivo, 'w', encoding='utf-8') as f:
            # Escribir encabezados
            f.write(separador.join(self.columnas) + chr(10))
            # Escribir filas
            for i in range(self._num_filas):
                linea = []
                for col in self.columnas:
                    val = self._columnas[col][i]
                    if val is None:
                        linea.append("")
                    else:
                        str_val = str(val)
                        if separador in str_val or '"' in str_val or chr(10) in str_val:
                            str_val = '"' + str_val.replace('"', '""') + '"'
                        linea.append(str_val)
                f.write(separador.join(linea) + chr(10))

    def escojo_a(self, lista_columnas):
        """Selecciona únicamente las columnas especificadas."""
        if isinstance(lista_columnas, str):
            lista_columnas = [lista_columnas]
        nuevas_columnas = {}
        for col in lista_columnas:
            if col not in self._columnas:
                raise KeyError(f"No se puede seleccionar la columna '{col}' porque no existe. Columnas disponibles: {self.columnas}")
            nuevas_columnas[col] = SerieMomo(self._columnas[col].vector, nombre=col)
        return TablaMomo(nuevas_columnas)

    def but_te_enteras_que(self, mascara_booleana):
        """Filtra las filas de la tabla según una máscara booleana."""
        if isinstance(mascara_booleana, VectorMomo):
            mascara = mascara_booleana.datos
        elif isinstance(mascara_booleana, (list, tuple)):
            mascara = list(mascara_booleana)
        else:
            raise TypeError(f"El filtro requiere una máscara booleana, no {type(mascara_booleana)}")

        if len(mascara) != self._num_filas:
            raise ValueError(f"La máscara de filtrado ({len(mascara)}) no coincide con el número de filas ({self._num_filas}).")

        indices_validos = [i for i, m in enumerate(mascara) if bool(m)]
        nuevas_columnas = {}
        for col, serie in self._columnas.items():
            nuevas_columnas[col] = [serie.datos[i] for i in indices_validos]
        return TablaMomo(nuevas_columnas)

    def el_futuro_es_hoy_oiste_viejo(self, nombre_columna, valores):
        """Crea o actualiza una columna calculada."""
        if isinstance(valores, (VectorMomo, SerieMomo)):
            lista_valores = valores.datos
        elif isinstance(valores, (list, tuple)):
            lista_valores = list(valores)
        else:
            # Valor escalar repetido
            lista_valores = [valores] * self._num_filas

        if self._num_filas > 0 and len(lista_valores) != self._num_filas:
            raise ValueError(
                f"No coinciden las dimensiones: la columna calculada tiene {len(lista_valores)} elementos "
                f"pero la tabla tiene {self._num_filas} filas."
            )

        self._columnas[nombre_columna] = SerieMomo(lista_valores, nombre=nombre_columna)
        if self._num_filas == 0:
            self._num_filas = len(lista_valores)
        return self

    def ordenar_a_los_papus(self, columna, ascendente=True):
        """Ordena las filas de la tabla de acuerdo a una columna."""
        if columna not in self._columnas:
            raise KeyError(f"No se puede ordenar por '{columna}' porque no existe. Columnas disponibles: {self.columnas}")

        valores = self._columnas[columna].datos
        
        # Función clave para ordenar tratando None al final
        def clave_orden(idx):
            v = valores[idx]
            if v is None:
                return (1, 0)
            return (0, v)

        indices_ordenados = sorted(range(self._num_filas), key=clave_orden, reverse=not ascendente)
        nuevas_columnas = {}
        for col, serie in self._columnas.items():
            nuevas_columnas[col] = [serie.datos[i] for i in indices_ordenados]
        return TablaMomo(nuevas_columnas)

    def tratar_datos_faltantes(self, columna=None, valor_relleno=0, eliminar=False):
        """Manejo y limpieza de valores nulos o celdas vacías."""
        if eliminar:
            # Elimina filas donde haya valores None
            mascara = []
            cols_revisar = [columna] if columna else self.columnas
            for i in range(self._num_filas):
                fila_valida = all(self._columnas[c][i] is not None for c in cols_revisar)
                mascara.append(fila_valida)
            return self.but_te_enteras_que(mascara)
        else:
            # Rellena los valores None con valor_relleno
            cols_rellenar = [columna] if columna else self.columnas
            for c in cols_rellenar:
                nuevos_datos = [valor_relleno if x is None else x for x in self._columnas[c].datos]
                self._columnas[c] = SerieMomo(nuevos_datos, nombre=c)
            return self

    def juntar_a_la_grasa_por(self, columnas_clave):
        """Inicia el agrupamiento por una o varias columnas clave."""
        if isinstance(columnas_clave, str):
            columnas_clave = [columnas_clave]
        for col in columnas_clave:
            if col not in self._columnas:
                raise KeyError(f"No se puede agrupar por '{col}' porque no existe en la tabla. Columnas: {self.columnas}")
        return AgrupamientoMomo(self, columnas_clave)

    def ver_primeras_filas(self, n=5):
        """Muestra una vista previa en consola de las primeras filas de la tabla."""
        limite = min(n, self._num_filas)
        lineas = []
        lineas.append(" | ".join(f"{c:>15}" for c in self.columnas))
        lineas.append("-" * (18 * len(self.columnas)))
        for i in range(limite):
            fila_str = [str(self._columnas[c][i]) if self._columnas[c][i] is not None else "None" for c in self.columnas]
            lineas.append(" | ".join(f"{v:>15}" for v in fila_str))
        return chr(10).join(lineas)

    def __repr__(self):
        return f"TablaMomo({self._num_filas} filas x {len(self._columnas)} columnas: {self.columnas})"


class AgrupamientoMomo:
    """Estructura para procesar grupos de datos y aplicar agregaciones estadísticas múltiples."""

    def __init__(self, tabla, columnas_clave):
        self.tabla = tabla
        self.columnas_clave = columnas_clave
        self.grupos = {}  # {clave_tupla: [indices_filas]}

        for i in range(tabla.num_filas):
            clave = tuple(tabla[c][i] for c in columnas_clave)
            if clave not in self.grupos:
                self.grupos[clave] = []
            self.grupos[clave].append(i)

    def sacar_cuentas(self, lista_agregaciones):
        """
        Aplica múltiples agregaciones simultáneamente sobre cada grupo.
        lista_agregaciones: lista de tuplas (nombre_salida, funcion_nombre, col_origen)
        """
        datos_resultado = {col: [] for col in self.columnas_clave}
        for nombre_salida, _, _ in lista_agregaciones:
            datos_resultado[nombre_salida] = []

        # Ordenar claves de grupo para consistencia y reproducibilidad
        claves_ordenadas = sorted(self.grupos.keys(), key=lambda k: tuple(str(x) for x in k))

        for clave_grupo in claves_ordenadas:
            indices_grupo = self.grupos[clave_grupo]

            # Agregar valores de clave
            for col_idx, col_nombre in enumerate(self.columnas_clave):
                datos_resultado[col_nombre].append(clave_grupo[col_idx])

            # Calcular cada función de agregación solicitada
            for nombre_salida, func_nombre, col_origen in lista_agregaciones:
                func_limpia = func_nombre.lower().strip()

                if func_limpia in ("contar_papus", "conteo", "contar"):
                    datos_resultado[nombre_salida].append(len(indices_grupo))
                else:
                    if col_origen not in self.tabla.columnas:
                        raise KeyError(f"La columna '{col_origen}' especificada en {func_nombre}() no existe en la tabla.")
                    
                    valores_grupo = [self.tabla[col_origen][i] for i in indices_grupo]
                    vector = VectorMomo(valores_grupo)

                    if func_limpia in ("suma", "sumar", "sumar_momos", "sumar_papus"):
                        res = vector.suma()
                    elif func_limpia in ("promedio", "media"):
                        res = vector.promedio()
                    elif func_limpia == "mediana":
                        res = vector.mediana()
                    elif func_limpia in ("el_mas_pro", "maximo", "max"):
                        res = vector.el_mas_pro()
                    elif func_limpia in ("el_mas_manco", "minimo", "min"):
                        res = vector.el_mas_manco()
                    elif func_limpia in ("desviacion_pro", "desviacion"):
                        res = vector.desviacion_pro()
                    else:
                        raise ValueError(f"Función de agregación desconocida: '{func_nombre}'")

                    datos_resultado[nombre_salida].append(res)

        return TablaMomo(datos_resultado)
