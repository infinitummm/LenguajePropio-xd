
---

# MomoLang XD (`.xd`)

**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción  
**Docente:** Joaquín F. Sánchez  

**Equipo de Desarrollo:**  
* Dylan Torres  
* Juan Gomez  
* Javier Rosero  

---

## ¿Qué es MomoLang XD y para qué sirve?

En programación, los lenguajes generales —como Python o Java— son muy útiles porque permiten hacer casi cualquier cosa. Sin embargo, cuando una tarea es muy específica, suele ser mejor contar con una herramienta diseñada especialmente para ese propósito. A ese tipo de herramienta se le conoce como **Lenguaje de Dominio Específico (DSL)**.

**MomoLang XD** es un lenguaje creado específicamente para trabajar en **ciencia de datos**. Su objetivo es que los flujos de trabajo con datos sean claros, ordenados y fáciles de leer. Con este lenguaje se puede:

* Cargar y guardar archivos de datos en formato CSV.
* Limpiar datos, seleccionar columnas y filtrar filas.
* Crear columnas nuevas a partir de cálculos matemáticos.
* Agrupar datos y calcular estadísticas como sumas, promedios y máximos.
* Generar gráficos de forma declarativa.

**El toque de identidad:** para mantener la esencia de la cultura de internet y de los memes hispanos, el lenguaje tiene una regla de oro: **toda instrucción debe terminar con la palabra `xd`**. También se aceptan las formas `XD` y `xD`.

---

## Filosofía de Diseño

El lenguaje se construyó pensando en la facilidad de uso y en mantener los datos originales intactos. Sus principios principales son:

1. **Decir qué se quiere, no cómo hacerlo:** es un lenguaje *declarativo*. El usuario indica qué transformaciones desea realizar —por ejemplo, “filtrar los precios mayores a 50”— y el sistema se encarga de ejecutarlas.
2. **El modelo de “tubería” (pipeline):** los datos fluyen a través de una tubería usando el operador `|:v>` o `|>`. Esto permite encadenar varias operaciones paso a paso sin modificar el conjunto de datos original.
3. **El delimitador `xd`:** cada línea de código termina con `xd`. Esto facilita la lectura del código y le da una personalidad propia al lenguaje.
4. **Una arquitectura ordenada:** la parte que lee el texto está separada de la parte que ejecuta las acciones. Esto hace que el sistema sea más fácil de mantener y de ampliar.

---

## ¿Cómo funciona internamente?

Para construir el “cerebro” del lenguaje se utiliza **ANTLR4**, una herramienta que ayuda a leer y comprender el código escrito en `.xd`.

El proceso funciona de la siguiente manera:

```text
Código fuente .xd
        ↓
Lectura del texto y separación en piezas
        ↓
Revisión del orden y la estructura del programa
        ↓
Si todo está correcto: ejecución del programa
Si hay un error: mensaje claro con la línea y la columna del problema
```

* **Manejo de errores comprensible:** si el usuario se equivoca, el lenguaje no muestra un mensaje técnico difícil de entender. Indica con precisión la línea y la columna, y explica qué elemento falta o sobra.

---

## Estructura del Proyecto

El repositorio está organizado de forma modular, con las responsabilidades bien separadas:

```text
LenguajePropio-xd/
├── grammar/              # Reglas oficiales del lenguaje (gramática ANTLR4).
├── docs/                 # Documentación técnica y académica.
│   ├── manual_usuario.md # Manual de usuario y catálogo de instrucciones.
│   └── reglas_semanticas.md # Especificación formal de tipos y símbolos.
├── src/                  # Motores de análisis y ejecución.
│   ├── core/             # Librerías propias en Python, sin depender de Pandas, NumPy ni Matplotlib.
│   │   ├── datos_momeros.py       # TablaMomo, SerieMomo y lector CSV propio.
│   │   ├── matematica_momera.py   # VectorMomo, estadística, números aleatorios y álgebra propia.
│   │   ├── estructuras_momeras.py # PilaMomera, ColaMomera, ListaMomera y MapaMomero.
│   │   └── graficas_momeras.py    # Motor propio de generación de imágenes PNG en Python puro.
│   ├── semantica/        # Revisión del sentido del programa y ejecución.
│   │   ├── tabla_simbolos.py     # Manejo de símbolos, ámbitos y tipos.
│   │   └── visitor_ejecutor.py   # Componente que recorre la estructura y ejecuta el DSL.
│   ├── parser/           # Archivos generados automáticamente por ANTLR4.
│   └── validador/        # Diagnóstico sintáctico y mensajes de error claros.
├── ejemplos/             # Programas .xd de prueba y demostración.
├── datos/                # Conjuntos de datos CSV de prueba (ventas, empleados, estudiantes).
├── salidas/              # Archivos CSV generados por los programas MomoLang XD.
├── ejecutar_dsl.py       # Validador y ejecutor principal desde la terminal.
├── Makefile              # Comandos rápidos para compilar, ejecutar y limpiar.
└── README.md             # Este documento.
```

