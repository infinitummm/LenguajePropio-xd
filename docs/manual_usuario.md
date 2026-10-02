# Manual de Usuario: MomoLang XD (.xd) :v
### Guía Completa de Uso y Funcionamiento del Lenguaje de la Grasa

¡Bienvenido al manual oficial de **MomoLang XD**! Este documento está escrito en lenguaje natural, claro y directo para que entiendas sin rodeos cómo funciona el lenguaje, qué hace cada instrucción, cómo procesa los datos y cómo puedes crear tus propios programas de ciencia de datos sin complicarte la vida.

---

## 1. ¿Qué es MomoLang XD?

**MomoLang XD** es un Lenguaje de Dominio Específico (DSL) creado para manipular, transformar, filtrar y analizar tablas de datos (archivos CSV). 

En lugar de usar la sintaxis fría y compleja de librerías tradicionales como Pandas o SQL, MomoLang utiliza la jerga y cultura de la grasa / momos de internet. Todo el motor de cálculo y procesamiento está construido en **Python Puro desde cero**, sin ninguna dependencia externa (cero Pandas, cero NumPy).

### La Regla de Oro del Lenguaje
> **Toda sentencia en MomoLang XD debe terminar OBLIGATORIAMENTE con `xd` (o en mayúsculas `XD` / `xD`).**  
> Si se te olvida poner `xd` al final de una línea, el analizador sintáctico te marcará error de inmediato.

---

## 2. El Flujo de Datos: El Operador Tubería (`|:v>`)

En MomoLang el análisis de datos se piensa como una línea de ensamblaje. Tienes una tabla inicial y la vas pasando por varias transformaciones hasta llegar al resultado final.

Para conectar una operación con la siguiente usamos el operador de tubería:
* **`|:v>`** (o su alias simplificado `|>`)

Piensa en `|:v>` como un *"y luego hazle esto"*. Cada paso recibe la tabla transformada del paso anterior y le aplica una nueva acción.

---

## 3. Catálogo de Instrucciones Explicadas Paso a Paso

### 3.1 Imprimir mensajes en pantalla: `when haces`
Sirve para mostrar mensajes de texto o valores en la consola mientras se ejecuta tu programa.

```momo
when haces "Iniciando el analisis de datos papu..." xd
```

---

### 3.2 Cargar un archivo CSV: `pasa_el_pack`
Para comenzar a analizar información, necesitas cargar un archivo tabular (`.csv`).

```momo
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd
```
* **¿Qué hace por debajo?** Nuestro parser propio lee el archivo caracter por caracter (sin usar el módulo `csv` ni pandas), limpia saltos de línea `\r\n`, detecta comillas y convierte automáticamente los números enteros y decimales para que queden listos para operar.

---

### 3.3 Seleccionar columnas: `escojo_a`
Si tu tabla tiene 20 columnas y solo te interesan 3, usas `escojo_a` con la lista de columnas entre corchetes `[...]`.

```momo
tabla_reducida = ventas |:v> escojo_a [ciudad, categoria, precio] xd
```
* **¿Qué hace?** Filtra verticalmente la tabla, descartando las columnas no mencionadas y dejando solo las que elegiste.

---

### 3.4 Filtrar filas: `but_te_enteras_que`
Permite quedarte únicamente con los registros (filas) que cumplan una condición lógica.

```momo
ventas_grandes = ventas |:v> but_te_enteras_que unidades > 10 xd
```

También puedes combinar varias condiciones lógicas:
* `y_ademas` (equivalente a `AND` o `&&`): Ambas condiciones deben ser verdaderas.
* `o_bien` (equivalente a `OR` o `||`): Al menos una condición debe ser verdadera.

```momo
ventas_top = ventas 
    |:v> but_te_enteras_que unidades >= 15 y_ademas precio > 50000 xd
```

Operadores de comparación soportados:
* `==` : Igual a
* `!=` : Diferente de
* `>`  : Mayor que
* `<`  : Menor que
* `>=` : Mayor o igual que
* `<=` : Menor o igual que

---

### 3.5 Crear o modificar columnas: `el_futuro_es_hoy_oiste_viejo`
Cuando necesitas calcular un nuevo valor por cada fila a partir de columnas existentes (o valores numéricos), usas esta instrucción:

```momo
ventas_con_total = ventas 
    |:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio xd
```

Operaciones matemáticas vectoriales soportadas:
* `+` : Suma
* `-` : Resta
* `*` : Multiplicación
* `/` : División (protegida contra divisiones entre cero)

* **¿Cómo funciona internamente?** Nuestra clase `VectorMomo` toma las dos columnas numéricas y efectúa una operación elemento por elemento en paralelo en tiempo de ejecución, agregando la nueva columna a la tabla.

---

### 3.6 Agrupar y calcular estadísticas: `juntar_a_la_grasa_por`
Esta es la instrucción estrella para resumir información. Te permite agrupar filas por una o varias columnas categóricas (por ejemplo, agrupar por `ciudad` o por `categoria`) y calcular métricas matemáticas para cada grupo.

```momo
resumen_ventas = ventas_con_total 
    |:v> juntar_a_la_grasa_por [ciudad] calcular [
        suma(total) como total_recaudado,
        promedio(total) como ticket_promedio,
        el_mas_pro(total) como venta_maxima,
        contar_papus(unidades) como cantidad_operaciones
    ] xd
```

