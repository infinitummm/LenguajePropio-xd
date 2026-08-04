# Proyecto de Curso: Lenguaje de Dominio Específico (DSL) para Ciencia de Datos y Visualización xd

**Asignatura:** Lenguajes de Programación y Transducción  
**Universidad Sergio Arboleda** - Programa de Ciencias de la Computación e Inteligencia Artificial  
**Docente:** Joaquín F. Sánchez | **Semestre:** 2026-2

---

## 📌 Descripción General
Este proyecto implementa un Lenguaje de Dominio Específico (DSL) declarativo en español para flujos reproducibles de ciencia de datos (carga de archivos CSV, filtrado, selección de columnas, agrupamiento con estadísticas y generación de visualizaciones SVG).

El sistema destaca por utilizar **tres motorizaciones/librerías propias creadas 100% desde cero en Python** sin depender de librerías externas de terceros como Pandas, NumPy o Matplotlib.

---

## 🏗️ Arquitectura del Sistema

```
Programa Fuente (.dsl) ──> Lexer & Parser (ANTLR4) ──> Parse Tree
                                                            │
                                                            ▼
Tablas CSV & Gráficos SVG ◄── Motor Propio Python ◄── Visitor Semántico
```

---

## 🚀 Estructura del Proyecto

```
.
├── grammar/
│   └── LenguajeDatos.g4         # Gramática formal en ANTLR4
├── docs/
│   ├── alcance_catalogo.md      # Alcance y catálogo de instrucciones
│   └── gramatica_ebnf.md        # Especificación EBNF de la gramática
├── ejemplos/
│   ├── programa_correcto1.dsl   # Ejemplo 1 de código DSL válido
│   ├── programa_correcto2.dsl   # Ejemplo 2 de código DSL válido
│   └── programa_incorrecto.dsl  # Ejemplo con errores para validación
├── src/
│   ├── core/                    # Librerías propias desde cero en español (_xd)
│   │   ├── matematica_propia.py # Reemplazo propio de NumPy
│   │   ├── datos_propios.py     # Reemplazo propio de Pandas (TablaDatos/Serie)
│   │   └── graficos_propios.py  # Reemplazo propio de Matplotlib (SVG Engine)
│   ├── parser/                  # Código lexer/parser generado por ANTLR4
│   ├── lexer_parser_runner.py   # Runner de análisis léxico y sintáctico
│   └── visitor_ejecutor.py      # Evaluador semántico por patrón Visitor
├── tests/
│   ├── probar_librerias.py      # Pruebas unitarias de las librerías propias
│   └── test_corte1.py           # Pruebas léxicas, sintácticas e integración del Corte 1
├── ejecutar_dsl.py              # CLI para ejecutar programas .dsl
└── demostracion_librerias.py    # Demostración del motor interno
```

---

## 💻 Instrucciones de Ejecución

### 1. Ejecutar Pruebas Unitarias e Integración (Corte 1)
```bash
python -m unittest tests/test_corte1.py
```

### 2. Ejecutar un Programa escrito en el DSL
```bash
python ejecutar_dsl.py ejemplos/programa_correcto1.dsl
```

### 3. Probar Diagnóstico de Errores Sintácticos
```bash
python ejecutar_dsl.py ejemplos/programa_incorrecto.dsl
```