---

## Manual de Instrucciones

A continuación se presentan las instrucciones principales de MomoLang XD, organizadas por categorías.

### Cargar, imprimir y guardar

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `when haces ... xd` | Imprime un mensaje o resultado en la consola. | `when haces "Hola mundo" xd` |
| `id = pasa_el_pack "ruta" xd` | Carga un archivo CSV en una variable. | `ventas = pasa_el_pack "datos/ventas.csv" xd` |
| `... separador ";"` | Permite indicar que el CSV usa punto y coma en lugar de comas. | `datos = pasa_el_pack "a.csv" separador ";" xd` |
| `subir_al_grupo id en "ruta" xd` | Guarda los datos procesados en un nuevo archivo CSV. | `subir_al_group resumen en "salida.csv" xd` |

### Operaciones en la tubería (`|:v>`)

Estas operaciones se encadenan para transformar los datos paso a paso.

| Operación | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `escojo_a [col1, col2]` | Selecciona únicamente las columnas necesarias. | `\|:v> escojo_a [fecha, precio]` |
| `but_te_enteras_que ...` | Filtra las filas que cumplen una condición. | `\|:v> but_te_enteras_que precio > 50` |
| `el_futuro_es_hoy... col = expr` | Crea una columna nueva a partir de una fórmula. | `\|:v> el_futuro_es_hoy_oiste_viejo total = cant * precio` |
| `ordenar_a_los_papus col ...` | Ordena los datos de forma ascendente o descendente. | `\|:v> ordenar_a_los_papus total de_arriba_a_abajo` |

### Estadísticas y agrupaciones

Estas instrucciones permiten resumir la información.

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `juntar_a_la_grasa_por [cols]` | Agrupa los datos por una o varias columnas. | `\|:v> juntar_a_la_grasa_por [ciudad]` |
| `sacar_cuentas ...` | Calcula estadísticas sobre los grupos creados. | `\|:v> sacar_cuentas total = suma(ventas)` |
| *Funciones disponibles:* | `suma()`, `promedio()`, `mediana()`, `el_mas_pro()` (máximo), `el_mas_manco()` (mínimo), `desviacion_pro()`, `contar_papus()` (contar filas). | `sacar_cuentas m = el_mas_pro(precio), n = contar_papus()` |

### Control de flujo y funciones

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `var = expr xd` | Asigna un valor numérico, texto, función o tabla a una variable. | `total = cant * precio xd` |
| `si_el_papu ... sino... fin_del_momo xd` | Ejecuta una bifurcación condicional según una expresión booleana. | `si_el_papu meta > 100 entonces ... fin_del_momo xd` |
| `mientras_el_papu ... fin_del_bucle xd` | Repite un bloque mientras la condición sea verdadera. | `mientras_el_papu c <= 3 haz_esto ... fin_del_bucle xd` |
| `para_cada_papu ... fin_del_bucle xd` | Recorre un rango numérico de inicio a fin. | `para_cada_papu i desde 1 hasta 5 haz_esto ... fin_del_bucle xd` |
| `momo_funcion ... fin_de_la_funcion xd` | Define una función reutilizable con parámetros. | `momo_funcion calc(a, b) ... fin_de_la_funcion xd` |
| `suelta_el_momo expr xd` | Retorna un valor desde una función al lugar desde donde se llamó. | `suelta_el_momo a + b xd` |

### Estructuras de datos y colecciones

MomoLang XD incluye soporte para colecciones literales y estructuras clásicas:

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `[elem1, elem2, ...]` | Crea una lista dinámica. | `nums = [10, 20, 30] xd` |
| `{clave: valor, ...}` | Crea un mapa o diccionario asociativo. | `config = {"iva": 19} xd` |
| `id[indice]` | Accede a un elemento de listas, mapas y tablas. | `valor = nums[0] xd` |
| `id[indice] = expr xd` | Asigna o modifica un valor por índice. | `nums[1] = 99 xd` |
| `crear_pila() xd` | Inicializa una Pila Momera (LIFO). | `pila = crear_pila() xd` |
| `apilar_papu(p, x) xd` | Inserta un elemento en el tope de la pila. | `apilar_papu(pila, "momo") xd` |
| `desapilar_papu(p) xd` | Extrae y retorna el elemento del tope. | `elem = desapilar_papu(pila) xd` |
| `tope_papu(p) xd` | Consulta el elemento del tope sin extraerlo. | `t = tope_papu(pila) xd` |
| `crear_cola() xd` | Inicializa una Cola Momera (FIFO). | `cola = crear_cola() xd` |
| `encolar_papu(c, x) xd` | Inserta un elemento al final de la cola. | `encolar_papu(cola, "ticket") xd` |
| `desencolar_papu(c) xd` | Extrae y retorna el primer elemento de la cola. | `t = desencolar_papu(cola) xd` |
| `frente_papu(c) xd` | Consulta el primer elemento sin extraerlo. | `f = frente_papu(cola) xd` |
| `longitud_papu(c) xd` | Retorna el tamaño de cualquier colección. | `tam = longitud_papu(cola) xd` |

