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
- **Validación Léxica y Sintáctica (Corte 1):** El sistema procesa archivos de código `.xd` determinando si son **[ACEPTADOS]** (mostrando el árbol sintáctico estructurado y métricas) o **[RECHAZADOS]** (reportando línea, columna y causa del error sintáctico).
- **Cero Dependencias Externas de Ciencia de Datos:** Toda la lógica de ejecución para los siguientes cortes se apoya en librerías propias desarrolladas desde cero en Python puro.

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
│   ├── validador_momo_xd.py     # Validador y formateador de árbol sintáctico
│   └── core/                    # Motor de librerías propias (matemática, datos, gráficos)
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

## 5. Instrucciones de Instalación y Ejecución

### 5.1 Requisitos Previos
* **Python 3.10+**
* **ANTLR4** (v4.13+)
* Runtime de Python para ANTLR4:
  ```bash
  pip install antlr4-python3-runtime==4.13.2
  ```

### 5.2 Compilar la Gramática ANTLR4
Para regenerar el lexer y parser en Python a partir del archivo `.g4`:
```bash
antlr4 -Dlanguage=Python3 -visitor -o src/parser grammar/LenguajeMomoXD.g4
```

### 5.3 Ejecutar las Pruebas Unitarias del Corte 1
Para ejecutar la suite automatizada de pruebas de aceptación y rechazo:
```bash
python3 -m unittest tests/test_corte1.py -v
```

### 5.4 Validar un Programa con la CLI
Para validar un archivo `.xd` y comprobar si es **Aceptado** o **Rechazado**:

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
