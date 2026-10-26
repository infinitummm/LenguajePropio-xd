
***

# MomoLang XD (`.xd`) 

**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción  
**Docente:** Joaquín F. Sánchez 

**Equipo de Desarrollo:**  
* Dylan Torres  
* Juan Gomez  
* Javier Rosero  

---

##  ¿Qué es MomoLang XD y para qué sirve?

En el mundo de la programación, a veces los lenguajes generales (como Python o Java) son como una navaja suiza: sirven para todo, pero para tareas muy específicas es mejor usar una herramienta diseñada a la medida. A esto le llamamos **Lenguaje de Dominio Específico (DSL)**.

**MomoLang XD** es un DSL creado específicamente para hacer **ciencia de datos**. Su objetivo es permitirte escribir flujos de trabajo de datos de forma clara, ordenada y fácil de leer. Con este lenguaje puedes:
* Cargar y guardar archivos de datos (CSV).
* Limpiar datos, elegir columnas específicas y filtrar filas.
* Crear columnas nuevas con cálculos matemáticos.
* Agrupar datos y calcular estadísticas (sumas, promedios, máximos, etc.).
* Generar gráficos de manera declarativa.

**El toque de identidad:** Para mantener la esencia de la cultura de internet y los memes hispanos, el lenguaje tiene una regla de oro inquebrantable: **absolutamente toda instrucción debe terminar con la palabra `xd`** (también acepta `XD` o `xD`).

---

##  Filosofía de Diseño

El lenguaje se construyó pensando en la facilidad de uso y en mantener los datos originales intactos. Sus pilares son:

1. **Dile qué quieres, no cómo hacerlo:** Es un lenguaje *declarativo*. Tú le dices al programa qué transformaciones quieres (ej. "filtra los precios mayores a 50"), y el sistema se encarga de ejecutarlo.
2. **El modelo de "Tubería" (Pipeline):** Los datos fluyen a través de una tubería usando el operador `|:v>` (o `|>`). Esto permite encadenar varias operaciones paso a paso sin alterar el conjunto de datos original.
3. **El delimitador `xd`:** Cada línea de código termina con `xd`. Esto evita confusiones al leer el código y le da su personalidad única.
4. **Arquitectura limpia:** El código que "lee" el texto (front-end) está completamente separado del código que "ejecuta" las acciones, lo que hace que el sistema sea más fácil de mantener y escalar.

---

## ¿Cómo funciona bajo el capó? (Arquitectura)

Para construir el "cerebro" del lenguaje, utilizamos **ANTLR4**, una herramienta poderosa que nos ayuda a leer y entender el código escrito en `.xd`. 

El proceso funciona así:

```text
                       ┌─────────────────────────────────┐
                       │   Tu Código Fuente (.xd)        │
                       └────────────────┬────────────────┘
                                        │
                                        ▼
                       ┌─────────────────────────────────┐
                       │      1. Analizador Léxico       │
                       │   Lee el texto y lo divide en   │
                       │   "palabras" o Tokens.          │
                       └────────────────┬────────────────┘
                                        │ 
                                        ▼
                       ┌─────────────────────────────────┐
                       │     2. Analizador Sintáctico    │
                       │   Revisa si las palabras están  │
                       │   en el orden correcto (gramática).│
                       └────────┬───────────────┬────────┘
                                │               │
                  ¿Todo bien?   │               │ ¿Hay un error?
                                ▼               ▼
            ┌─────────────────────────┐   ┌───────────────────────────────┐
            │   Árbol Sintáctico      │   │  Sistema de Errores Amigable  │
            │  (Estructura lógica     │   │  Te dice exactamente en qué   │
            │   del programa)         │   │  línea fallaste y cómo arreglarlo│
            └───────────┬─────────────┘   └───────────────┬───────────────┘
                        │                                 │
                        ▼                                 ▼
             [ PROGRAMA ACEPTADO :v ]          [ PROGRAMA RECHAZADO xd ]
```

* **Manejo de errores humano:** Si te equivocas, el lenguaje no te lanzará un mensaje de error críptico. Te dirá con la línea y columna exacta, qué token faltó o sobró.

---

## Estructura del Proyecto

El repositorio está organizado de forma modular y desacoplada:

