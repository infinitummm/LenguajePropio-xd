# Documento de Alcance y Catálogo de Instrucciones - Corte 1
## Lenguaje de Dominio Específico: MomoLang XD (`.xd`)

**Asignatura:** Lenguajes de Programación y Transducción  
**Universidad Sergio Arboleda** — Programa de Ciencias de la Computación e Inteligencia Artificial  
**Docente:** Joaquín F. Sánchez | **Semestre:** 2026-2

---

## 1. Delimitación del Dominio y Casos de Uso

**MomoLang XD** es un Lenguaje de Dominio Específico (DSL) declarativo y temático diseñado para expresar flujos reproducibles de ciencia de datos: carga de archivos tabulares (CSV), selección y filtrado de variables, creación de columnas calculadas, agrupamientos con estadísticas descriptivas, exportación de resultados y generación de visualizaciones vectoriales (SVG).

El lenguaje adopta una sintaxis distintiva basada en la **cultura de momos / memes hispanoamericanos** y una regla sintáctica fundamental: **cada sentencia del lenguaje debe terminar obligatoriamente con el sufijo `xd`**.

### Usuarios Objetivo
* Estudiantes, analistas de datos e investigadores que buscan describir canalizaciones de análisis de datos de manera legible, declarativa y divertida.
* Desarrolladores interesados en lenguajes de dominio específico construidos con **ANTLR4** y motores propios de ejecución en Python.

### Entradas y Salidas
* **Entradas:** Archivos de código fuente con extensión `.xd` y archivos de datos en formato `.csv`.
* **Salidas:** Reporte léxico/sintáctico en consola (Aceptado/Rechazado con árbol de análisis sintáctico), archivos de datos procesados `.csv` y gráficos `.svg`.

### Restricciones del Sistema
* **Corte 1:** El sistema actúa como un reconocedor formal (Lexer y Parser generados con ANTLR4) que acepta programas correctos o los rechaza con diagnóstico detallado (línea, columna y sugerencia contextual).
* **Motor Propio:** El procesamiento de datos no utiliza librerías de terceros (como Pandas, NumPy o Matplotlib), sino librerías propias desarrolladas en Python desde cero.

---

## 2. Catálogo de Instrucciones y Palabras Reservadas

A continuación se detalla el conjunto de palabras reservadas, operadores y sintaxis que componen **MomoLang XD**:

### 2.1 Terminador Obligatorio
* **`xd`** (o `XD` / `xD`): Delimitador final obligatorio para todas las sentencias del lenguaje.

### 2.2 Impresión en Consola
| Instrucción / Palabra Reservada | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| `when haces` | Imprime cadenas de texto, identificadores o expresiones en consola. | `when haces "Iniciando analisis de datos papu..." xd` |

### 2.3 Carga y Almacenamiento
| Instrucción / Palabra Reservada | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| `pasa_el_pack` / `pasa_el_zelda` / `robar_momo` | Carga un archivo CSV y devuelve una referencia tabular. | `ventas = pasa_el_pack "datos/ventas.csv" xd` |
| `separador` | Especifica un delimitador personalizado para el archivo CSV. | `datos = pasa_el_pack "datos.csv" separador ";" xd` |
| `subir_al_grupo` / `guardar_momo` | Exporta un conjunto de datos transformado a formato CSV. | `subir_al_grupo resumen en "salidas/resumen.csv" xd` |

### 2.4 Operador de Tubería (Pipeline)
* **`|:v>`** (o `|>`): Conecta secuencialmente transformaciones de datos, pasando el resultado de una operación a la siguiente.

