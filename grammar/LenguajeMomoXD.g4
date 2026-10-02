grammar LenguajeMomoXD;

// ==========================================
// --- REGLAS SINTÁCTICAS (PARSER) ---
// ==========================================

programa
    : sentencia* EOF
    ;

sentencia
    : asignacion XD
    | instruccionImprimir XD
    | instruccionGuardado XD
    | instruccionVisualizacion XD
    | instruccionSi XD
    | instruccionMientras XD
    | instruccionPara XD
    | definicionFuncion XD
    | instruccionRetorno XD
    | llamadaFuncion XD
    | expresionAritmetica XD
    ;

asignacion
    : ID '=' expresionPipeline
    ;

expresionPipeline
    : expresionBase (PIPE operacionPipeline)*
    ;

expresionBase
    : instruccionCarga
    | expresionAritmetica
    ;

instruccionCarga
    : (PASA_EL_PACK | PASA_EL_ZELDA | ROBAR_MOMO) CADENA (SEPARADOR CADENA)?
    ;

instruccionImprimir
    : WHEN_HACES (expresionAritmetica | CADENA | ID)
    ;

instruccionGuardado
    : (SUBIR_AL_GRUPO | GUARDAR_MOMO) ID EN CADENA
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
    : (ESCOJO_A | ESCOJO_A_LOS_PAPUS | SELECCIONAR_MOMOS) listaIDs
    ;

operacionFiltrar
    : (BUT_TE_ENTERAS_QUE | BUT_ELLA_NO_TE_AMA | NO_LO_SE_RICK | FILTRAR_GRASOSOS) expresionBooleana
    ;

operacionOrdenar
    : (ORDENAR_A_LOS_PAPUS | ORDENAR_MOMOS) ID (DE_ARRIBA_A_ABAJO | DE_ABAJO_A_ARRIBA | ASCENDENTE | DESCENDENTE)?
    ;

operacionCrearColumna
    : (EL_FUTURO_ES_HOY_OISTE_VIEJO | METANLE_SABOR_A | CREAR_MOMO) ID '=' expresionAritmetica
    ;

operacionAgrupar
    : (JUNTAR_A_LA_GRASA_POR | AGRUPAR_A_LOS_PAPUS_POR) listaIDs ((CALCULAR | SACAR_CUENTAS) CORCH_IZQ? listaAgregaciones CORCH_DER?)?
    ;

operacionResumir
    : (SACAR_CUENTAS | RESUMIR_MOMOS | CALCULAR) CORCH_IZQ? listaAgregaciones CORCH_DER?
    ;

listaAgregaciones
    : agregacion (COMA agregacion)*
    ;

agregacion
    : ID '=' funcionAgg PAREN_IZQ (ID | funcionAgg)? PAREN_DER
    | funcionAgg PAREN_IZQ (ID | funcionAgg)? PAREN_DER (COMO ID)?
    ;

funcionAgg
    : SUMA
    | MULTIPLICACION
    | RESTA
    | DIVISION
    | PROMEDIO
    | MEDIA
    | MEDIANA
    | EL_MAS_PRO
    | MAXIMO
    | EL_MAS_MANCO
    | MINIMO
    | CONTAR_PAPUS
    | CONTEO
    | DESVIACION_PRO
    ;

instruccionVisualizacion
    : tipoGrafico ID (TITULO CADENA)? (EJE_X CADENA)? (EJE_Y CADENA)? (GUARDAR CADENA)?
    ;

tipoGrafico
    : GRAFICAR_MOMOS_EN_BARRAS
    | GRAFICAR_MOMOS_EN_LINEAS
    | GRAFICAR_MOMOS_EN_HISTOGRAMA
    | GRAFICAR_MOMOS_EN_DISPERSION
    | GRAFICAR_MOMOS_EN_CAJAS
    ;

// --- CONDICIONALES ---
instruccionSi
    : (SI_EL_PAPU | SI_PASA_ESTO | SI) expresionBooleana (ENTONCES | HAZ_ESTO)? bloque ((SINO_CALLESE_SENORA | PERO_SI_NO | SINO) bloque)? (FIN_DEL_MOMO | FIN_DEL_SI)
    ;

// --- CICLOS ---
instruccionMientras
    : (MIENTRAS_EL_PAPU | MIENTRAS_TANTO | MIENTRAS) expresionBooleana (HAZ_ESTO | ENTONCES)? bloque (FIN_DEL_BUCLE | FIN_DEL_MOMO)
    ;

instruccionPara
    : (PARA_CADA_PAPU | POR_CADA_UNO | PARA) ID DESDE expresionAritmetica HASTA expresionAritmetica (HAZ_ESTO | ENTONCES)? bloque (FIN_DEL_BUCLE | FIN_DEL_MOMO)
    ;