```text
LenguajePropio-xd/
├── grammar/              # Reglas oficiales del lenguaje (Gramática ANTLR4).
├── docs/                 # Documentación técnica y académica.
│   ├── manual_usuario.md # Manual de usuario y catálogo de instrucciones.
│   └── reglas_semanticas.md # Especificación formal de tipos y símbolos.
├── src/                  # Motores de análisis y ejecución.
│   ├── core/             # Librerías PROPIAS en Python Puro (cero Pandas/NumPy/Matplotlib).
│   │   ├── datos_momeros.py       # TablaMomo, SerieMomo, Parser CSV propio.
│   │   ├── matematica_momera.py   # VectorMomo, estadística, números aleatorios y álgebra propia.
│   │   ├── estructuras_momeras.py # PilaMomera, ColaMomera, ListaMomera, MapaMomero.
│   │   └── graficas_momeras.py    # Motor de renderizado PNG propio en Python puro.
│   ├── semantica/        # Analizador semántico y ejecutor.
│   │   ├── tabla_simbolos.py     # Manejo de símbolos, ámbitos y tipos.
│   │   └── visitor_ejecutor.py   # Visitor ANTLR4 que ejecuta el DSL.
│   ├── parser/           # Archivos generados automáticamente por ANTLR4.
│   └── validador/        # Diagnóstico sintáctico y listeners amigables.
├── ejemplos/             # Programas .xd de prueba y demostración (análisis y control de flujo).
├── datos/                # Datasets CSV de prueba (ventas, empleados, estudiantes).
├── salidas/              # Archivos CSV generados por los programas MomoLang XD.
├── ejecutar_dsl.py       # Validador y ejecutor semántico CLI principal.
├── Makefile              # Comandos rápidos para compilar, ejecutar y limpiar.
└── README.md             # Este documento.
```

---

## Manual de Instrucciones (Catálogo)

Aquí tienes las "palabras mágicas" de MomoLang XD, divididas por categorías:

### Cargar, Imprimir y Guardar
| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `when haces ... xd` | Imprime un mensaje o resultado en la consola. | `when haces "Hola mundo" xd` |
| `id = pasa_el_pack "ruta" xd` | Carga un archivo CSV en una variable. | `ventas = pasa_el_pack "datos/ventas.csv" xd` |
| `... separador ";"` | Úsalo si tu CSV usa punto y coma en vez de comas. | `datos = pasa_el_pack "a.csv" separador ";" xd` |
| `subir_al_grupo id en "ruta" xd` | Guarda los datos procesados en un nuevo CSV. | `subir_al_group resumen en "salida.csv" xd` |

### Operaciones en la Tubería (`|:v>`)
Estas operaciones se encadenan para transformar los datos paso a paso.

| Operación | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `escojo_a [col1, col2]` | Selecciona solo las columnas que necesitas. | `\|:v> escojo_a [fecha, precio]` |
| `but_te_enteras_que ...` | Filtra las filas que cumplan una condición. | `\|:v> but_te_enteras_que precio > 50` |
| `el_futuro_es_hoy... col = expr` | Crea una columna nueva con una fórmula. | `\|:v> el_futuro_es_hoy_oiste_viejo total = cant * precio` |
| `ordenar_a_los_papus col ...` | Ordena los datos (de arriba a abajo o viceversa). | `\|:v> ordenar_a_los_papus total de_arriba_a_abajo` |

### Estadísticas y Agrupaciones
Para cuando necesitas resumir la información.

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `juntar_a_la_grasa_por [cols]` | Agrupa los datos por una o varias columnas. | `\|:v> juntar_a_la_grasa_por [ciudad]` |
| `sacar_cuentas ...` | Calcula estadísticas sobre los grupos creados. | `\|:v> sacar_cuentas total = suma(ventas)` |
| *Funciones:* | `suma()`, `promedio()`, `mediana()`, `el_mas_pro()` (máximo), `el_mas_manco()` (mínimo), `desviacion_pro()`, `contar_papus()` (contar filas). | `sacar_cuentas m = el_mas_pro(precio), n = contar_papus()` |

### Control de Flujo y Funciones
| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `var = expr xd` | Asigna cualquier valor numérico, texto, función o tabla a una variable. | `total = cant * precio xd` |
| `si_el_papu ... sino... fin_del_momo xd` | Bifurcación condicional evaluando expresiones booleanas. | `si_el_papu meta > 100 entonces ... fin_del_momo xd` |
| `mientras_el_papu ... fin_del_bucle xd` | Bucle while que itera mientras la condición sea verdadera. | `mientras_el_papu c <= 3 haz_esto ... fin_del_bucle xd` |
| `para_cada_papu ... fin_del_bucle xd` | Bucle for sobre un rango numérico de inicio a fin. | `para_cada_papu i desde 1 hasta 5 haz_esto ... fin_del_bucle xd` |
| `momo_funcion ... fin_de_la_funcion xd` | Define una función reutilizable con parámetros. | `momo_funcion calc(a, b) ... fin_de_la_funcion xd` |
| `suelta_el_momo expr xd` | Retorna un valor desde una función al llamador. | `suelta_el_momo a + b xd` |

