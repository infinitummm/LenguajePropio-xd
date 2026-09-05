# Proyecto de Curso: MomoLang XD (`.xd`) - Lenguaje de Dominio Específico

**Asignatura:** Lenguajes de Programación y Transducción  

**Universidad Sergio Arboleda** — Programa de Ciencias de la Computación e Inteligencia Artificial  

**Estudiantes:** Dylan Torres - Juan Gomez - Javier Rosero

**Docente:** Joaquín F. Sánchez | **Semestre:** 2026-2  

---

## 1. Descripción General

**MomoLang XD** es un Lenguaje de Dominio Específico (DSL) declarativo y temático diseñado para expresar flujos reproducibles de ciencia de datos: carga de archivos CSV, selección de columnas, filtrado relacional, creación de columnas calculadas, ordenamiento, agregaciones descriptivas y generación de visualizaciones vectoriales.

El lenguaje adopta una temática única inspirada en la **cultura de momos / memes hispanoamericanos** y establece una regla sintáctica fundamental: **cada sentencia del lenguaje debe terminar obligatoriamente con el sufijo `xd`**.

### Características Destacadas:
- **Terminador Obligatorio:** Toda sentencia finaliza con `xd` (ej. `when haces "Hola" xd`).
- **Operador de Tubería:** `|:v>` (o `|>`) para encadenamiento funcional y transformaciones declarativas.
- **Validación Léxica y Sintáctica:** El sistema procesa archivos de código `.xd` determinando si son **[ACEPTADOS]** (mostrando el árbol sintáctico estructurado y métricas) o **[RECHAZADOS]** (reportando línea, columna y causa del error sintáctico).

---

## 2. Arquitectura del Front-end (Corte 1)

```
Programa Fuente (.xd) ──> Lexer ANTLR4 (Tokens) ──> Parser ANTLR4 (Reglas)
                                                            │
                                                            ▼
                                                ¿Errores Léxicos/Sintácticos?
                                                  ├─ SÍ ─> [ RECHAZADO xd ] (Línea:Columna + Diagnóstico)
                                                  └─ NO ─> [ ACEPTADO :v ] (Parse Tree + Estadísticas)
```

---

## 3. Estructura del Repositorio

```
.
├── grammar/
│   └── LenguajeMomoXD.g4         # Gramática formal ANTLR4 (Lexer y Parser)
├── docs/
│   ├── alcance_catalogo.md      # Catálogo completo de instrucciones y alcance
│   └── gramatica_ebnf.md        # Especificación formal de la gramática en EBNF
├── ejemplos/
│   ├── programa_correcto1.xd    # Flujo completo de ventas y agregación
│   ├── programa_correcto2.xd    # Análisis exploratorio y dispersión
│   ├── programa_incorrecto1.xd  # Rechazado: Omisión del 'xd' final
│   └── programa_incorrecto2.xd  # Rechazado: Pipeline y expresiones rotas
├── src/
│   ├── parser/                  # Código Lexer/Parser generado por ANTLR4
│   │   ├── LenguajeMomoXDLexer.py
│   │   ├── LenguajeMomoXDParser.py
│   │   └── LenguajeMomoXDVisitor.py
│   └── validador_momo_xd.py     # Validador y formateador de árbol sintáctico
├── tests/
│   └── test_corte1.py           # Pruebas unitarias de aceptación y rechazo
├── ejecutar_dsl.py              # CLI principal para validar archivos .xd
└── README.md                    # Documentación del proyecto
```

---

## 4. Catálogo Rápido de Instrucciones

