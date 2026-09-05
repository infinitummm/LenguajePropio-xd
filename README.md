# MomoLang XD (`.xd`) — Lenguaje de Dominio Específico para Ciencia de Datos y Visualización

**Universidad Sergio Arboleda**  
**Escuela de Ciencias Exactas e Ingeniería**  
**Programa de Ciencias de la Computación e Inteligencia Artificial**  
**Asignatura:** Lenguajes de Programación y Transducción  
**Docente:** Joaquín F. Sánchez | **Semestre Académico:** 2026-2  

**Integrantes del Proyecto:**  
* Dylan Torres  
* Juan Gomez  
* Javier Rosero  

---

## 1. Introducción y Propósito del Proyecto

En el desarrollo de software y el análisis computacional moderno, un **Lenguaje de Dominio Específico (DSL)** representa una herramienta de alto valor al delimitar su vocabulario y semántica para resolver problemas dentro de un contexto concreto, a diferencia de los lenguajes de propósito general (GPL) como C++, Java o Python.

**MomoLang XD** es un DSL declarativo y funcional concebido para estructurar y comunicar **flujos de trabajo reproducibles en ciencia de datos**:
* Ingesta y persistencia de conjuntos de datos estructurados en formato CSV.
* Operaciones de limpieza, proyección de atributos y filtrado mediante expresiones booleanas.
* Generación de variables derivadas (columnas calculadas) a través de expresiones aritméticas.
* Agrupamiento multidimensional y cálculo de agregaciones estadísticas descriptivas.
* Especificación sintáctica y declarativa de representaciones gráficas vectoriales.

Como rasgo de identidad sintáctica y cohesión comunitaria, el lenguaje toma inspiración en la cultura digital y los memes hispanoamericanos, estableciendo una convención formal determinante: **toda sentencia del lenguaje debe concluir obligatoriamente con el delimitador léxico `xd`**.

---

## 2. Principios de Diseño del Lenguaje

El diseño de MomoLang XD se rige por principios de ingeniería de lenguajes orientados a la legibilidad y la inmutabilidad:

1. **Sintaxis Declarativa y Funcional:** El programador describe *qué transformaciones* aplicar sobre la información, delegando al procesador la determinación de *cómo* estructurar la secuencia de operaciones.
2. **Modelo de Tuberías (Pipelines):** Se introduce el operador de encadenamiento `|:v>` (con variante estándar `|>`), el cual transfiere el conjunto de datos resultante de una etapa a la subsiguiente sin mutar la fuente original.
3. **Delimitador Explícito de Sentencia:** Cada instrucción concluye con el token `xd` (sensible a variantes capitalizadas como `XD` o `xD`), evitando ambigüedades de fin de sentencia comunes en lenguajes basados en saltos de línea arbitrarios.
4. **Separación Estricta de Fases:** El compilador mantiene un desacoplamiento riguroso entre el front-end (reconocimiento léxico y sintáctico) y las capas posteriores de evaluación semántica y ejecución.

---

## 3. Arquitectura del Front-End

El front-end del lenguaje ha sido desarrollado utilizando la herramienta de generación de analizadores **ANTLR4** (ANother Tool for Language Recognition) con destino a **Python 3**:

```
                       ┌─────────────────────────────────┐
                       │   Código Fuente (.xd) en Disco  │
                       └────────────────┬────────────────┘
                                        │
                                        ▼
                       ┌─────────────────────────────────┐
                       │      Analizador Léxico          │
                       │   (LenguajeMomoXDLexer.py)      │
                       │  Convierte texto plano a Tokens │
                       └────────────────┬────────────────┘
                                        │ Flujo de Tokens
                                        ▼
                       ┌─────────────────────────────────┐
                       │     Analizador Sintáctico       │
                       │   (LenguajeMomoXDParser.py)     │
                       │  Aplica reglas de gramática .g4 │
                       └────────┬───────────────┬────────┘
                                │               │
                  ¿Sin errores? │               │ ¿Discrepancia detectada?
                                ▼               ▼
            ┌─────────────────────────┐   ┌───────────────────────────────┐
            │   Parse Tree Generado   │   │  MomoSintaxisErrorListener    │
            │  Árbol Sintáctico LISP  │   │  Captura línea, columna,      │
            │  y Formato Jerárquico   │   │  token y sugerencia amigable  │
            └───────────┬─────────────┘   └───────────────┬───────────────┘
                        │                                 │
                        ▼                                 ▼
             [ PROGRAMA ACEPTADO :v ]          [ PROGRAMA RECHAZADO xd ]
             Métricas estructurales de         Diagnóstico preciso para el
             sentencias e inspección visual    desarrollador en consola
```