### 2.5 Transformación y Limpieza en Pipeline
| Instrucción / Palabra Reservada | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| `escojo_a` / `escojo_a_los_papus` | Selecciona un subconjunto de columnas. | `\|:v> escojo_a [fecha, ciudad, total]` |
| `but_te_enteras_que` / `but_ella_no_te_ama` | Filtra registros mediante una condición booleana. | `\|:v> but_te_enteras_que unidades > 10` |
| `el_futuro_es_hoy_oiste_viejo` / `metanle_sabor_a` | Crea o modifica una columna calculada con expresiones aritméticas. | `\|:v> el_futuro_es_hoy_oiste_viejo total = u * p` |
| `ordenar_a_los_papus` | Ordena registros por una columna específica. | `\|:v> ordenar_a_los_papus precio de_arriba_a_abajo` |
| `de_arriba_a_abajo` / `de_abajo_a_arriba` | Modificadores de ordenamiento descendente y ascendente. | `\|:v> ordenar_a_los_papus total de_abajo_a_arriba` |

### 2.6 Agrupamiento y Funciones de Agregación
| Instrucción / Palabra Reservada | Descripción | Ejemplo de Uso |
| :--- | :--- | :--- |
| `juntar_a_la_grasa_por` | Agrupa registros por una o varias columnas clave. | `\|:v> juntar_a_la_grasa_por [ciudad]` |
| `sacar_cuentas` | Aplica una o varias funciones de agregación sobre el grupo. | `\|:v> sacar_cuentas total_v = suma(total)` |
| `suma` | Calcula la sumatoria de una columna numérica. | `suma(total)` |
| `promedio` / `media` | Calcula la media aritmética. | `promedio(precio)` |
| `mediana` | Calcula el valor mediano. | `mediana(unidades)` |
| `el_mas_pro` / `maximo` | Obtiene el valor máximo. | `el_mas_pro(ingresos)` |
| `el_mas_manco` / `minimo` | Obtiene el valor mínimo. | `el_mas_manco(gastos)` |
| `contar_papus` / `conteo` | Cuenta el número de registros o filas en el grupo. | `contar_papus()` |
| `desviacion_pro` | Calcula la desviación estándar muestral. | `desviacion_pro(precio)` |

### 2.7 Visualizaciones (Reconocimiento Sintáctico en Corte 1)
| Instrucción / Palabra Reservada | Tipo de Gráfico | Ejemplo de Uso |
| :--- | :--- | :--- |
| `graficar_momos_en_barras` | Gráfico de barras | `graficar_momos_en_barras df titulo "Ventas" xd` |
| `graficar_momos_en_lineas` | Gráfico de líneas | `graficar_momos_en_lineas df titulo "Tendencia" xd` |
| `graficar_momos_en_histograma` | Histograma | `graficar_momos_en_histograma df titulo "Distribucion" xd` |
| `graficar_momos_en_dispersion` | Diagrama de dispersión | `graficar_momos_en_dispersion df eje_x "X" eje_y "Y" xd` |
| `graficar_momos_en_cajas` | Diagrama de caja | `graficar_momos_en_cajas df titulo "Boxplot" xd` |

---

## 3. Ejemplo Completo de un Programa en MomoLang (`.xd`)

```dsl
# Ejemplo de flujo completo en MomoLang XD
when haces "Iniciando analisis de datos de la grasa..." xd

ventas = pasa_el_pack "datos/ventas_prueba.csv" xd

ventas_limpias = ventas 
    |:v> escojo_a [fecha, ciudad, categoria, unidades, precio]
    |:v> but_te_enteras_que unidades > 10
    |:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio xd

resumen_ciudades = ventas_limpias 
    |:v> juntar_a_la_grasa_por [ciudad]
    |:v> sacar_cuentas total_ventas = suma(total), promedio_u = promedio(unidades), total_filas = contar_papus() xd

subir_al_grupo resumen_ciudades en "salidas/resumen_ciudades_momo.csv" xd

graficar_momos_en_barras resumen_ciudades titulo "Ingresos por Ciudad Grasosa" eje_x "Ciudad" eje_y "Total ($)" guardar "salidas/grafico_momo_barras.svg" xd

when haces "Analisis finalizado exitosamente papu xd" xd
```
