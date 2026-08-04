# Documento de Alcance y Catálogo de Instrucciones - Corte 1

## 1. Delimitación del Dominio y Casos de Uso
El DSL **LenguajeDatos** es un lenguaje de dominio específico diseñado para expresar flujos reproducibles de ciencia de datos: carga de archivos tabulares, selección y limpieza de variables, transformaciones numéricas, agrupamientos y generación de visualizaciones vectoriales (SVG).

### Usuarios Objetivo
Estudiantes, analistas de datos e investigadores que requieren realizar análisis exploratorio de datos (EDA) mediante una sintaxis declarativa, concisa y comprensible en español, alimentada por motores internos propios en Python.

### Entradas y Salidas
- **Entradas:** Archivos de código fuente con extensión `.dsl` y conjuntos de datos en formato `.csv`.
- **Salidas:** Archivos de datos procesados en formato `.csv` y representaciones gráficas en formato `.svg`.

---

## 2. Catálogo de Instrucciones y Palabras Reservadas

| Categoría | Instrucción / Palabra Reservada | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- | :--- |
| **Carga / Guardado** | `cargar_csv_xd` | Carga un archivo CSV y devuelve una tabla. | `ventas = cargar_csv_xd "datos.csv"` |
| | `guardar_csv_xd` | Exporta una tabla a un archivo CSV. | `guardar_csv_xd resumen "salida.csv"` |
| **Selección y Limpieza** | `seleccionar_xd` | Selecciona columnas específicas. | `df \|> seleccionar_xd [fecha, ciudad]` |
| | `filtrar_xd` | Filtra filas por una condición booleana. | `df \|> filtrar_xd unidades > 10` |
| | `ordenar_por_xd` | Ordena las filas según una columna. | `df \|> ordenar_por_xd precio` |
| | `renombrar_xd` | Renombra una o más columnas. | `df \|> renombrar_xd [viejo: nuevo]` |
| | `eliminar_duplicados_xd` | Elimina filas repetidas. | `df \|> eliminar_duplicados_xd` |
| | `eliminar_nulos_xd` | Elimina filas con valores faltantes. | `df \|> eliminar_nulos_xd` |
| | `rellenar_nulos_xd` | Reemplaza valores nulos por un valor. | `df \|> rellenar_nulos_xd 0` |
| **Transformación** | `crear_columna_xd` | Crea o modifica una columna calculada. | `df \|> crear_columna_xd total = u * p` |
| **Agrupamiento** | `agrupar_por_xd` | Agrupa filas por una o más variables. | `df \|> agrupar_por_xd [ciudad]` |
| | `resumir_xd` | Aplica agregaciones por grupo (`suma`, `promedio`, `minimo`, `maximo`, `conteo`). | `df \|> resumir_xd total = suma(total)` |
| **Visualización** | `graficar_barras_xd` | Produce un gráfico de barras. | `graficar_barras_xd resumen` |
| | `graficar_lineas_xd` | Produce un gráfico de líneas. | `graficar_lineas_xd serie_tiempo` |
| | `graficar_histograma_xd`| Produce un histograma de frecuencias. | `graficar_histograma_xd df` |
| | `graficar_dispersion_xd`| Produce un gráfico de dispersión X-Y. | `graficar_dispersion_xd df` |
| | `graficar_cajas_xd` | Produce un gráfico de cajas (Boxplot). | `graficar_cajas_xd df` |