### Componentes Clave:
* **Lexer (`src/parser/LenguajeMomoXDLexer.py`):** Escanea el flujo de caracteres, produce tokens tipificados e ignora comentarios iniciados con `#` y espacios en blanco.
* **Parser (`src/parser/LenguajeMomoXDParser.py`):** Evalúa la pertenencia sintáctica según la gramática libre de contexto y construye el árbol de análisis sintáctico.
* **Error Listener (`src/validador_momo_xd.py`):** Implementa un oyente personalizado que intercepta errores sintácticos de ANTLR4, impidiendo salidas crudas y ofreciendo diagnósticos en español con localización exacta.
* **Interfaz de Línea de Comandos (`ejecutar_dsl.py`):** Punto de entrada que procesa archivos `.xd`, resume métricas del programa y opcionalmente imprime el árbol jerárquico.

---

## 4. Estructura del Repositorio

La organización del proyecto preserva una distribución modular:

```text
LenguajePropio-xd/
├── grammar/
│   └── LenguajeMomoXD.g4         # Especificación formal de la gramática en ANTLR4
├── docs/
│   ├── alcance_catalogo.md      # Documento descriptivo de alcance y catálogo
│   └── gramatica_ebnf.md        # Notación en Forma de Backus-Naur Extendida (EBNF)
├── src/
│   ├── parser/                  # Módulos generados automáticamente por ANTLR4
│   │   ├── LenguajeMomoXDLexer.py
│   │   ├── LenguajeMomoXDParser.py
│   │   ├── LenguajeMomoXDVisitor.py
│   │   └── LenguajeMomoXDListener.py
│   └── validador_momo_xd.py     # Motor de validación sintáctica y oyente de diagnóstico
├── ejemplos/
│   ├── programa_correcto1.xd    # Caso de estudio: Ingesta, pipeline, agregación y guardado
│   ├── programa_correcto2.xd    # Caso de estudio: Exploración, ordenamiento y dispersión
│   ├── programa_incorrecto1.xd  # Caso negativo: Omisión del delimitador obligatorio 'xd'
│   └── programa_incorrecto2.xd  # Caso negativo: Expresiones y tuberías sintácticamente corruptas
├── datos/
│   └── ventas_prueba.csv        # Archivo CSV de prueba para validación de estructuras
├── tests/
│   └── test_corte1.py           # Batería de 9 pruebas unitarias automatizadas (unittest)
├── ejecutar_dsl.py              # CLI para ejecución y validación de programas .xd
├── Makefile                     # Automatización de tareas de compilación y pruebas
├── Proyecto_LP.pdf              # Guía del proyecto académico
└── README.md                    # Documentación técnica del proyecto
```

---

## 5. Catálogo de Instrucciones y Palabras Reservadas

MomoLang XD traduce conceptos formales de ciencia de datos a un lenguaje declarativo y estructurado:

### 5.1 Entrada, Salida y Persistencia
| Instrucción / Sintaxis | Descripción Formal | Ejemplo en MomoLang XD |
| :--- | :--- | :--- |
| `when haces expr xd` | Imprime expresiones, cadenas o literales en la consola. | `when haces "Iniciando analisis de datos..." xd` |
| `id = pasa_el_pack ruta xd` | Carga un archivo estructurado en formato CSV. | `ventas = pasa_el_pack "datos/ventas.csv" xd` |
| `... separador "s"` | Configura un delimitador personalizado de columnas en el CSV. | `datos = pasa_el_pack "datos.csv" separador ";" xd` |
| `subir_al_grupo id en ruta xd` | Exporta la estructura tabular resultante a un archivo CSV. | `subir_al_grupo resumen en "salidas/resumen.csv" xd` |

