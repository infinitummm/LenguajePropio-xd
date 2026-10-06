# Manual de Usuario: MomoLang XD (`.xd`)

---

## 1. Reglas Fundamentales del Lenguaje

1. **Terminador Obligatorio:** Toda sentencia debe finalizar obligatoriamente con `xd` (o `XD` / `xD`).
2. **Sensibilidad a Mayúsculas:** Las palabras reservadas y nombres de funciones están normalizados en minúsculas.
3. **Flujo de Tubería:** Las transformaciones de datos se encadenan de izquierda a derecha usando el operador `|:v>` (o `|>`).
4. **Comentarios:** Inician con `#` o `//` y se extienden hasta el final de la línea.
5. **Tipos de Datos Soportados:**
   - **Numérico:** Enteros (`10`) y flotantes (`3.14`).
   - **Cadena:** Texto delimitado por comillas dobles (`"texto"`) o simples (`'texto'`).
   - **Booleano:** Valores de verdad (`True` / `False`) y máscaras relacionales.
   - **Tabla:** Estructuras tabulares bidimensionales cargadas desde CSV o producidas por transformaciones.
   - **Vector:** Series de datos numéricos unidimensionales sobre las que se realizan operaciones aritméticas.
   - **Función:** Subrutinas creadas por el usuario con parámetros y retorno.

---

## 2. Catálogo Completo de Instrucciones y Nombres Disponibles

### 2.1 Entrada, Salida y Almacenamiento

| Instrucción / Nombres Disponibles | Parámetros / Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `when haces`, `when_haces` | `expresion` | Imprime en pantalla una cadena, variable o expresión. | `when haces "Hola mundo" xd` |
| `pasa_el_pack`, `pasa_el_zelda`, `robar_momo` | `"ruta"` (`separador "sep"`)? | Carga un archivo CSV en memoria como una tabla. | `datos = pasa_el_pack "datos.csv" xd` |
| `subir_al_grupo`, `guardar_momo` | `tabla en "ruta"` | Exporta una tabla de datos a formato CSV. | `subir_al_grupo datos en "salida.csv" xd` |

---

### 2.2 Variables y Asignación

| Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- |
| `id = expresion` | Asigna un valor numérico, texto, booleano, tabla o resultado a un identificador. | `precio = 50000 xd`<br>`total = precio * 1.19 xd` |

---

### 2.3 Operaciones en Tubería de Datos (`|:v>`)

| Operación / Nombres Disponibles | Sintaxis | Descripción | Ejemplo |
| :--- | :--- | :--- | :--- |
| `escojo_a`, `escojo_a_los_papus`, `seleccionar_momos` | `[col1, col2, ...]` | Selecciona un subconjunto de columnas de la tabla. | `\|:v> escojo_a [ciudad, total]` |
| `but_te_enteras_que`, `but_ella_no_te_ama`, `no_lo_se_rick`, `filtrar_grasosos` | `condicion` | Filtra las filas que cumplan la condición booleana. | `\|:v> but_te_enteras_que unidades > 10` |
| `el_futuro_es_hoy_oiste_viejo`, `metanle_sabor_a`, `crear_momo` | `col_nueva = expr` | Crea o modifica una columna aplicando una fórmula aritmética vectorial. | `\|:v> el_futuro_es_hoy_oiste_viejo total = cant * precio` |
| `ordenar_a_los_papus`, `ordenar_momos` | `columna sentido?` | Ordena los registros por una columna específica. | `\|:v> ordenar_a_los_papus total de_arriba_a_abajo` |
| Sentidos de ordenamiento: | `de_arriba_a_abajo`, `descendente`<br>`de_abajo_a_arriba`, `ascendente` | Define orden descendente (mayor a menor) o ascendente (menor a mayor). | `\|:v> ordenar_momos precio ascendente` |
| `juntar_a_la_grasa_por`, `agrupar_a_los_papus_por` | `[cols] (calcular [...])?` | Agrupa los datos por una o más columnas. Permite calcular métricas de forma directa o encadenada. | `\|:v> juntar_a_la_grasa_por [ciudad]` |
| `sacar_cuentas`, `resumir_momos`, `calcular` | `[metrica1, metrica2]` | Calcula métricas estadísticas sobre una tabla agrupada. | `\|:v> sacar_cuentas total = suma(venta)` |
| `como` | `funcion(col) como alias` | Define el nombre resultante de una columna calculada en el resumen. | `calcular [ suma(subtotal) como total ]` |

---

### 2.4 Funciones Estadísticas y Matemáticas

| Función / Nombres Disponibles | Argumentos | Descripción |
| :--- | :--- | :--- |
| `suma`, `sumar`, `sumar_papus`, `sumar_momos` | `(columna)` o `(a, b)` | Calcula la suma total de una columna o de dos valores. |
| `promedio`, `media` | `(columna)` | Calcula la media aritmética de los valores de la columna. |
| `mediana` | `(columna)` | Obtiene el valor central ordenado de una columna. |
| `el_mas_pro`, `maximo` | `(columna)` | Obtiene el valor máximo de la columna. |
| `el_mas_manco`, `minimo` | `(columna)` | Obtiene el valor mínimo de la columna. |
| `desviacion_pro`, `desviacion` | `(columna)` | Calcula la desviación estándar de la columna. |
| `contar_papus`, `conteo`, `contar` | `()` o `(columna)` | Cuenta la cantidad total de registros o filas. |
| `multiplicacion`, `multiplicar`, `multiplicar_papus`, `multiplicar_momos` | `(a, b)` | Multiplica dos escalares o columnas vectoriales. |
| `resta`, `restar`, `restar_papus`, `restar_momos` | `(a, b)` | Resta dos escalares o columnas vectoriales. |
| `division`, `dividir`, `dividir_papus`, `dividir_momos` | `(a, b)` | Divide dos escalares o columnas vectoriales. |