#### Funciones estadísticas disponibles:
| Función en MomoLang | ¿Qué calcula? |
| :--- | :--- |
| `suma(columna)` | Suma todos los valores numéricos del grupo. |
| `promedio(columna)` / `media(columna)` | Promedio aritmético del grupo. |
| `mediana(columna)` | Valor central del grupo ordenado. |
| `el_mas_pro(columna)` / `maximo(columna)` | El valor más alto (máximo). |
| `el_mas_manco(columna)` / `minimo(columna)` | El valor más bajo (mínimo). |
| `desviacion_pro(columna)` | Desviación estándar poblacional/muestral. |
| `contar_papus(columna)` | Cantidad total de registros en ese grupo. |

---

### 3.7 Ordenar registros: `ordenar_a_los_papus`
Permite ordenar las filas de la tabla según los valores de una columna en orden ascendente o descendente.

```momo
resumen_ordenado = resumen_ventas 
    |:v> ordenar_a_los_papus total_recaudado de_arriba_a_abajo xd
```

* `de_arriba_a_abajo`: Orden descendente (de mayor a menor).
* `de_abajo_a_arriba`: Orden ascendente (de menor a mayor).

---

### 3.8 Guardar el resultado en un archivo CSV: `subir_al_grupo`
Toda transformación que hagas en memoria puede guardarse en un archivo `.csv` final en tu disco duro para compartir o reportar.

```momo
subir_al_grupo resumen_ordenado en "salidas/reporte_ventas_final.csv" xd
```
* **¿Qué hace?** Nuestro exportador genera el archivo con sus encabezados y filas formateadas correctamente.

---

### 3.9 Estructuras Condicionales: `si_pasa_esto` y `pero_si_no`
MomoLang permite ejecutar bloques de código condicionalmente según variables numéricas o comparaciones:

```momo
si_pasa_esto (meta_superada > 1000000) {
    when haces "Meta superada con honores papu :v" xd
} pero_si_no {
    when haces "Falta vender mas momos para la meta xd" xd
} xd
```

---

## 4. Ejemplo Completo de Inicio a Fin

A continuación tienes un ejemplo real y ejecutable (`ejemplos/programa_ventas_fase2.xd`):

```momo
when haces "=== ANALISIS DE VENTAS CON LIBRERIAS PROPIAS MOMOLANG ===" xd

# 1. Cargar archivo CSV
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd

# 2. Filtrar y crear columna calculada con operaciones vectoriales
ventas_filtradas = ventas 
    |:v> but_te_enteras_que unidades > 2
    |:v> el_futuro_es_hoy_oiste_viejo total_venta = unidades * precio xd

# 3. Agrupamiento por ciudad con multiples funciones estadisticas
resumen_ciudades = ventas_filtradas 
    |:v> juntar_a_la_grasa_por [ciudad] calcular [
        suma(total_venta) como total_recaudado,
        promedio(total_venta) como ticket_promedio,
        el_mas_pro(total_venta) como venta_maxima,
        el_mas_manco(total_venta) como venta_minima,
        contar_papus(unidades) como cantidad_ventas
    ]
    |:v> ordenar_a_los_papus total_recaudado de_arriba_a_abajo xd

# 4. Guardar resultado final a disco
subir_al_grupo resumen_ciudades en "salidas/reporte_ventas_ciudades.csv" xd

when haces "Procesamiento completado y reporte guardado en salidas/reporte_ventas_ciudades.csv :v" xd
```

---

## 5. ¿Cómo Funcionan las Librerías Propias Internas?

Para cumplir con las exigencias del proyecto y de la materia:
1. **No se utiliza Pandas ni NumPy.**
2. **`VectorMomo` (`src/core/matematica_propia.py`):** Modela columnas vectoriales numéricas. Implementa la sobrecarga de operadores matemáticos (`+`, `-`, `*`, `/`) y relacionales (`>`, `<`, `==`, etc.) en listas nativas de Python, junto con algoritmos estadísticos puros (suma, promedio, mediana con ordenamiento manual, desviación estándar con varianza y raíz cuadrada mediante exponente `** 0.5`).
3. **`TablaMomo` (`src/core/datos_propios.py`):** Modela estructuras tabulares bidimensionales con nombres de métodos de momos (`escojo_a`, `but_te_enteras_que`, `el_futuro_es_hoy_oiste_viejo`, `juntar_a_la_grasa_por`, `ordenar_a_los_papus`, `pasa_el_pack`, `subir_al_grupo`).
4. **`parsear_csv_propio`:** Un autómata finito determinista (FSM) que procesa archivos CSV respetando comillas, comas internas y conversiones de tipo sin usar el módulo `csv`.

---

## 6. Comandos para Ejecutar Programas

Puedes ejecutar cualquier programa `.xd` desde la terminal con el comando:

```bash
python3 ejecutar_dsl.py ejemplos/programa_ventas_fase2.xd
```

O si prefieres usar el `Makefile` simplificado:

```bash
make run-ventas          # Ejecuta el analisis de ventas
make run-empleados       # Ejecuta el analisis de nomina de empleados
make run-estudiantes     # Ejecuta el analisis de notas academicas
make run-error-semantico # Muestra la deteccion de errores semanticos
```

¡Y listo! Con esto tienes todo el conocimiento necesario para dominar y explicar MomoLang XD en tus presentaciones y defensas. :v
