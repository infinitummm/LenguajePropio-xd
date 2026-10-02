# Manual de Usuario: MomoLang XD (.xd) :v
### Guía Completa de Uso y Funcionamiento del Lenguaje de la Grasa

¡Bienvenido al manual oficial de **MomoLang XD**! Este documento está escrito en lenguaje natural, claro y directo para que entiendas sin rodeos cómo funciona el lenguaje, qué hace cada instrucción, cómo procesa los datos y cómo puedes crear tus propios programas con asignaciones, condicionales, ciclos, funciones y análisis de datos sin depender de librerías externas.

---

## 1. ¿Qué es MomoLang XD?

**MomoLang XD** es un Lenguaje de Programación y DSL creado tanto para programación general (control de flujo, funciones, variables) como para ciencia de datos (carga de CSV, transformaciones, filtros, agrupaciones y estadísticas).

En lugar de usar la sintaxis fría y compleja de librerías tradicionales como Pandas o SQL, MomoLang utiliza la jerga y cultura de la grasa / momos de internet. Todo el motor de cálculo y procesamiento está construido en **Python Puro desde cero**, sin ninguna dependencia externa (cero Pandas, cero NumPy).

### La Regla de Oro del Lenguaje
> **Toda sentencia en MomoLang XD debe terminar OBLIGATORIAMENTE con `xd` (o en mayúsculas `XD` / `xD`).**  
> Si se te olvida poner `xd` al final de una línea, el analizador sintáctico te marcará error de inmediato.

---

## 2. Variables y Asignación

En MomoLang puedes crear variables y asignarles cualquier valor (números enteros, decimales, texto, booleanos, resultados de operaciones, funciones o tablas completas):

```momo
# Variables numéricas y de texto
precio = 50000 xd
descuento_porcentaje = 10 xd
nombre_cliente = "Dylan" xd

# Asignación de expresiones aritméticas
descuento = precio * descuento_porcentaje / 100 xd
precio_final = precio - descuento xd

# Asignación de tablas de datos
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd
```

---

## 3. Manejo de Condicionales (`si_el_papu` / `si_pasa_esto`)

Permite ejecutar bloques de código de forma condicional evaluando comparaciones lógicas:

```momo
si_el_papu saldo > 200000 entonces
    when haces "El papu tiene saldo suficiente :v" xd
sino_callese_senora
    when haces "Fondos insuficientes xd" xd
fin_del_momo xd
```

* **Palabras reservadas aceptadas:**
  * Para iniciar: `si_el_papu`, `si_pasa_esto`, `si`
  * Para la rama afirmativa: `entonces`, `haz_esto`
  * Para la rama alternativa: `sino_callese_senora`, `pero_si_no`, `sino`
  * Para cerrar el bloque: `fin_del_momo`, `fin_del_si`

### Operadores de Comparación y Lógicos:
* Comparaciones: `==`, `!=`, `>`, `<`, `>=`, `<=`
* Operadores lógicos: `y_ademas` (`&&`), `o_bien` (`||`), `no_es_cierto` (`!`)

---

## 4. Ciclos y Bucles

### 4.1 Bucle Mientras (`mientras_el_papu` / `mientras_tanto` / `mientras`)
Repite un bloque de código mientras una condición lógica sea verdadera (ideal para contadores y algoritmos iterativos):

```momo
contador = 1 xd
mientras_el_papu contador <= 5 haz_esto
    when haces "Iteracion #" + contador xd
    contador = contador + 1 xd
fin_del_bucle xd
```

### 4.2 Bucle Para (`para_cada_papu` / `por_cada_uno` / `para`)
Itera automáticamente una variable sobre un rango numérico `desde ... hasta ...` de forma inclusiva:

```momo
para_cada_papu i desde 1 hasta 4 haz_esto
    cuadrado = i * i xd
    when haces "El cuadrado de " + i + " es: " + cuadrado xd
fin_del_bucle xd
```