---

### 2.5 Control de Flujo: Condicionales

| Estructura / Nombres Disponibles | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Inicio:** `si_el_papu`, `si_pasa_esto`, `si` | `si_el_papu condicion entonces` | Evalúa una condición booleana para ejecutar un bloque. |
| **Entonces:** `entonces`, `haz_esto` |  | Delimita el inicio del bloque afirmativo. |
| **Sino:** `sino_callese_senora`, `pero_si_no`, `sino` |  | Delimita el bloque alternativo opcional. |
| **Fin:** `fin_del_momo`, `fin_del_si`, `fin_si` | `fin_del_momo xd` | Cierra la estructura condicional. |

**Ejemplo:**
```momo
si_el_papu saldo > 200000 entonces
    when haces "Saldo disponible" xd
sino_callese_senora
    when haces "Saldo insuficiente" xd
fin_del_momo xd
```

---

### 2.6 Control de Flujo: Ciclos

#### Bucle Mientras (`while`)
| Instrucción / Nombres Disponibles | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Inicio:** `mientras_el_papu`, `mientras_tanto`, `mientras` | `mientras_el_papu condicion haz_esto` | Ejecuta un bloque de sentencias mientras la condición sea verdadera. |
| **Cuerpo:** `haz_esto`, `entonces` |  | Delimita el inicio del cuerpo del ciclo. |
| **Fin:** `fin_del_bucle`, `fin_bucle`, `fin_del_momo` | `fin_del_bucle xd` | Cierra la estructura del bucle mientras. |

**Ejemplo:**
```momo
contador = 1 xd
mientras_el_papu contador <= 3 haz_esto
    when haces contador xd
    contador = contador + 1 xd
fin_del_bucle xd
```

#### Bucle Para (`for` sobre rango)
| Instrucción / Nombres Disponibles | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Inicio:** `para_cada_papu`, `por_cada_uno`, `para` | `para_cada_papu id desde ini hasta fin haz_esto` | Itera la variable sobre el rango numérico inclusivo. |
| **Límites:** `desde`, `hasta` |  | Establece el valor inicial y final de la variable de control. |
| **Fin:** `fin_del_bucle`, `fin_bucle`, `fin_del_momo` | `fin_del_bucle xd` | Cierra la estructura del bucle para. |

**Ejemplo:**
```momo
para_cada_papu i desde 1 hasta 5 haz_esto
    when haces i * 2 xd
fin_del_bucle xd
```

---

### 2.7 Funciones de Usuario

| Instrucción / Nombres Disponibles | Sintaxis | Descripción |
| :--- | :--- | :--- |
| **Declaración:** `momo_funcion`, `funcion_papu`, `rutina_momo`, `funcion` | `momo_funcion nombre(p1, p2, ...)` | Declara una función con parámetros en un ámbito local aislado. |
| **Retorno:** `suelta_el_momo`, `retorna_el_pack`, `regresar`, `retornar` | `suelta_el_momo valor xd` | Retorna un valor desde la función y finaliza su ejecución. |
| **Fin:** `fin_de_la_funcion`, `fin_funcion`, `fin_del_momo` | `fin_de_la_funcion xd` | Cierra la declaración de la función. |

**Ejemplo:**
```momo
momo_funcion calcular_iva(base, tasa)
    impuesto = base * tasa / 100 xd
    suelta_el_momo base + impuesto xd
fin_de_la_funcion xd

total = calcular_iva(100000, 19) xd
when haces total xd
```

---

### 2.8 Operadores Relacionales, Lógicos y Aritméticos

* **Relacionales:** `==` (igual), `!=` (diferente), `>` (mayor), `<` (menor), `>=` (mayor o igual), `<=` (menor o igual).
* **Lógicos:**
  * Conjunción: `y_ademas`, `&&`, `and`
  * Disyunción: `o_bien`, `||`, `or`
  * Negación: `no_es_cierto`, `!`, `not`
* **Aritméticos:** `+` (suma/concatenación), `-` (resta), `*` (multiplicación), `/` (división), `%` (módulo), `^` (potencia).

---

### 2.9 Instrucciones de Visualización (Sintaxis Reconocida)

| Instrucción | Parámetros Opcionales | Descripción |
| :--- | :--- | :--- |
| `graficar_momos_en_barras` | `titulo "t"`, `eje_x "x"`, `eje_y "y"`, `guardar "ruta"` | Gráfico de barras sobre una tabla. |
| `graficar_momos_en_lineas` | `titulo "t"`, `eje_x "x"`, `eje_y "y"`, `guardar "ruta"` | Gráfico de líneas temporales. |
| `graficar_momos_en_histograma` | `titulo "t"`, `eje_x "x"`, `eje_y "y"`, `guardar "ruta"` | Gráfico de distribución de frecuencias. |
| `graficar_momos_en_dispersion` | `titulo "t"`, `eje_x "x"`, `eje_y "y"`, `guardar "ruta"` | Gráfico de dispersión bidimensional. |
| `graficar_momos_en_cajas` | `titulo "t"`, `eje_x "x"`, `eje_y "y"`, `guardar "ruta"` | Diagrama de cajas y bigotes. |