// --- FUNCIONES ---
definicionFuncion
    : (MOMO_FUNCION | FUNCION_PAPU | RUTINA_MOMO | FUNCION) ID PAREN_IZQ listaParametros? PAREN_DER bloque (FIN_DE_LA_FUNCION | FIN_DEL_MOMO)
    ;

listaParametros
    : parametro (COMA parametro)*
    ;

parametro
    : ID
    | funcionAgg
    ;

instruccionRetorno
    : (SUELTA_EL_MOMO | RETORNA_EL_PACK | REGRESAR | RETORNAR) expresionAritmetica?
    ;

bloque
    : sentencia+
    ;

// --- EXPRESIONES BOOLEANAS Y LÓGICAS ---
expresionBooleana
    : expresionLogicaOr
    ;

expresionLogicaOr
    : expresionLogicaAnd ((O_BIEN | OR_OP) expresionLogicaAnd)*
    ;

expresionLogicaAnd
    : expresionLogicaNot ((Y_ADEMAS | AND_OP) expresionLogicaNot)*
    ;

expresionLogicaNot
    : (NO_ES_CIERTO | NOT_OP)? expresionRelacional
    ;

expresionRelacional
    : PAREN_IZQ expresionBooleana PAREN_DER
    | expresionAritmetica opRelacional expresionAritmetica
    | expresionAritmetica
    ;

opRelacional
    : MAYOR_IGUAL | MENOR_IGUAL | IGUAL_IGUAL | DIFERENTE | MAYOR | MENOR
    ;

// --- EXPRESIONES ARITMÉTICAS ---
expresionAritmetica
    : termino ((MAS | MENOS) termino)*
    ;

termino
    : factor ((MULT | DIV | MOD | POT) factor)*
    ;

factor
    : PAREN_IZQ expresionAritmetica PAREN_DER
    | llamadaFuncion
    | ID
    | funcionAgg
    | NUMERO
    | CADENA
    ;

llamadaFuncion
    : funcionNombre PAREN_IZQ listaArgumentos? PAREN_DER
    ;

funcionNombre
    : ID
    | funcionAgg
    ;

listaArgumentos
    : expresionAritmetica (COMA expresionAritmetica)*
    ;

listaIDs
    : CORCH_IZQ idOAgg (COMA idOAgg)* CORCH_DER
    | idOAgg
    ;

idOAgg
    : ID
    | funcionAgg
    ;

// ==========================================
// --- REGLAS LÉXICAS (LEXER) ---
// ==========================================

XD                         : 'xd' | 'XD' | 'xD' ;
PIPE                       : '|:v>' | '|>' ;

WHEN_HACES                 : 'when_haces' | 'when' [ \t]+ 'haces' ;
PASA_EL_PACK               : 'pasa_el_pack' | 'pasa' [ \t]+ 'el' [ \t]+ 'pack' ;
PASA_EL_ZELDA              : 'pasa_el_zelda' | 'pasa' [ \t]+ 'el' [ \t]+ 'zelda' ;
ROBAR_MOMO                 : 'robar_momo' | 'robar' [ \t]+ 'momo' ;
SUBIR_AL_GRUPO             : 'subir_al_grupo' | 'subir' [ \t]+ 'al' [ \t]+ 'grupo' ;
GUARDAR_MOMO               : 'guardar_momo' | 'guardar' [ \t]+ 'momo' ;

ESCOJO_A                   : 'escojo_a' | 'escojo' [ \t]+ 'a' ;
ESCOJO_A_LOS_PAPUS         : 'escojo_a_los_papus' | 'escojo' [ \t]+ 'a' [ \t]+ 'los' [ \t]+ 'papus' ;
SELECCIONAR_MOMOS          : 'seleccionar_momos' | 'seleccionar' [ \t]+ 'momos' ;

BUT_TE_ENTERAS_QUE         : 'but_te_enteras_que' | 'but' [ \t]+ 'te' [ \t]+ 'enteras' [ \t]+ 'que' ;
BUT_ELLA_NO_TE_AMA         : 'but_ella_no_te_ama' | 'but' [ \t]+ 'ella' [ \t]+ 'no' [ \t]+ 'te' [ \t]+ 'ama' ;
NO_LO_SE_RICK              : 'no_lo_se_rick' | 'no' [ \t]+ 'lo' [ \t]+ 'se' [ \t]+ 'rick' ;
FILTRAR_GRASOSOS           : 'filtrar_grasosos' | 'filtrar' [ \t]+ 'grasosos' ;