---

## 5. Funciones Definidas por el Usuario (`momo_funcion`)

Puedes crear tus propias subrutinas reutilizables con parámetros y devolver resultados usando sentencias de retorno:

```momo
# Definición de la función
momo_funcion calcular_precio_final(precio_base, impuesto, descuento)
    monto_impuesto = precio_base * impuesto / 100 xd
    monto_descuento = precio_base * descuento / 100 xd
    total = precio_base + monto_impuesto - monto_descuento xd
    suelta_el_momo total xd
fin_de_la_funcion xd

# Invocación de la función
total_compra = calcular_precio_final(100000, 19, 10) xd
when haces "Total a pagar: " + total_compra xd
```

* **Palabras para declarar funciones:** `momo_funcion`, `funcion_papu`, `rutina_momo`, `funcion`.
* **Palabras de retorno:** `suelta_el_momo`, `retorna_el_pack`, `regresar`, `retornar`.
* **Cierre de función:** `fin_de_la_funcion`, `fin_del_momo`.
* Cada llamada a una función genera un **ámbito léxico local (scope)** independiente en la Tabla de Símbolos, protegiendo las variables locales de colisiones con el entorno global.

---

## 6. Procesamiento de Datos y Tuberías (`|:v>`)

Para el análisis de datos masivos, MomoLang utiliza el modelo de tubería con el operador `|:v>` (o `|>`).

```momo
# 1. Cargar datos
ventas = pasa_el_pack "datos/ventas_prueba.csv" xd

# 2. Filtrar filas y calcular columna con álgebra vectorial
ventas_procesadas = ventas 
    |:v> but_te_enteras_que unidades > 2
    |:v> el_futuro_es_hoy_oiste_viejo subtotal = unidades * precio xd

# 3. Agrupamiento por ciudad con métricas estadísticas
resumen = ventas_procesadas 
    |:v> juntar_a_la_grasa_por [ciudad] calcular [
        suma(subtotal) como total_ciudad,
        promedio(subtotal) como promedio_ciudad,
        el_mas_pro(subtotal) como max_venta,
        contar_papus(unidades) como cant_transacciones
    ]
    |:v> ordenar_a_los_papus total_ciudad de_arriba_a_abajo xd

# 4. Exportar a CSV
subir_al_grupo resumen en "salidas/reporte_ventas.csv" xd
```

### Funciones Estadísticas Disponibles:
| Función en MomoLang | ¿Qué calcula? |
| :--- | :--- |
| `suma(columna)` | Suma de valores del grupo. |
| `promedio(columna)` / `media(columna)` | Promedio aritmético. |
| `mediana(columna)` | Valor central ordenado. |
| `el_mas_pro(columna)` / `maximo(columna)` | Valor máximo. |
| `el_mas_manco(columna)` / `minimo(columna)` | Valor mínimo. |
| `desviacion_pro(columna)` | Desviación estándar. |
| `contar_papus(columna)` | Cantidad de registros en el grupo. |

---

## 7. Ejecución de Programas

A partir de la Fase 2, el comando ejecuta los programas **directamente** (sin carteles de validación sintáctica de la Fase 1):

```bash
python3 ejecutar_dsl.py ejemplos/programa_control_funciones.xd
```

O utilizando los atajos del `Makefile`:

```bash
make run-control         # Demuestra asignación, condicionales, ciclos y funciones
make run-completo        # Pipeline completo combinando funciones y datos CSV
make run-ventas          # Análisis de ventas comerciales
make run-empleados       # Análisis de nómina por departamento
make run-estudiantes     # Rendimiento académico y notas
make run-error-semantico # Detección diagnóstica de errores semánticos
```

Si deseas inspeccionar el árbol sintáctico jerárquico o validar la sintaxis, puedes agregar la bandera `--arbol` o `--validar`:

```bash
python3 ejecutar_dsl.py ejemplos/programa_control_funciones.xd --arbol
```
