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
    : (JUNTAR_A_LA_GRASA_POR | AGRUPAR_A_LOS_PAPUS_POR) listaIDs
    ;

operacionResumir
    : (SACAR_CUENTAS | RESUMIR_MOMOS) listaAgregaciones
    ;

listaAgregaciones
    : agregacion (COMA agregacion)*
    ;

agregacion
    : ID '=' funcionAgg PAREN_IZQ ID? PAREN_DER
    ;

funcionAgg
    : SUMA
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

instruccionSi
    : SI_EL_PAPU expresionBooleana ENTONCES bloque (SINO_CALLESE_SENORA bloque)? FIN_DEL_MOMO
    ;

bloque
    : sentencia+
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
    : factor ((MULT | DIV | MOD | POT) factor)*
    ;

factor
    : PAREN_IZQ expresionAritmetica PAREN_DER
    | ID
    | NUMERO
    | CADENA
    ;

listaIDs
    : CORCH_IZQ ID (COMA ID)* CORCH_DER
    | ID
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

SUMA                       : 'suma' | 'sumar_momos' ;
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

SI_EL_PAPU                 : 'si_el_papu' | 'si' [ \t]+ 'el' [ \t]+ 'papu' ;
ENTONCES                   : 'entonces' ;
SINO_CALLESE_SENORA        : 'sino_callese_senora' | 'sino' [ \t]+ 'callese' [ \t]+ ('señora' | 'senora') ;
FIN_DEL_MOMO               : 'fin_del_momo' | 'fin' [ \t]+ 'del' [ \t]+ 'momo' ;

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