ORDENAR_A_LOS_PAPUS        : 'ordenar_a_los_papus' | 'ordenar' [ \t]+ 'a' [ \t]+ 'los' [ \t]+ 'papus' ;
ORDENAR_MOMOS              : 'ordenar_momos' | 'ordenar' [ \t]+ 'momos' ;
DE_ARRIBA_A_ABAJO          : 'de_arriba_a_abajo' | 'de' [ \t]+ 'arriba' [ \t]+ 'a' [ \t]+ 'abajo' ;
DE_ABAJO_A_ARRIBA          : 'de_abajo_a_arriba' | 'de' [ \t]+ 'abajo' [ \t]+ 'a' [ \t]+ 'arriba' ;
ASCENDENTE                 : 'ascendente' ;
DESCENDENTE                : 'descendente' ;

EL_FUTURO_ES_HOY_OISTE_VIEJO : 'el_futuro_es_hoy_oiste_viejo' | 'el' [ \t]+ 'futuro' [ \t]+ 'es' [ \t]+ 'hoy' [ \t]+ 'oiste' [ \t]+ 'viejo' ;
METANLE_SABOR_A            : 'metanle_sabor_a' | 'metanle' [ \t]+ 'sabor' [ \t]+ 'a' ;
CREAR_MOMO                 : 'crear_momo' | 'crear' [ \t]+ 'momo' ;

JUNTAR_A_LA_GRASA_POR      : 'juntar_a_la_grasa_por' | 'juntar' [ \t]+ 'a' [ \t]+ 'la' [ \t]+ 'grasa' [ \t]+ 'por' ;
AGRUPAR_A_LOS_PAPUS_POR    : 'agrupar_a_los_papus_por' | 'agrupar' [ \t]+ 'a' [ \t]+ 'los' [ \t]+ 'papus' [ \t]+ 'por' ;
SACAR_CUENTAS              : 'sacar_cuentas' | 'sacar' [ \t]+ 'cuentas' ;
RESUMIR_MOMOS              : 'resumir_momos' | 'resumir' [ \t]+ 'momos' ;
CALCULAR                   : 'calcular' ;
COMO                       : 'como' ;

SUMA                       : 'suma' | 'sumar_momos' | 'sumar_papus' | 'sumar' [ \t]+ 'papus' | 'sumar' ;
MULTIPLICACION             : 'multiplicacion' | 'multiplicar' | 'multiplicar_papus' | 'multiplicar_momos' ;
RESTA                      : 'resta' | 'restar' | 'restar_papus' | 'restar_momos' ;
DIVISION                   : 'division' | 'dividir' | 'dividir_papus' | 'dividir_momos' ;
PROMEDIO                   : 'promedio' ;
MEDIA                      : 'media' ;
MEDIANA                    : 'mediana' ;
EL_MAS_PRO                 : 'el_mas_pro' | 'el' [ \t]+ 'mas' [ \t]+ 'pro' ;
MAXIMO                     : 'maximo' ;
EL_MAS_MANCO               : 'el_mas_manco' | 'el' [ \t]+ 'mas' [ \t]+ 'manco' ;
MINIMO                     : 'minimo' ;
CONTAR_PAPUS               : 'contar_papus' | 'contar' [ \t]+ 'papus' | 'contar' ;
CONTEO                     : 'conteo' ;
DESVIACION_PRO             : 'desviacion_pro' | 'desviacion' ;

GRAFICAR_MOMOS_EN_BARRAS   : 'graficar_momos_en_barras' | 'graficar' [ \t]+ 'momos' [ \t]+ 'en' [ \t]+ 'barras' ;
GRAFICAR_MOMOS_EN_LINEAS   : 'graficar_momos_en_lineas' | 'graficar' [ \t]+ 'momos' [ \t]+ 'en' [ \t]+ 'lineas' ;
GRAFICAR_MOMOS_EN_HISTOGRAMA : 'graficar_momos_en_histograma' | 'graficar' [ \t]+ 'momos' [ \t]+ 'en' [ \t]+ 'histograma' ;
GRAFICAR_MOMOS_EN_DISPERSION : 'graficar_momos_en_dispersion' | 'graficar' [ \t]+ 'momos' [ \t]+ 'en' [ \t]+ 'dispersion' ;
GRAFICAR_MOMOS_EN_CAJAS    : 'graficar_momos_en_cajas' | 'graficar' [ \t]+ 'momos' [ \t]+ 'en' [ \t]+ 'cajas' ;