### 5.2 Operaciones en Pipeline (`|:v>`)
| Operación | Descripción | Ejemplo en MomoLang XD |
| :--- | :--- | :--- |
| `escojo_a [col1, col2, ...]` | Selecciona y proyecta un subconjunto de columnas. | `|:v> escojo_a [fecha, ciudad, categoria, total]` |
| `but_te_enteras_que condicion` | Filtra registros evaluando una condición booleana relacional. | `|:v> but_te_enteras_que precio > 50 y unidades > 0` |
| `el_futuro_es_hoy_oiste_viejo col = expr` | Incorpora una nueva columna derivada calculada aritméticamente. | `|:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio` |
| `ordenar_a_los_papus col criterio` | Ordena registros de forma ascendente o descendente. | `|:v> ordenar_a_los_papus total de_arriba_a_abajo` |

### 5.3 Agrupamiento y Métricas Estadísticas
| Instrucción | Función Estadística | Ejemplo en MomoLang XD |
| :--- | :--- | :--- |
| `juntar_a_la_grasa_por [cols]` | Agrupa el conjunto de datos por una o más dimensiones clave. | `|:v> juntar_a_la_grasa_por [ciudad]` |
| `sacar_cuentas res1 = fn(col), ...` | Aplica funciones descriptivas sobre los grupos definidos. | `|:v> sacar_cuentas tot = suma(total), cant = contar_papus()` |
| `suma(col)` | Sumatoria acumulada de valores numéricos. | `suma(total)` |
| `promedio(col)` / `media(col)` | Media aritmética de la variable. | `promedio(precio)` |
| `mediana(col)` | Mediana descriptiva (percentil 50). | `mediana(unidades)` |
| `el_mas_pro(col)` / `maximo(col)` | Valor máximo observado. | `el_mas_pro(ingreso)` |
| `el_mas_manco(col)` / `minimo(col)` | Valor mínimo observado. | `el_mas_manco(descuento)` |
| `desviacion_pro(col)` | Desviación estándar muestral. | `desviacion_pro(precio)` |
| `contar_papus()` | Frecuencia absoluta (recuento de filas en el grupo). | `contar_papus()` |

### 5.4 Especificación de Visualizaciones
MomoLang XD soporta el reconocimiento formal de 5 tipos de representaciones gráficas:
* `graficar_momos_en_barras <id> titulo "..." [eje_x "..."] [eje_y "..."] [guardar "..."] xd`
* `graficar_momos_en_lineas <id> titulo "..." [eje_x "..."] [eje_y "..."] [guardar "..."] xd`
* `graficar_momos_en_histograma <id> titulo "..." [columna "..."] [guardar "..."] xd`
* `graficar_momos_en_dispersion <id> titulo "..." [eje_x "..."] [eje_y "..."] [guardar "..."] xd`
* `graficar_momos_en_cajas <id> titulo "..." [columna "..."] [guardar "..."] xd`

---

## 6. Automatización del Proyecto con `Makefile`

El repositorio dispone de un **`Makefile`** multiplataforma (compatible con Linux, macOS y Windows) que permite ejecutar todas las acciones del sistema mediante instrucciones concisas:

| Comando Make | Descripción y Propósito |
| :--- | :--- |
| `make help` | Imprime el menú de ayuda con la descripción interactiva de cada comando. |
| `make build` | Compila la gramática formal ANTLR4 y regenera el analizador en `src/parser/`. |
| `make test` | Ejecuta la batería de pruebas unitarias automatizadas sobre el reconocedor sintáctico. |
| `make run` | Ejecuta la validación sintáctica del programa de prueba `ejemplos/programa_correcto1.xd`. |
| `make run-tree` | Valida el programa correcto y despliega en terminal el árbol sintáctico estructurado. |
| `make run-incorrect` | Ejecuta el validador sobre un programa incorrecto, demostrando la captura de errores. |
| `make clean` | Remueve archivos transitorios, residuos de compilación y directorios `__pycache__`. |

### Flujo de Trabajo Recomendado:

```bash
# Paso 1: Ejecutar la suite de pruebas unitarias automatizadas
make test

# Paso 2: Validar un programa válido y observar las métricas de sentencias reconocidas
make run

# Paso 3: Visualizar la estructura jerárquica del Parse Tree
make run-tree

# Paso 4: Evaluar el comportamiento del reconocedor ante errores sintácticos
make run-incorrect
```