### Gráficos

MomoLang XD cuenta con un motor propio de generación de imágenes en Python estándar (`graficas_momeras.py`). Este motor produce imágenes **PNG** reales sin utilizar matplotlib, Pillow ni SVG:

* `graficar_momos_en_barras`
* `graficar_momos_en_lineas`
* `graficar_momos_en_histograma`
* `graficar_momos_en_dispersion`
* `graficar_momos_en_cajas`

Todas estas instrucciones aceptan parámetros opcionales como `titulo`, `eje_x`, `eje_y` y `guardar "ruta.png"` para exportar la imagen.

---

## Automatización con `Makefile`

Para evitar escribir comandos largos, el proyecto incluye un archivo `Makefile`. Basta con abrir la terminal en la carpeta del proyecto y usar los siguientes comandos:

| Comando | ¿Qué hace? |
| :--- | :--- |
| `make help` | Muestra la lista de todos los comandos disponibles. |
| `make build` | Compila la gramática ANTLR4 y genera el analizador léxico y sintáctico en Python. |
| `make run` | Ejecuta el programa principal (`ejemplos/programa_correcto1.xd`). |
| `make run-caso-estudio` | Ejecuta el caso de estudio integral final con estructuras de datos y generación de cuatro gráficas PNG. |
| `make run-control` | Ejecuta el programa de control de flujo y funciones (`programa_control_funciones.xd`). |
| `make run-completo` | Ejecuta el flujo completo combinando funciones y datos CSV (`programa_analisis_completo.xd`). |
| `make run-ventas` | Ejecuta el análisis de ventas con agrupaciones y filtros (`programa_ventas.xd`). |
| `make run-empleados` | Ejecuta el análisis de nómina y departamentos (`programa_empleados.xd`). |
| `make run-estudiantes` | Ejecuta el análisis de notas y rendimiento académico (`programa_estudiantes.xd`). |
| `make run-error-semantico` | Muestra la detección y el diagnóstico de errores de sentido en la consola. |
| `make run-incorrect` | Prueba un archivo con errores sintácticos para ver el diagnóstico de ANTLR4. |
| `make run-tree` | Valida el ejemplo y muestra el árbol sintáctico jerárquico. |
| `make clean` | Borra archivos temporales y la caché de Python. |

**Flujos de ejecución recomendados:**

```bash
make run-control         # 1. Asignaciones, condicionales, ciclos y funciones
make run-completo        # 2. Flujo integral de datos con funciones
make run-ventas          # 3. Análisis de ventas con CSV resultante
make run-error-semantico # 4. Diagnóstico de errores de sentido
```

---

## Ejemplo real de MomoLang XD

Así se ve un programa completo y funcional en este lenguaje (`ejemplos/programa_correcto1.xd`):

```dsl
# =======================================================
# Análisis de Ventas en MomoLang XD
# =======================================================

# 1. Imprimir un mensaje de inicio
when haces "Iniciando analisis de datos de la grasa..." xd

# 2. Cargar los datos desde un CSV
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd

# 3. Transformar los datos paso a paso (Pipeline)
ventas_limpias = ventas 
    |:v> escojo_a [fecha, ciudad, categoria, unidades, precio]
    |:v> but_te_enteras_que unidades > 10
    |:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio xd

# 4. Agrupar por ciudad y sacar estadísticas
resumen_ciudades = ventas_limpias 
    |:v> juntar_a_la_grasa_por [ciudad]
    |:v> sacar_cuentas total_ventas = suma(total), promedio_unidades = promedio(unidades), total_filas = contar_papus() xd

# 5. Guardar el resultado en un nuevo CSV
subir_al_grupo resumen_ciudades en "salidas/resumen_ciudades_momo.csv" xd

# 6. Generar un gráfico de barras
graficar_momos_en_barras resumen_ciudades titulo "Ingresos por Ciudad Grasosa" eje_x "Ciudad" eje_y "Total ($)" guardar "salidas/grafico_momo_barras.svg" xd

# 7. Mensaje final
when haces "Analisis finalizado exitosamente papu xd" xd
```

---


