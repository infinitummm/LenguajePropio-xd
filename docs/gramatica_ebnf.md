# Especificación Formal de la Gramática en Notación EBNF
## Lenguaje de Dominio Específico: MomoLang XD (`.xd`)

**Asignatura:** Lenguajes de Programación y Transducción  
**Universidad Sergio Arboleda (2026-2)**

---

A continuación se presenta la especificación formal de la sintaxis del lenguaje **MomoLang XD** utilizando la notación **EBNF** (*Extended Backus-Naur Form*), correspondiente a la gramática implementada en ANTLR4 (`LenguajeMomoXD.g4`).

```ebnf
(* ========================================================================= *)
(* REGLAS SINTÁCTICAS (PARSER)                                              *)
(* ========================================================================= *)

programa            = { sentencia } EOF ;

sentencia           = ( asignacion
                      | instruccion_imprimir
                      | instruccion_guardado
                      | instruccion_visualizacion
                      | instruccion_si ) XD ;

asignacion          = IDENTIFICADOR "=" expresion_pipeline ;

expresion_pipeline  = expresion_base { OPERADOR_PIPE operacion_pipeline } ;

expresion_base      = instruccion_carga
                    | IDENTIFICADOR
                    | LITERAL_CADENA
                    | LITERAL_NUMERO ;

instruccion_carga   = PALABRA_CARGA LITERAL_CADENA [ "separador" LITERAL_CADENA ] ;

instruccion_imprimir= "when haces" ( expresion_aritmetica | LITERAL_CADENA | IDENTIFICADOR ) ;

instruccion_guardado= PALABRA_GUARDAR IDENTIFICADOR "en" LITERAL_CADENA ;

operacion_pipeline  = op_seleccionar
                    | op_filtrar
                    | op_ordenar
                    | op_crear_columna
                    | op_agrupar
                    | op_resumir ;

op_seleccionar      = PALABRA_SELECCIONAR lista_identificadores ;

op_filtrar          = PALABRA_FILTRAR expresion_booleana ;

op_ordenar          = PALABRA_ORDENAR IDENTIFICADOR [ MODIFICADOR_ORDEN ] ;

op_crear_columna    = PALABRA_CREAR_COLUMNA IDENTIFICADOR "=" expresion_aritmetica ;

op_agrupar          = PALABRA_AGRUPAR lista_identificadores ;

op_resumir          = PALABRA_RESUMIR lista_agregaciones ;

lista_agregaciones  = agregacion { "," agregacion } ;

agregacion          = IDENTIFICADOR "=" FUNCION_AGG "(" [ IDENTIFICADOR ] ")" ;

instruccion_visualizacion = TIPO_GRAFICO IDENTIFICADOR [ opciones_grafico ] ;

opciones_grafico    = [ "titulo" LITERAL_CADENA ]
                      [ "eje_x" LITERAL_CADENA ]
                      [ "eje_y" LITERAL_CADENA ]
                      [ "guardar" LITERAL_CADENA ] ;

instruccion_si      = "si el papu" expresion_booleana "entonces" bloque
                      [ "sino callese señora" bloque ] "fin del momo" ;

bloque              = { sentencia } ;

expresion_booleana  = expresion_aritmetica OPERADOR_RELACIONAL expresion_aritmetica ;

expresion_aritmetica= termino { ( "+" | "-" ) termino } ;

termino             = factor { ( "*" | "/" | "%" | "^" ) factor } ;

factor              = "(" expresion_aritmetica ")"
                    | IDENTIFICADOR
                    | LITERAL_NUMERO
                    | LITERAL_CADENA ;

lista_identificadores = "[" IDENTIFICADOR { "," IDENTIFICADOR } "]"
                      | IDENTIFICADOR ;


(* ========================================================================= *)
(* REGLAS LÉXICAS (TERMINALES / TOKENS)                                      *)
(* ========================================================================= *)

XD                  = "xd" | "XD" | "xD" ;
OPERADOR_PIPE       = "|:v>" | "|>" ;

PALABRA_CARGA       = "pasa_el_pack" | "pasa el pack"
                    | "pasa_el_zelda" | "pasa el zelda"
                    | "robar_momo" | "robar momo" ;

PALABRA_GUARDAR     = "subir_al_grupo" | "subir al grupo"
                    | "guardar_momo" | "guardar momo" ;

PALABRA_SELECCIONAR = "escojo_a" | "escojo a"
                    | "escojo_a_los_papus" | "escojo a los papus"
                    | "seleccionar_momos" | "seleccionar momos" ;

PALABRA_FILTRAR     = "but_te_enteras_que" | "but te enteras que"
                    | "but_ella_no_te_ama" | "but ella no te ama"
                    | "no_lo_se_rick" | "no lo se rick"
                    | "filtrar_grasosos" | "filtrar grasosos" ;

PALABRA_ORDENAR     = "ordenar_a_los_papus" | "ordenar a los papus"
                    | "ordenar_momos" | "ordenar momos" ;

MODIFICADOR_ORDEN   = "de_arriba_a_abajo" | "de arriba a abajo"
                    | "de_abajo_a_arriba" | "de abajo a arriba"
                    | "ascendente" | "descendente" ;

PALABRA_CREAR_COLUMNA = "el_futuro_es_hoy_oiste_viejo" | "el futuro es hoy oiste viejo"
                      | "metanle_sabor_a" | "metanle sabor a"
                      | "crear_momo" | "crear momo" ;

PALABRA_AGRUPAR     = "juntar_a_la_grasa_por" | "juntar a la grasa por"
                    | "agrupar_a_los_papus_por" | "agrupar a los papus por" ;

PALABRA_RESUMIR     = "sacar_cuentas" | "sacar cuentas"
                    | "resumir_momos" | "resumir momos" ;

FUNCION_AGG         = "suma" | "sumar_momos"
                    | "promedio" | "media" | "mediana"
                    | "el_mas_pro" | "maximo"
                    | "el_mas_manco" | "minimo"
                    | "contar_papus" | "contar" | "conteo"
                    | "desviacion_pro" | "desviacion" ;

TIPO_GRAFICO        = "graficar_momos_en_barras" | "graficar momos en barras"
                    | "graficar_momos_en_lineas" | "graficar momos en lineas"
                    | "graficar_momos_en_histograma" | "graficar momos en histograma"
                    | "graficar_momos_en_dispersion" | "graficar momos en dispersion"
                    | "graficar_momos_en_cajas" | "graficar momos en cajas" ;

OPERADOR_RELACIONAL = ">=" | "<=" | "==" | "!=" | ">" | "<" ;

IDENTIFICADOR       = ( LETRA | "_" ) { LETRA | DIGITO | "_" } ;
LITERAL_NUMERO      = DIGITO { DIGITO } [ "." DIGITO { DIGITO } ] ;
LITERAL_CADENA      = '"' { CUALQUIER_CARACTER_EXCEPTO_COMILLAS } '"'
                    | "'" { CUALQUIER_CARACTER_EXCEPTO_COMILLAS } "'" ;

COMENTARIO          = ( "#" | "//" ) { CUALQUIER_CARACTER_EXCEPTO_SALTO } ;
ESPACIO_BLANCO      = { " " | "\t" | "\r" | "\n" } ;
```