---

## 7. Ejecución Manual Alternativa

Si se desea interactuar directamente con el intérprete sin recurrir a Make:

### 7.1 Dependencias Requeridas
* **Python 3.10 o superior**
* **Runtime de Python para ANTLR4 (versión 4.13.2):**
  ```bash
  pip install antlr4-python3-runtime==4.13.2
  ```

### 7.2 Compilación Manual de la Gramática
```bash
antlr4 -Dlanguage=Python3 -visitor -o src/parser grammar/LenguajeMomoXD.g4
```

### 7.3 Ejecución de Pruebas Unitarias
```bash
python -m unittest tests/test_corte1.py -v
```

### 7.4 Validación de Archivos `.xd` desde la CLI
* **Validación estándar:**
  ```bash
  python ejecutar_dsl.py ejemplos/programa_correcto1.xd
  ```
* **Validación con despliegue de árbol sintáctico:**
  ```bash
  python ejecutar_dsl.py ejemplos/programa_correcto1.xd --arbol
  ```
* **Prueba de diagnóstico de errores:**
  ```bash
  python ejecutar_dsl.py ejemplos/programa_incorrecto1.xd
  ```

---

## 8. Verificación y Suite de Pruebas Automatizadas

El archivo `tests/test_corte1.py` contiene **9 pruebas unitarias** que certifican el comportamiento riguroso del analizador frente a diversos escenarios sintácticos:

1. `test_aceptar_programa_correcto_1_xd`: Flujo integral de ingesta, pipeline de transformación, agregación y guardado.
2. `test_aceptar_programa_correcto_2_xd`: Pipeline exploratorio con ordenamiento y declaración de gráficos de dispersión.
3. `test_aceptar_pipeline_completo_con_operador_momo_xd`: Encadenamiento de múltiples operaciones consecutivas mediante `|:v>`.
4. `test_aceptar_sentencia_imprimir_when_haces_xd`: Sentencias de impresión con literales y expresiones evaluables.
5. `test_aceptar_instrucciones_visualizacion_todas_xd`: Reconocimiento léxico-sintáctico de los 5 tipos de visualizaciones.
6. `test_rechazar_programa_sin_terminador_xd`: Rechazo riguroso ante la omisión del sufijo delimitador `xd`.
7. `test_rechazar_palabra_desconocida_o_token_invalido_xd`: Detección de identificadores ilegítimos en lugar de palabras clave.
8. `test_rechazar_programa_con_sintaxis_corrupta_xd`: Identificación de expresiones aritméticas truncadas o mal formadas.
9. `test_rechazar_operador_relacional_faltante_xd`: Detección de cláusulas condicionales desprovistas de operador relacional.

Todas las pruebas se ejecutan de manera determinista y reportan un estado de satisfacción total (`OK`).

---

## 9. Ejemplo de Código Fuente en MomoLang XD

A continuación se ilustra un programa completo representativo (`ejemplos/programa_correcto1.xd`):

```dsl
# =======================================================
# Análisis de Ventas y Agregación Estadística en MomoLang XD
# =======================================================

when haces "Iniciando analisis de datos de la grasa..." xd

# Ingesta del archivo estructurado
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd

# Transformación funcional mediante pipeline
ventas_limpias = ventas 
    |:v> escojo_a [fecha, ciudad, categoria, unidades, precio]
    |:v> but_te_enteras_que unidades > 10
    |:v> el_futuro_es_hoy_oiste_viejo total = unidades * precio xd

# Agrupamiento por dimensión y cálculo de métricas agregadas
resumen_ciudades = ventas_limpias 
    |:v> juntar_a_la_grasa_por [ciudad]
    |:v> sacar_cuentas total_ventas = suma(total), promedio_unidades = promedio(unidades), total_filas = contar_papus() xd

# Persistencia del conjunto de datos transformado
subir_al_grupo resumen_ciudades en "salidas/resumen_ciudades_momo.csv" xd

# Declaración de visualización gráfica
graficar_momos_en_barras resumen_ciudades titulo "Ingresos por Ciudad Grasosa" eje_x "Ciudad" eje_y "Total ($)" guardar "salidas/grafico_momo_barras.svg" xd

when haces "Analisis finalizado exitosamente papu xd" xd
```