| Función / Propósito | Instrucción MomoLang XD | Ejemplo |
| :--- | :--- | :--- |
| **Imprimir en consola** | `when haces` | `when haces "Iniciando analisis..." xd` |
| **Cargar CSV** | `pasa_el_pack` / `pasa_el_zelda` | `ventas = pasa_el_pack "datos.csv" xd` |
| **Exportar CSV** | `subir_al_grupo` / `guardar_momo` | `subir_al_grupo resumen en "resumen.csv" xd` |
| **Seleccionar columnas** | `escojo_a` / `escojo_a_los_papus` | `\|:v> escojo_a [fecha, ciudad, precio]` |
| **Filtrar registros** | `but_te_enteras_que` / `but_ella_no_te_ama` | `\|:v> but_te_enteras_que precio > 50` |
| **Columna calculada** | `el_futuro_es_hoy_oiste_viejo` | `\|:v> el_futuro_es_hoy_oiste_viejo total = u * p` |
| **Ordenar filas** | `ordenar_a_los_papus` | `\|:v> ordenar_a_los_papus total de_arriba_a_abajo` |
| **Agrupar datos** | `juntar_a_la_grasa_por` | `\|:v> juntar_a_la_grasa_por [ciudad]` |
| **Resumir agregaciones**| `sacar_cuentas` | `\|:v> sacar_cuentas total = suma(total), cant = contar_papus()` |
| **Visualización** | `graficar_momos_en_barras` ... | `graficar_momos_en_barras df titulo "Ventas" xd` |

---

## 5. Ejecución Rápida usando el Makefile (Recomendado)

El repositorio incluye un **`Makefile`** que automatiza todas las tareas esenciales (compilación, pruebas unitarias y validación) con comandos directos de una sola palabra:

| Comando | Acción Realizada |
| :--- | :--- |
| `make help` | Despliega el menú interactivo con la lista de todos los comandos disponibles. |
| `make build` *(o `make antlr`)* | Compila la gramática ANTLR4 (`grammar/LenguajeMomoXD.g4`) y genera el Lexer y Parser en `src/parser/`. |
| `make test` | Ejecuta la suite completa de **9 pruebas unitarias automatizadas** del Corte 1 (aceptación y rechazo). |
| `make run` | Valida el archivo `ejemplos/programa_correcto1.xd` confirmando el estado **[ACEPTADO]** y sus métricas. |
| `make run-tree` | Valida el programa correcto y despliega en terminal el **Árbol Sintáctico (Parse Tree) jerárquico completo**. |
| `make run-incorrect` | Prueba el validador con `ejemplos/programa_incorrecto1.xd`, demostrando el diagnóstico de **[RECHAZADO]**. |
| `make clean` | Limpia los archivos temporales y la caché de Python (`__pycache__`, `.pyc`). |

### 5.1 Flujo Rápido de Demostración con `make`
Para sustentar o probar el proyecto rápidamente en la terminal:

```bash
# 1. Ejecutar las pruebas unitarias automatizadas
make test

# 2. Validar un programa correcto y ver métricas
make run

# 3. Validar e inspeccionar el árbol sintáctico jerárquico
make run-tree

# 4. Probar la detección y diagnóstico de errores sintácticos
make run-incorrect
```

---

## 6. Ejecución Alternativa Manual (CLI Directa con Python)

Si prefieres no usar `make` o estás en un entorno sin Make instalado, puedes ejecutar los comandos directamente con Python:

### 6.1 Requisitos Previos
* **Python 3.10+**
* Runtime de Python para ANTLR4:
  ```bash
  pip install antlr4-python3-runtime==4.13.2
  ```

### 6.2 Compilar la Gramática ANTLR4 (Manual)
```bash
antlr4 -Dlanguage=Python3 -visitor -o src/parser grammar/LenguajeMomoXD.g4
```

### 6.3 Ejecutar las Pruebas Unitarias (Manual)
```bash
python3 -m unittest tests/test_corte1.py -v
```

### 6.4 Validar Archivos .xd con la CLI (Manual)
* **Programa Válido:**
  ```bash
  python3 ejecutar_dsl.py ejemplos/programa_correcto1.xd
  ```

* **Programa Válido con Árbol Sintáctico Jerárquico Completo:**
  ```bash
  python3 ejecutar_dsl.py ejemplos/programa_correcto1.xd --arbol
  ```

* **Programa Inválido (Diagnóstico de Errores):**
  ```bash
  python3 ejecutar_dsl.py ejemplos/programa_incorrecto1.xd
  ```
