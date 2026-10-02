# Especificación de Reglas Semánticas, Tabla de Símbolos y Control de Flujo
## Fase 2: Semántica, Control de Flujo y Procesamiento de Datos
### Lenguaje: MomoLang XD (`.xd`)

**Asignatura:** Lenguajes de Programación y Transducción  
**Universidad Sergio Arboleda** — Ciencias de la Computación e Inteligencia Artificial  
**Semestre:** 2026-2

---

## 1. Introducción y Arquitectura Semántica

La fase semántica de **MomoLang XD** valida el significado, la coherencia de tipos y la validez de los datos y estructuras de control que viajan a través de los programas analizados sintácticamente por ANTLR4.

La arquitectura se compone de:
1. **`TablaSimbolos` (`src/semantica/tabla_simbolos.py`):** Estructura jerárquica con soporte de ámbitos (global y locales) para registrar variables, funciones de usuario, tipos, valores en tiempo de ejecución y metadatos (como nombres de columnas en tablas).
2. **`VisitorEjecutor` (`src/semantica/visitor_ejecutor.py`):** Patrón Visitor que recorre el Árbol de Análisis Sintáctico (Parse Tree), validando reglas semánticas y ejecutando directamente el programa: asignaciones, condicionales, ciclos, funciones y operaciones tabulares con Python Puro.
3. **Manejo Diagnóstico de Excepciones (`ErrorSemantico`):** Captura inconsistencias semánticas e informa al usuario con número de línea, columna y sugerencia correctiva.

---

## 2. Sistema de Tipos del Lenguaje

MomoLang clasifica los valores en los siguientes tipos semánticos:

| Tipo Semántico | Descripción | Ejemplos / Representación |
| :--- | :--- | :--- |
| `TABLA` | Estructura bidimensional de filas y columnas (`TablaMomo`). | Resultado de `pasa_el_pack` o transformaciones `\|:v>`. |
| `VECTOR` | Serie unidimensional homogénea (`VectorMomo`). | Columnas numéricas individuales durante cálculos. |
| `NUMERO` | Escalar numérico (entero `int` o flotante `float`). | `10`, `3.1416`, `50000`. |
| `CADENA` | Cadena alfanumérica (`str`). | `"Bogota"`, `"datos/ventas.csv"`. |
| `BOOLEANO` | Valor de verdad (`bool` o vector de máscaras booleanas). | `True`, `False`, o máscara producida por `unidades > 10`. |
| `FUNCION` | Subrutina definida por el usuario (`SimboloFuncion`). | Parámetros formales, cuerpo AST y ámbito léxico. |
| `AGRUPAMIENTO` | Conjunto particionado de datos tabulares (`AgrupamientoMomo`). | Resultado de `juntar_a_la_grasa_por`. |

---

## 3. Catálogo Formal de Reglas Semánticas

### Regla 1: Definición Previa de Variables (Scope & Declaration)
* **Enunciado:** Ningún identificador puede ser referenciado en una expresión, tubería, condicional o ciclo sin haber sido previamente definido en el ámbito actual o en un ámbito superior.
* **Violación:** `res = tabla_fantasma |:v> escojo_a [ciudad] xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La variable 'tabla_fantasma' no ha sido declarada ni cargada antes de usarse.`

---

### Regla 2: Reglas de Funciones de Usuario (Aridad y Ámbito)
* **Enunciado:** Al invocar una función de usuario, el número de argumentos suministrados debe coincidir exactamente con el número de parámetros formales declarados (aridad estricta).
* Además, la función se ejecuta en su propio ámbito local hijo (`TablaSimbolos.crear_hijo()`), garantizando el aislamiento de variables locales.
* La sentencia de retorno (`suelta_el_momo`) interrumpe la ejecución del bloque de la función y devuelve el valor evaluado al llamador mediante desenrollado controlado de pila.
* **Violación:** `calcular_precio_final(1000)` cuando la función espera 3 parámetros.
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La función 'calcular_precio_final' espera 3 argumento(s) pero recibió 1.`

---

### Regla 3: Reglas Semánticas en Ciclos (Loops)
* **Enunciado para `mientras_el_papu`:** La condición del bucle debe ser evaluable a un valor booleano o numérico. Se incluye un límite de salvaguarda de iteraciones para proteger contra bucles infinitos.
* **Enunciado para `para_cada_papu`:** Los límites del rango (`desde` y `hasta`) deben evaluarse a valores convertibles a enteros (`int`). La variable de iteración se actualiza en cada paso en el entorno activo.
* **Violación:** `para_cada_papu i desde "inicio" hasta 10 haz_esto`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: Los límites de 'para_cada_papu' deben ser enteros. Se recibió desde=inicio, hasta=10.`

