grammar LenguajeDatos;

// --- REGLAS SINTÁCTICAS (PARSER) ---

programa
    : sentencia* EOF
    ;

sentencia
    : asignacion
    | instruccionGuardado
    | instruccionVisualizacion
    ;

asignacion
    : ID '=' expresionPipeline
    ;

expresionPipeline
    : expresionBase (PIPE operacionPipeline)*
    ;

expresionBase
    : instruccionCarga
    | ID
    | CADENA
    | NUMERO
    ;

instruccionCarga
    : CARGAR_CSV_XD CADENA (SEPARADOR CADENA)?
    ;

instruccionGuardado
    : GUARDAR_CSV_XD ID CADENA
    ;

operacionPipeline
    : operacionSeleccionar
    | operacionFiltrar
    | operacionOrdenar
    | operacionCrearColumna
    | operacionAgrupar
    | operacionResumir
    ;

operacionSeleccionar
    : SELECCIONAR_XD listaIDs
    ;

operacionFiltrar
    : FILTRAR_XD expresionBooleana
    ;

operacionOrdenar
    : ORDENAR_POR_XD ID (ASCENDENTE | DESCENDENTE)?
    ;

operacionCrearColumna
    : CREAR_COLUMNA_XD ID '=' expresionAritmetica
    ;

operacionAgrupar
    : AGRUPAR_POR_XD listaIDs
    ;

operacionResumir
    : RESUMIR_XD listaAgregaciones
    ;

listaAgregaciones
    : agregacion (COMA agregacion)*
    ;

agregacion
    : ID '=' FUNCION_AGG PAREN_IZQ ID PAREN_DER
    | ID '=' FUNCION_AGG PAREN_IZQ PAREN_DER
    ;

instruccionVisualizacion
    : tipoGrafico ID (TITULO CADENA)? (EJE_X CADENA)? (EJE_Y CADENA)? (GUARDAR CADENA)?
    ;

tipoGrafico
    : GRAFICAR_BARRAS_XD
    | GRAFICAR_LINEAS_XD
    | GRAFICAR_HISTOGRAMA_XD
    | GRAFICAR_DISPERSION_XD
    | GRAFICAR_CAJAS_XD
    ;

expresionBooleana
    : expresionAritmetica opRelacional expresionAritmetica
    ;

opRelacional
    : MAYOR_IGUAL | MENOR_IGUAL | IGUAL_IGUAL | DIFERENTE | MAYOR | MENOR
    ;

expresionAritmetica
    : termino ((MAS | MENOS) termino)*
    ;

termino
    : factor ((MULT | DIV | MOD) factor)*
    ;

factor
    : PAREN_IZQ expresionAritmetica PAREN_DER
    | ID
    | NUMERO
    ;

listaIDs
    : CORCH_IZQ ID (COMA ID)* CORCH_DER
    | ID
    ;

// --- REGLAS LÉXICAS (LEXER) ---

CARGAR_CSV_XD          : 'cargar_csv_xd' ;
GUARDAR_CSV_XD         : 'guardar_csv_xd' ;
SELECCIONAR_XD         : 'seleccionar_xd' ;
FILTRAR_XD             : 'filtrar_xd' ;
ORDENAR_POR_XD         : 'ordenar_por_xd' ;
CREAR_COLUMNA_XD       : 'crear_columna_xd' ;
AGRUPAR_POR_XD         : 'agrupar_por_xd' ;
RESUMIR_XD             : 'resumir_xd' ;

GRAFICAR_BARRAS_XD     : 'graficar_barras_xd' ;
GRAFICAR_LINEAS_XD     : 'graficar_lineas_xd' ;
GRAFICAR_HISTOGRAMA_XD : 'graficar_histograma_xd' ;
GRAFICAR_DISPERSION_XD : 'graficar_dispersion_xd' ;
GRAFICAR_CAJAS_XD      : 'graficar_cajas_xd' ;

FUNCION_AGG            : 'suma' | 'promedio' | 'mediana' | 'minimo' | 'maximo' | 'conteo' ;

ASCENDENTE             : 'ascendente' ;
DESCENDENTE            : 'descendente' ;
SEPARADOR              : 'separador' ;
TITULO                 : 'titulo' ;
EJE_X                  : 'eje_x' ;
EJE_Y                  : 'eje_y' ;
GUARDAR                : 'guardar' ;

PIPE                   : '|>' ;
COMA                   : ',' ;
DOS_PUNTOS             : ':' ;
PAREN_IZQ              : '(' ;
PAREN_DER              : ')' ;
CORCH_IZQ              : '[' ;
CORCH_DER              : ']' ;

MAS                    : '+' ;
MENOS                  : '-' ;
MULT                   : '*' ;
DIV                    : '/' ;
MOD                    : '%' ;

MAYOR_IGUAL            : '>=' ;
MENOR_IGUAL            : '<=' ;
IGUAL_IGUAL            : '==' ;
DIFERENTE              : '!=' ;
MAYOR                  : '>' ;
MENOR                  : '<' ;

ID                     : [a-zA-Z_] [a-zA-Z0-9_]* ;
NUMERO                 : [0-9]+ ('.' [0-9]+)? ;
CADENA                 : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

COMENTARIO             : '#' ~[\r\n]* -> skip ;
WS                     : [ \t\r\n]+ -> skip ;
