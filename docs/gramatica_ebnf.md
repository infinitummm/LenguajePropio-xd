# Especificación de la Gramática en Notación EBNF

Definición formal en EBNF (Extended Backus-Naur Form) para el DSL **LenguajeDatos**.

```ebnf
programa            = { sentencia } ;

sentencia           = asignacion
                    | instruccion_visualizacion
                    | instruccion_guardado ;

asignacion          = IDENTIFICADOR "=" expresion_pipeline ;

expresion_pipeline  = expresion_base { "|>" operacion_pipeline } ;

expresion_base      = instruccion_carga
                    | IDENTIFICADOR
                    | LITERAL_CADENA
                    | LITERAL_NUMERO ;

instruccion_carga   = "cargar_csv_xd" LITERAL_CADENA [ separador_opc ] ;
instruccion_guardado= "guardar_csv_xd" IDENTIFICADOR LITERAL_CADENA ;

operacion_pipeline  = op_seleccionar
                    | op_filtrar
                    | op_ordenar
                    | op_crear_columna
                    | op_agrupar
                    | op_resumir ;

op_seleccionar      = "seleccionar_xd" lista_identificadores ;
op_filtrar          = "filtrar_xd" expresion_booleana ;
op_ordenar          = "ordenar_por_xd" IDENTIFICADOR [ "ascendente" | "descendente" ] ;
op_crear_columna    = "crear_columna_xd" IDENTIFICADOR "=" expresion_aritmetica ;
op_agrupar          = "agrupar_por_xd" lista_identificadores ;
op_resumir          = "resumir_xd" lista_agregaciones ;

lista_agregaciones  = agregacion { "," agregacion } ;
agregacion          = IDENTIFICADOR "=" FUNCION_AGG "(" IDENTIFICADOR ")" ;

instruccion_visualizacion = TIPO_GRAFICO IDENTIFICADOR [ opciones_grafico ] ;

TIPO_GRAFICO        = "graficar_barras_xd"
                    | "graficar_lineas_xd"
                    | "graficar_histograma_xd"
                    | "graficar_dispersion_xd"
                    | "graficar_cajas_xd" ;

FUNCION_AGG         = "suma" | "promedio" | "mediana" | "minimo" | "maximo" | "conteo" ;

expresion_booleana  = expresion_aritmetica OPERADOR_RELACIONAL expresion_aritmetica ;
expresion_aritmetica= termino { ( "+" | "-" ) termino } ;
termino             = factor { ( "*" | "/" ) factor } ;
factor              = IDENTIFICADOR | LITERAL_NUMERO | "(" expresion_aritmetica ")" ;

lista_identificadores = "[" IDENTIFICADOR { "," IDENTIFICADOR } "]" ;

OPERADOR_RELACIONAL = ">" | "<" | ">=" | "<=" | "==" | "!=" ;
LITERAL_CADENA      = '"' { CHARACTER } '"' ;
LITERAL_NUMERO      = [ "-" ] DIGIT { DIGIT } [ "." DIGIT { DIGIT } ] ;
IDENTIFICADOR       = LETTER { LETTER | DIGIT | "_" } ;
```
