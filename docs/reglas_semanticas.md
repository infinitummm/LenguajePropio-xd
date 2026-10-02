# Especificación de Reglas Semánticas y Tabla de Símbolos
## Fase 2: Semántica y Procesamiento de Datos
### Lenguaje: MomoLang XD (`.xd`)

**Asignatura:** Lenguajes de Programación y Transducción  
**Universidad Sergio Arboleda** — Ciencias de la Computación e Inteligencia Artificial  
**Semestre:** 2026-2

---

## 1. Introducción y Arquitectura Semántica

La fase semántica de **MomoLang XD** valida el significado, la coherencia de tipos y la validez de los datos que viajan a través de los programas analizados sintácticamente por ANTLR4.

La arquitectura se compone de:
1. **`TablaSimbolos` (`src/semantica/tabla_simbolos.py`):** Estructura jerárquica con soporte de ámbitos (global y locales) para registrar variables, tipos, valores en tiempo de ejecución y metadatos (como nombres de columnas en tablas).
2. **`VisitorEjecutor` (`src/semantica/visitor_ejecutor.py`):** Patrón Visitor que recorre el Árbol de Análisis Sintáctico (Parse Tree), validando reglas semánticas y delegando las transformaciones a los motores de Python Puro (`TablaMomo` y `VectorMomo`).
3. **Manejo Diagnóstico de Excepciones (`ErrorSemantico`):** Captura inconsistencias semánticas e informa al usuario con número de línea, columna y sugerencia correctiva.

---

## 2. Sistema de Tipos del DSL

MomoLang clasifica los valores en cinco tipos fundamentales:

| Tipo Semántico | Descripción | Ejemplos / Representación |
| :--- | :--- | :--- |
| `TABLA` | Estructura bidimensional de filas y columnas (`TablaMomo`). | Resultado de `pasa_el_pack` o de transformaciones con `\|:v>`. |
| `VECTOR` | Serie unidimensional homogénea (`VectorMomo`). | Columnas numéricas individuales durante cálculos de expresiones. |
| `NUMERO` | Escalar numérico (entero `int` o flotante `float`). | `10`, `3.1416`, `50000`. |
| `TEXTO` | Cadena alfanumérica (`str`). | `"Bogota"`, `"datos/ventas.csv"`. |
| `BOOLEANO` | Valor de verdad (`bool` o vector booleano / máscara). | `True`, `False`, o máscara producida por `unidades > 10`. |

---

## 3. Catálogo Formal de Reglas Semánticas

### Regla 1: Definición Previa de Variables (Scope & Declaration)
* **Enunciado:** Ningún identificador puede ser referenciado en una expresión, tubería o asignación sin haber sido previamente definido en el ámbito actual o en un ámbito superior.
* **Violación:** `res = tabla_fantasma |:v> escojo_a [ciudad] xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La variable 'tabla_fantasma' no ha sido definida.`

---

### Regla 2: Compatibilidad de Tuberías (Pipeline Validity)
* **Enunciado:** El operador de tubería `|:v>` (o `|>`) solo puede aplicarse sobre expresiones que evalúen al tipo `TABLA`. No es válido encadenar tuberías sobre tipos primitivos (`NUMERO`, `TEXTO`).
* **Violación:** `x = 50 |:v> escojo_a [col] xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La operación de tubería (|:v>) requiere una TABLA, pero se recibió 'NUMERO'.`

---

### Regla 3: Existencia de Columnas en Operaciones Tabulares
* **Enunciado:** Toda columna referenciada dentro de `escojo_a`, `but_te_enteras_que`, `el_futuro_es_hoy_oiste_viejo`, `juntar_a_la_grasa_por` o `ordenar_a_los_papus` debe pertenecer al conjunto de columnas activas del dataset sobre el que se opera.
* **Violación:** `ventas |:v> el_futuro_es_hoy_oiste_viejo total = unidades * comision_inventada xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La columna 'comision_inventada' no existe en el dataset. Columnas disponibles: ['fecha', 'ciudad', 'categoria', 'unidades', 'precio']`

---

### Regla 4: Compatibilidad de Tipos en Operaciones Aritméticas
* **Enunciado:** Los operadores aritméticos binarios (`+`, `-`, `*`, `/`) son válidos únicamente entre:
  1. Dos escalares numéricos (`NUMERO` y `NUMERO`).
  2. Dos columnas vectoriales de igual longitud (`VECTOR` y `VECTOR`).
  3. Un vector numérico y un escalar numérico (`VECTOR` y `NUMERO`).
* **Violación:** Sumar una columna de texto con un número, o intentar dividir por cero.
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: Operación aritmética inválida entre 'TEXTO' y 'NUMERO'.`

---

### Regla 5: Validez de Funciones de Agregación
* **Enunciado:** En la cláusula `juntar_a_la_grasa_por [...] calcular [...]`, únicamente se admiten las funciones de agregación definidas en el catálogo (`suma`, `promedio`, `media`, `mediana`, `el_mas_pro`, `maximo`, `el_mas_manco`, `minimo`, `desviacion_pro`, `contar_papus`).
* Además, la columna agregada debe existir y ser de tipo numérico (excepto `contar_papus`, aplicable a cualquier columna).
* **Violación:** `... calcular [ magia(total) como meta ] xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: Función de agregación 'magia' no reconocida.`

---

### Regla 6: Validez en la Estructura Condicional
* **Enunciado:** La condición dentro de `si_pasa_esto (condicion)` debe ser evaluable a un valor booleano o numérico para determinar la bifurcación del flujo. Los símbolos asignados dentro del bloque condicional quedan registrados en el ámbito local o actual.

---

## 4. Estructura de la Tabla de Símbolos

Cada entrada en la `TablaSimbolos` contiene:
```python
class Simbolo:
    nombre: str          # Identificador de la variable
    tipo: str            # 'TABLA', 'VECTOR', 'NUMERO', 'TEXTO', 'BOOLEANO'
    valor: Any           # Instancia de TablaMomo, VectorMomo o valor nativo
    columnas: list[str]  # Lista de columnas activas si el tipo es TABLA
    linea: int           # Línea donde fue declarada
    columna: int         # Columna donde fue declarada
```

La tabla soporta:
* `definir(nombre, tipo, valor, columnas)`: Registra o actualiza un símbolo.
* `buscar(nombre)`: Búsqueda ascendente a través de los ámbitos anidados.
* `existe(nombre)`: Comprobación rápida de existencia.
* `empujar_ambito()` / `sacar_ambito()`: Gestión de bloques locales en condicionales y subrutinas.

---

## 5. Ejemplo de Detección de Error Semántico

Dado el programa erróneo `ejemplos/programa_error_semantico.xd`:
```momo
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd
ventas_error = ventas |:v> el_futuro_es_hoy_oiste_viejo total = unidades * comision_inventada xd
```

La ejecución produce la siguiente salida en consola con código de salida `2`:
```text
======================================================================
  ESTADO SEMÁNTICO: [ ERROR SEMÁNTICO DETECTADO xd ]
======================================================================
  [Error Semántico xd] [Línea 9, Col 26]: La columna 'comision_inventada' no existe en el dataset. Columnas disponibles: ['fecha', 'ciudad', 'categoria', 'unidades', 'precio']
======================================================================
```