### Estructuras de Datos y Colecciones
MomoLang XD incluye soporte nativo para colecciones literales y estructuras clásicas:

| Instrucción | ¿Qué hace? | Ejemplo |
| :--- | :--- | :--- |
| `[elem1, elem2, ...]` | Literal de lista dinámica. | `nums = [10, 20, 30] xd` |
| `{clave: valor, ...}` | Literal de mapa / diccionario asociativo. | `config = {"iva": 19} xd` |
| `id[indice]` | Acceso e indexación sobre listas, mapas y tablas. | `valor = nums[0] xd` |
| `id[indice] = expr xd` | Asignación y mutación por índice. | `nums[1] = 99 xd` |
| `crear_pila() xd` | Inicializa una Pila Momera (LIFO). | `pila = crear_pila() xd` |
| `apilar_papu(p, x) xd` | Inserta un elemento en el tope de la pila. | `apilar_papu(pila, "momo") xd` |
| `desapilar_papu(p) xd` | Extrae y retorna el elemento en el tope. | `elem = desapilar_papu(pila) xd` |
| `tope_papu(p) xd` | Consulta el elemento del tope sin extraerlo. | `t = tope_papu(pila) xd` |
| `crear_cola() xd` | Inicializa una Cola Momera (FIFO). | `cola = crear_cola() xd` |
| `encolar_papu(c, x) xd` | Inserta un elemento al final de la cola. | `encolar_papu(cola, "ticket") xd` |
| `desencolar_papu(c) xd` | Extrae y retorna el primer elemento al frente. | `t = desencolar_papu(cola) xd` |
| `frente_papu(c) xd` | Consulta el primer elemento sin extraerlo. | `f = frente_papu(cola) xd` |
| `longitud_papu(c) xd` | Retorna el tamaño de cualquier colección. | `tam = longitud_papu(cola) xd` |

### Gráficos
MomoLang XD cuenta con un motor propio de renderizado rasterizado en Python estándar (`graficas_momeras.py`), generando imágenes **PNG** reales sin utilizar matplotlib, Pillow ni SVG:
* `graficar_momos_en_barras`
* `graficar_momos_en_lineas`
* `graficar_momos_en_histograma`
* `graficar_momos_en_dispersion`
* `graficar_momos_en_cajas`

*(Todos aceptan parámetros opcionales como `titulo`, `eje_x`, `eje_y` y `guardar "ruta.png"` para exportar la imagen).*

---

## Automatización con `Makefile`

Para no tener que escribir comandos largos, el proyecto incluye un `Makefile`. Solo abre tu terminal en la carpeta del proyecto y usa:

| Comando | ¿Qué hace? |
| :--- | :--- |
| `make help` | Muestra la lista de todos los comandos disponibles. |
| `make build` | Compila la gramática ANTLR4 y genera el lexer/parser en Python. |
| `make run` | Ejecuta el programa principal (`ejemplos/programa_correcto1.xd`). |
| `make run-caso-estudio` | Ejecuta el caso de estudio integral final con estructuras de datos y generación de 4 gráficas PNG. |
| `make run-control` | Ejecuta el programa de control de flujo y funciones (`programa_control_funciones.xd`). |
| `make run-completo` | Ejecuta el pipeline completo combinando funciones y datos CSV (`programa_analisis_completo.xd`). |
| `make run-ventas` | Ejecuta el pipeline de ventas con agregaciones y filtros (`programa_ventas.xd`). |
| `make run-empleados` | Ejecuta el análisis de nómina y departamentos (`programa_empleados.xd`). |
| `make run-estudiantes` | Ejecuta el análisis de notas y rendimiento académico (`programa_estudiantes.xd`). |
| `make run-error-semantico` | Demuestra la detección y diagnóstico de errores semánticos en consola. |
| `make run-incorrect` | Prueba el archivo con errores sintácticos para ver el diagnóstico de ANTLR4. |
| `make run-tree` | Valida el ejemplo y te muestra el árbol sintáctico jerárquico. |
| `make clean` | Borra archivos temporales y caché de Python. |

**Flujos de ejecución recomendados:**
```bash
make run-control         # 1. Asignaciones, condicionales, ciclos y funciones
make run-completo        # 2. Pipeline integral de datos con funciones
make run-ventas          # 3. Pipeline de ventas con CSV resultante
make run-error-semantico # 4. Diagnóstico de errores semánticos
```

---

## Ejemplo Real de MomoLang XD

Así es como se ve un programa completo y funcional en nuestro lenguaje (`ejemplos/programa_correcto1.xd`):

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
