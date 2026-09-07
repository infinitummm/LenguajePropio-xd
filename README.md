
***

# MomoLang XD (`.xd`) — Un Lenguaje para Ciencia de Datos

**Universidad Sergio Arboleda**  
**Escuela de Ciencias Exactas e Ingeniería**  
**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción  
**Docente:** Joaquín F. Sánchez | **Semestre:** 2026-2  

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

El repositorio está organizado de forma lógica para que encuentres todo fácilmente:

```text
LenguajePropio-xd/
├── grammar/          # Las reglas oficiales del lenguaje (Gramática ANTLR4).
├── docs/             # Documentación extra (alcance del proyecto y manual EBNF).
├── src/              # El código fuente del compilador/validador.
│   ├── parser/       # Archivos generados automáticamente por ANTLR4.
│   └── validador...  # El motor que revisa si tu código está bien escrito.
├── ejemplos/         # Archivos .xd de prueba (tanto correctos como con errores).
├── datos/            # Archivos CSV de prueba para usar en los ejemplos.
├── tests/            # Pruebas automáticas para asegurar que todo funcione.
├── ejecutar_dsl.py   # El programa principal para correr y validar tus archivos .xd.
├── Makefile          # Comandos rápidos para compilar, probar y limpiar el proyecto.
└── README.md         # Este documento.
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

### Gráficos
Puedes generar 5 tipos de gráficos de forma sencilla:
* `graficar_momos_en_barras`
* `graficar_momos_en_lineas`
* `graficar_momos_en_histograma`
* `graficar_momos_en_dispersion`
* `graficar_momos_en_cajas`

*(Todos aceptan parámetros opcionales como `titulo`, `eje_x`, `eje_y` y `guardar` para exportar la imagen).*

---

## Automatización con `Makefile`

Para no tener que escribir comandos largos, el proyecto incluye un `Makefile`. Solo abre tu terminal en la carpeta del proyecto y usa:

| Comando | ¿Qué hace? |
| :--- | :--- |
| `make help` | Muestra la lista de todos los comandos disponibles. |
| `make build` | Compila la gramática y actualiza el analizador del lenguaje. |
| `make test` | Ejecuta las pruebas automáticas para verificar que todo funcione. |
| `make run` | Valida el archivo de ejemplo correcto (`programa_correcto1.xd`). |
| `make run-tree` | Valida el ejemplo y te muestra el "árbol" lógico de cómo entendió el código. |
| `make run-incorrect` | Prueba el archivo con errores para ver cómo el sistema te regaña. |
| `make clean` | Borra archivos temporales y deja el proyecto limpio. |

**Flujo de trabajo recomendado:**
```bash
make test      # 1. Asegúrate de que el motor funciona.
make run       # 2. Valida un código correcto.
make run-tree  # 3. Mira cómo el lenguaje "piensa" el código.
```

---


## Pruebas Automatizadas (Tests)

Para garantizar que el lenguaje no falle, creamos una suite de **9 pruebas automáticas** (`tests/test_corte1.py`). Estas pruebas verifican que el lenguaje se comporte bien en escenarios como:
* Aceptar programas completos y correctos (carga, tuberías, gráficos).
* Aceptar el uso correcto del operador `|:v>`.
* Rechazar programas a los que se les olvidó poner el `xd` al final.
* Rechazar palabras inventadas o errores de tipeo.
* Detectar cuando falta un operador matemático o relacional (ej. `precio > `).

Todas las pruebas pasan exitosamente (`OK`), demostrando que el motor del lenguaje es robusto.

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