// Palabras reservadas de condicionales
SI_EL_PAPU                 : 'si_el_papu' | 'si' [ \t]+ 'el' [ \t]+ 'papu' ;
SI_PASA_ESTO               : 'si_pasa_esto' | 'si' [ \t]+ 'pasa' [ \t]+ 'esto' ;
SI                         : 'si' ;
ENTONCES                   : 'entonces' ;
HAZ_ESTO                   : 'haz_esto' | 'haz' [ \t]+ 'esto' ;
SINO_CALLESE_SENORA        : 'sino_callese_senora' | 'sino' [ \t]+ 'callese' [ \t]+ ('señora' | 'senora') ;
PERO_SI_NO                 : 'pero_si_no' | 'pero' [ \t]+ 'si' [ \t]+ 'no' ;
SINO                       : 'sino' ;
FIN_DEL_SI                 : 'fin_del_si' | 'fin' [ \t]+ 'del' [ \t]+ 'si' | 'fin_si' ;

// Palabras reservadas de ciclos
MIENTRAS_EL_PAPU           : 'mientras_el_papu' | 'mientras' [ \t]+ 'el' [ \t]+ 'papu' ;
MIENTRAS_TANTO             : 'mientras_tanto' | 'mientras' [ \t]+ 'tanto' ;
MIENTRAS                   : 'mientras' ;
FIN_DEL_BUCLE              : 'fin_del_bucle' | 'fin' [ \t]+ 'del' [ \t]+ 'bucle' | 'fin_bucle' ;

PARA_CADA_PAPU             : 'para_cada_papu' | 'para' [ \t]+ 'cada' [ \t]+ 'papu' ;
POR_CADA_UNO               : 'por_cada_uno' | 'por' [ \t]+ 'cada' [ \t]+ 'uno' ;
PARA                       : 'para' ;
DESDE                      : 'desde' ;
HASTA                      : 'hasta' ;

// Palabras reservadas de funciones
MOMO_FUNCION               : 'momo_funcion' | 'momo' [ \t]+ 'funcion' ;
FUNCION_PAPU               : 'funcion_papu' | 'funcion' [ \t]+ 'papu' ;
RUTINA_MOMO                : 'rutina_momo' | 'rutina' [ \t]+ 'momo' ;
FUNCION                    : 'funcion' ;
FIN_DE_LA_FUNCION          : 'fin_de_la_funcion' | 'fin' [ \t]+ 'de' [ \t]+ 'la' [ \t]+ 'funcion' | 'fin_funcion' ;

SUELTA_EL_MOMO             : 'suelta_el_momo' | 'suelta' [ \t]+ 'el' [ \t]+ 'momo' ;
RETORNA_EL_PACK            : 'retorna_el_pack' | 'retorna' [ \t]+ 'el' [ \t]+ 'pack' ;
REGRESAR                   : 'regresar' ;
RETORNAR                   : 'retornar' ;

FIN_DEL_MOMO               : 'fin_del_momo' | 'fin' [ \t]+ 'del' [ \t]+ 'momo' ;

// Operadores lógicos
Y_ADEMAS                   : 'y_ademas' | 'y' [ \t]+ 'ademas' ;
O_BIEN                     : 'o_bien' | 'o' [ \t]+ 'bien' ;
NO_ES_CIERTO               : 'no_es_cierto' | 'no' [ \t]+ 'es' [ \t]+ 'cierto' ;
AND_OP                     : '&&' | 'and' ;
OR_OP                      : '||' | 'or' ;
NOT_OP                     : '!' | 'not' ;

SEPARADOR                  : 'separador' ;
EN                         : 'en' ;
TITULO                     : 'titulo' ;
EJE_X                      : 'eje_x' | 'eje' [ \t]+ 'x' ;
EJE_Y                      : 'eje_y' | 'eje' [ \t]+ 'y' ;
GUARDAR                    : 'guardar' ;

COMA                       : ',' ;
DOS_PUNTOS                 : ':' ;
PAREN_IZQ                  : '(' ;
PAREN_DER                  : ')' ;
CORCH_IZQ                  : '[' ;
CORCH_DER                  : ']' ;

MAS                        : '+' ;
MENOS                      : '-' ;
MULT                       : '*' ;
DIV                        : '/' ;
MOD                        : '%' ;
POT                        : '^' ;

MAYOR_IGUAL                : '>=' ;
MENOR_IGUAL                : '<=' ;
IGUAL_IGUAL                : '==' ;
DIFERENTE                  : '!=' ;
MAYOR                      : '>' ;
MENOR                      : '<' ;

ID                         : [a-zA-Z_] [a-zA-Z0-9_]* ;
NUMERO                     : [0-9]+ ('.' [0-9]+)? ;
CADENA                     : '"' (~["\r\n])* '"' | '\'' (~['\r\n])* '\'' ;

COMENTARIO                 : ('#' | '//') ~[\r\n]* -> skip ;
WS                         : [ \t\r\n]+ -> skip ;