---

### Regla 4: Compatibilidad de Tuberías (Pipeline Validity)
* **Enunciado:** El operador de tubería `|:v>` (o `|>`) solo puede aplicarse sobre expresiones que evalúen al tipo `TABLA`. No es válido encadenar tuberías sobre tipos primitivos (`NUMERO`, `CADENA`).
* **Violación:** `x = 50 |:v> escojo_a [col] xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La operación 'escojo_a' solo puede aplicarse sobre una tabla de datos.`

---

### Regla 5: Existencia de Columnas en Operaciones Tabulares
* **Enunciado:** Toda columna referenciada dentro de `escojo_a`, `but_te_enteras_que`, `el_futuro_es_hoy_oiste_viejo`, `juntar_a_la_grasa_por` o `ordenar_a_los_papus` debe pertenecer al conjunto de columnas activas del dataset sobre el que se opera.
* **Violación:** `ventas |:v> el_futuro_es_hoy_oiste_viejo total = unidades * comision_inventada xd`
* **Diagnóstico emitido:** `[Error Semántico xd] [Línea L, Col C]: La columna 'comision_inventada' no existe en el dataset. Columnas disponibles: ['fecha', 'ciudad', 'categoria', 'unidades', 'precio']`

---

### Regla 6: Compatibilidad de Tipos en Operaciones Aritméticas
* **Enunciado:** Los operadores aritméticos binarios (`+`, `-`, `*`, `/`) son válidos entre:
  1. Dos escalares numéricos (`NUMERO` y `NUMERO`).
  2. Dos columnas vectoriales de igual longitud (`VECTOR` y `VECTOR`).
  3. Un vector numérico y un escalar numérico (`VECTOR` y `NUMERO`).
  4. Para el operador `+`, si uno de los operandos es `CADENA`, se realiza concatenación textual automática.

---

### Regla 7: Validez de Funciones de Agregación
* **Enunciado:** En la cláusula de agregación (`calcular` o `sacar_cuentas`), únicamente se admiten las funciones de agregación definidas en el catálogo (`suma`, `promedio`, `media`, `mediana`, `el_mas_pro`, `maximo`, `el_mas_manco`, `minimo`, `desviacion_pro`, `contar_papus`).
* La columna agregada debe existir y ser de tipo numérico (excepto `contar_papus`, aplicable a cualquier columna o sin argumentos).

---

## 4. Estructura de la Tabla de Símbolos

Cada entrada en la `TablaSimbolos` contiene:
```python
class Simbolo:
    nombre: str          # Identificador de la variable o función
    tipo: str            # 'TABLA', 'VECTOR', 'NUMERO', 'CADENA', 'BOOLEANO', 'FUNCION'
    valor: Any           # Instancia de TablaMomo, VectorMomo, SimboloFuncion o valor primitivo
    metadatos: dict      # Metadatos auxiliares (columnas de tablas, cantidad de filas)
```

Las funciones se modelan mediante:
```python
class SimboloFuncion:
    nombre: str               # Nombre de la función
    parametros: list[str]     # Lista de nombres de parámetros formales
    cuerpo_ctx: Any           # Nodo AST (bloque) para ser ejecutado
    ambito_definicion: TablaSimbolos # Entorno donde fue declarada (cierre léxico)
```

La tabla soporta:
* `definir(nombre, valor, tipo)`: Registra o actualiza un símbolo en el ámbito actual.
* `asignar_existente_o_local(nombre, valor)`: Actualiza la variable en el ámbito correspondiente (permitiendo contadores en bucles sin sobreescritura accidental).
* `definir_funcion(nombre, parametros, cuerpo_ctx)`: Registra funciones de usuario.
* `obtener(nombre)`: Búsqueda ascendente a través de los ámbitos anidados.
* `crear_hijo()`: Genera un nuevo entorno léxico subordinado para funciones o bloques condicionales.

---

## 5. Ejemplo de Detección de Error Semántico

Dado el programa erróneo `ejemplos/programa_error_semantico.xd`:
```momo
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd
ventas_error = ventas |:v> el_futuro_es_hoy_oiste_viejo total = unidades * comision_inventada xd
```

La ejecución produce la siguiente salida en consola con código de salida `2`:
```text
=================================================================
  ESTADO: [ ERROR SEMÁNTICO DETECTADO xd ]
=================================================================
  [Error Semántico xd] [Línea 9, Col 26]: La columna 'comision_inventada' no existe en el dataset. Columnas disponibles: ['fecha', 'ciudad', 'categoria', 'unidades', 'precio']
=================================================================
```
