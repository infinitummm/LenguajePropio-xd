# Generated from grammar/LenguajeMomoXD.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,81,272,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,5,0,64,8,0,10,0,12,0,
        67,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,3,1,89,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,
        98,8,3,10,3,12,3,101,9,3,1,4,1,4,3,4,105,8,4,1,5,1,5,1,5,1,5,3,5,
        111,8,5,1,6,1,6,1,6,1,6,3,6,117,8,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,
        1,8,1,8,1,8,1,8,3,8,130,8,8,1,9,1,9,1,9,1,10,1,10,1,10,1,11,1,11,
        1,11,3,11,141,8,11,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,
        1,14,1,14,1,15,1,15,1,15,5,15,157,8,15,10,15,12,15,160,9,15,1,16,
        1,16,1,16,1,16,1,16,3,16,167,8,16,1,16,1,16,1,17,1,17,1,18,1,18,
        1,18,1,18,3,18,177,8,18,1,18,1,18,3,18,181,8,18,1,18,1,18,3,18,185,
        8,18,1,18,1,18,3,18,189,8,18,1,19,1,19,1,20,1,20,1,20,1,20,1,20,
        1,20,3,20,199,8,20,1,20,1,20,1,21,4,21,204,8,21,11,21,12,21,205,
        1,22,1,22,1,22,1,22,1,23,1,23,1,24,1,24,1,24,5,24,217,8,24,10,24,
        12,24,220,9,24,1,25,1,25,1,25,5,25,225,8,25,10,25,12,25,228,9,25,
        1,26,1,26,1,26,1,26,1,26,1,26,1,26,1,26,3,26,238,8,26,1,27,1,27,
        1,27,3,27,243,8,27,1,27,1,27,1,28,1,28,3,28,249,8,28,1,29,1,29,1,
        29,5,29,254,8,29,10,29,12,29,257,9,29,1,30,1,30,1,30,1,30,5,30,263,
        8,30,10,30,12,30,266,9,30,1,30,1,30,3,30,270,8,30,1,30,0,0,31,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,60,0,14,1,0,5,7,1,0,8,9,1,0,10,12,1,0,13,16,1,
        0,17,18,1,0,19,22,1,0,23,25,1,0,26,27,1,0,28,29,1,0,30,43,1,0,44,
        48,1,0,71,76,1,0,65,66,1,0,67,70,276,0,65,1,0,0,0,2,88,1,0,0,0,4,
        90,1,0,0,0,6,94,1,0,0,0,8,104,1,0,0,0,10,106,1,0,0,0,12,112,1,0,
        0,0,14,118,1,0,0,0,16,129,1,0,0,0,18,131,1,0,0,0,20,134,1,0,0,0,
        22,137,1,0,0,0,24,142,1,0,0,0,26,147,1,0,0,0,28,150,1,0,0,0,30,153,
        1,0,0,0,32,161,1,0,0,0,34,170,1,0,0,0,36,172,1,0,0,0,38,190,1,0,
        0,0,40,192,1,0,0,0,42,203,1,0,0,0,44,207,1,0,0,0,46,211,1,0,0,0,
        48,213,1,0,0,0,50,221,1,0,0,0,52,237,1,0,0,0,54,239,1,0,0,0,56,248,
        1,0,0,0,58,250,1,0,0,0,60,269,1,0,0,0,62,64,3,2,1,0,63,62,1,0,0,
        0,64,67,1,0,0,0,65,63,1,0,0,0,65,66,1,0,0,0,66,68,1,0,0,0,67,65,
        1,0,0,0,68,69,5,0,0,1,69,1,1,0,0,0,70,71,3,4,2,0,71,72,5,2,0,0,72,
        89,1,0,0,0,73,74,3,12,6,0,74,75,5,2,0,0,75,89,1,0,0,0,76,77,3,14,
        7,0,77,78,5,2,0,0,78,89,1,0,0,0,79,80,3,36,18,0,80,81,5,2,0,0,81,
        89,1,0,0,0,82,83,3,40,20,0,83,84,5,2,0,0,84,89,1,0,0,0,85,86,3,48,
        24,0,86,87,5,2,0,0,87,89,1,0,0,0,88,70,1,0,0,0,88,73,1,0,0,0,88,
        76,1,0,0,0,88,79,1,0,0,0,88,82,1,0,0,0,88,85,1,0,0,0,89,3,1,0,0,
        0,90,91,5,77,0,0,91,92,5,1,0,0,92,93,3,6,3,0,93,5,1,0,0,0,94,99,
        3,8,4,0,95,96,5,3,0,0,96,98,3,16,8,0,97,95,1,0,0,0,98,101,1,0,0,
        0,99,97,1,0,0,0,99,100,1,0,0,0,100,7,1,0,0,0,101,99,1,0,0,0,102,
        105,3,10,5,0,103,105,3,48,24,0,104,102,1,0,0,0,104,103,1,0,0,0,105,
        9,1,0,0,0,106,107,7,0,0,0,107,110,5,79,0,0,108,109,5,53,0,0,109,
        111,5,79,0,0,110,108,1,0,0,0,110,111,1,0,0,0,111,11,1,0,0,0,112,
        116,5,4,0,0,113,117,3,48,24,0,114,117,5,79,0,0,115,117,5,77,0,0,
        116,113,1,0,0,0,116,114,1,0,0,0,116,115,1,0,0,0,117,13,1,0,0,0,118,
        119,7,1,0,0,119,120,5,77,0,0,120,121,5,54,0,0,121,122,5,79,0,0,122,
        15,1,0,0,0,123,130,3,18,9,0,124,130,3,20,10,0,125,130,3,22,11,0,
        126,130,3,24,12,0,127,130,3,26,13,0,128,130,3,28,14,0,129,123,1,
        0,0,0,129,124,1,0,0,0,129,125,1,0,0,0,129,126,1,0,0,0,129,127,1,
        0,0,0,129,128,1,0,0,0,130,17,1,0,0,0,131,132,7,2,0,0,132,133,3,60,
        30,0,133,19,1,0,0,0,134,135,7,3,0,0,135,136,3,44,22,0,136,21,1,0,
        0,0,137,138,7,4,0,0,138,140,5,77,0,0,139,141,7,5,0,0,140,139,1,0,
        0,0,140,141,1,0,0,0,141,23,1,0,0,0,142,143,7,6,0,0,143,144,5,77,
        0,0,144,145,5,1,0,0,145,146,3,48,24,0,146,25,1,0,0,0,147,148,7,7,
        0,0,148,149,3,60,30,0,149,27,1,0,0,0,150,151,7,8,0,0,151,152,3,30,
        15,0,152,29,1,0,0,0,153,158,3,32,16,0,154,155,5,59,0,0,155,157,3,
        32,16,0,156,154,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,159,
        1,0,0,0,159,31,1,0,0,0,160,158,1,0,0,0,161,162,5,77,0,0,162,163,
        5,1,0,0,163,164,3,34,17,0,164,166,5,61,0,0,165,167,5,77,0,0,166,
        165,1,0,0,0,166,167,1,0,0,0,167,168,1,0,0,0,168,169,5,62,0,0,169,
        33,1,0,0,0,170,171,7,9,0,0,171,35,1,0,0,0,172,173,3,38,19,0,173,
        176,5,77,0,0,174,175,5,55,0,0,175,177,5,79,0,0,176,174,1,0,0,0,176,
        177,1,0,0,0,177,180,1,0,0,0,178,179,5,56,0,0,179,181,5,79,0,0,180,
        178,1,0,0,0,180,181,1,0,0,0,181,184,1,0,0,0,182,183,5,57,0,0,183,
        185,5,79,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,188,1,0,0,0,186,
        187,5,58,0,0,187,189,5,79,0,0,188,186,1,0,0,0,188,189,1,0,0,0,189,
        37,1,0,0,0,190,191,7,10,0,0,191,39,1,0,0,0,192,193,5,49,0,0,193,
        194,3,44,22,0,194,195,5,50,0,0,195,198,3,42,21,0,196,197,5,51,0,
        0,197,199,3,42,21,0,198,196,1,0,0,0,198,199,1,0,0,0,199,200,1,0,
        0,0,200,201,5,52,0,0,201,41,1,0,0,0,202,204,3,2,1,0,203,202,1,0,
        0,0,204,205,1,0,0,0,205,203,1,0,0,0,205,206,1,0,0,0,206,43,1,0,0,
        0,207,208,3,48,24,0,208,209,3,46,23,0,209,210,3,48,24,0,210,45,1,
        0,0,0,211,212,7,11,0,0,212,47,1,0,0,0,213,218,3,50,25,0,214,215,
        7,12,0,0,215,217,3,50,25,0,216,214,1,0,0,0,217,220,1,0,0,0,218,216,
        1,0,0,0,218,219,1,0,0,0,219,49,1,0,0,0,220,218,1,0,0,0,221,226,3,
        52,26,0,222,223,7,13,0,0,223,225,3,52,26,0,224,222,1,0,0,0,225,228,
        1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,227,51,1,0,0,0,228,226,1,
        0,0,0,229,230,5,61,0,0,230,231,3,48,24,0,231,232,5,62,0,0,232,238,
        1,0,0,0,233,238,3,54,27,0,234,238,5,77,0,0,235,238,5,78,0,0,236,
        238,5,79,0,0,237,229,1,0,0,0,237,233,1,0,0,0,237,234,1,0,0,0,237,
        235,1,0,0,0,237,236,1,0,0,0,238,53,1,0,0,0,239,240,3,56,28,0,240,
        242,5,61,0,0,241,243,3,58,29,0,242,241,1,0,0,0,242,243,1,0,0,0,243,
        244,1,0,0,0,244,245,5,62,0,0,245,55,1,0,0,0,246,249,5,77,0,0,247,
        249,3,34,17,0,248,246,1,0,0,0,248,247,1,0,0,0,249,57,1,0,0,0,250,
        255,3,48,24,0,251,252,5,59,0,0,252,254,3,48,24,0,253,251,1,0,0,0,
        254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,59,1,0,0,0,257,
        255,1,0,0,0,258,259,5,63,0,0,259,264,5,77,0,0,260,261,5,59,0,0,261,
        263,5,77,0,0,262,260,1,0,0,0,263,266,1,0,0,0,264,262,1,0,0,0,264,
        265,1,0,0,0,265,267,1,0,0,0,266,264,1,0,0,0,267,270,5,64,0,0,268,
        270,5,77,0,0,269,258,1,0,0,0,269,268,1,0,0,0,270,61,1,0,0,0,24,65,
        88,99,104,110,116,129,140,158,166,176,180,184,188,198,205,218,226,
        237,242,248,255,264,269
    ]

class LenguajeMomoXDParser ( Parser ):

    grammarFileName = "LenguajeMomoXD.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'ascendente'", "'descendente'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'promedio'", "'media'", "'mediana'", 
                     "<INVALID>", "'maximo'", "<INVALID>", "'minimo'", "<INVALID>", 
                     "'conteo'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'entonces'", "<INVALID>", "<INVALID>", "'separador'", 
                     "'en'", "'titulo'", "<INVALID>", "<INVALID>", "'guardar'", 
                     "','", "':'", "'('", "')'", "'['", "']'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'^'", "'>='", "'<='", "'=='", 
                     "'!='", "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "XD", "PIPE", "WHEN_HACES", 
                      "PASA_EL_PACK", "PASA_EL_ZELDA", "ROBAR_MOMO", "SUBIR_AL_GRUPO", 
                      "GUARDAR_MOMO", "ESCOJO_A", "ESCOJO_A_LOS_PAPUS", 
                      "SELECCIONAR_MOMOS", "BUT_TE_ENTERAS_QUE", "BUT_ELLA_NO_TE_AMA", 
                      "NO_LO_SE_RICK", "FILTRAR_GRASOSOS", "ORDENAR_A_LOS_PAPUS", 
                      "ORDENAR_MOMOS", "DE_ARRIBA_A_ABAJO", "DE_ABAJO_A_ARRIBA", 
                      "ASCENDENTE", "DESCENDENTE", "EL_FUTURO_ES_HOY_OISTE_VIEJO", 
                      "METANLE_SABOR_A", "CREAR_MOMO", "JUNTAR_A_LA_GRASA_POR", 
                      "AGRUPAR_A_LOS_PAPUS_POR", "SACAR_CUENTAS", "RESUMIR_MOMOS", 
                      "SUMA", "MULTIPLICACION", "RESTA", "DIVISION", "PROMEDIO", 
                      "MEDIA", "MEDIANA", "EL_MAS_PRO", "MAXIMO", "EL_MAS_MANCO", 
                      "MINIMO", "CONTAR_PAPUS", "CONTEO", "DESVIACION_PRO", 
                      "GRAFICAR_MOMOS_EN_BARRAS", "GRAFICAR_MOMOS_EN_LINEAS", 
                      "GRAFICAR_MOMOS_EN_HISTOGRAMA", "GRAFICAR_MOMOS_EN_DISPERSION", 
                      "GRAFICAR_MOMOS_EN_CAJAS", "SI_EL_PAPU", "ENTONCES", 
                      "SINO_CALLESE_SENORA", "FIN_DEL_MOMO", "SEPARADOR", 
                      "EN", "TITULO", "EJE_X", "EJE_Y", "GUARDAR", "COMA", 
                      "DOS_PUNTOS", "PAREN_IZQ", "PAREN_DER", "CORCH_IZQ", 
                      "CORCH_DER", "MAS", "MENOS", "MULT", "DIV", "MOD", 
                      "POT", "MAYOR_IGUAL", "MENOR_IGUAL", "IGUAL_IGUAL", 
                      "DIFERENTE", "MAYOR", "MENOR", "ID", "NUMERO", "CADENA", 
                      "COMENTARIO", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_expresionPipeline = 3
    RULE_expresionBase = 4
    RULE_instruccionCarga = 5
    RULE_instruccionImprimir = 6
    RULE_instruccionGuardado = 7
    RULE_operacionPipeline = 8
    RULE_operacionSeleccionar = 9
    RULE_operacionFiltrar = 10
    RULE_operacionOrdenar = 11
    RULE_operacionCrearColumna = 12
    RULE_operacionAgrupar = 13
    RULE_operacionResumir = 14
    RULE_listaAgregaciones = 15
    RULE_agregacion = 16
    RULE_funcionAgg = 17
    RULE_instruccionVisualizacion = 18
    RULE_tipoGrafico = 19
    RULE_instruccionSi = 20
    RULE_bloque = 21
    RULE_expresionBooleana = 22
    RULE_opRelacional = 23
    RULE_expresionAritmetica = 24
    RULE_termino = 25
    RULE_factor = 26
    RULE_llamadaFuncion = 27
    RULE_funcionNombre = 28
    RULE_listaArgumentos = 29
    RULE_listaIDs = 30

    ruleNames =  [ "programa", "sentencia", "asignacion", "expresionPipeline", 
                   "expresionBase", "instruccionCarga", "instruccionImprimir", 
                   "instruccionGuardado", "operacionPipeline", "operacionSeleccionar", 
                   "operacionFiltrar", "operacionOrdenar", "operacionCrearColumna", 
                   "operacionAgrupar", "operacionResumir", "listaAgregaciones", 
                   "agregacion", "funcionAgg", "instruccionVisualizacion", 
                   "tipoGrafico", "instruccionSi", "bloque", "expresionBooleana", 
                   "opRelacional", "expresionAritmetica", "termino", "factor", 
                   "llamadaFuncion", "funcionNombre", "listaArgumentos", 
                   "listaIDs" ]

    EOF = Token.EOF
    T__0=1
    XD=2
    PIPE=3
    WHEN_HACES=4
    PASA_EL_PACK=5
    PASA_EL_ZELDA=6
    ROBAR_MOMO=7
    SUBIR_AL_GRUPO=8
    GUARDAR_MOMO=9
    ESCOJO_A=10
    ESCOJO_A_LOS_PAPUS=11
    SELECCIONAR_MOMOS=12
    BUT_TE_ENTERAS_QUE=13
    BUT_ELLA_NO_TE_AMA=14
    NO_LO_SE_RICK=15
    FILTRAR_GRASOSOS=16
    ORDENAR_A_LOS_PAPUS=17
    ORDENAR_MOMOS=18
    DE_ARRIBA_A_ABAJO=19
    DE_ABAJO_A_ARRIBA=20
    ASCENDENTE=21
    DESCENDENTE=22
    EL_FUTURO_ES_HOY_OISTE_VIEJO=23
    METANLE_SABOR_A=24
    CREAR_MOMO=25
    JUNTAR_A_LA_GRASA_POR=26
    AGRUPAR_A_LOS_PAPUS_POR=27
    SACAR_CUENTAS=28
    RESUMIR_MOMOS=29
    SUMA=30
    MULTIPLICACION=31
    RESTA=32
    DIVISION=33
    PROMEDIO=34
    MEDIA=35
    MEDIANA=36
    EL_MAS_PRO=37
    MAXIMO=38
    EL_MAS_MANCO=39
    MINIMO=40
    CONTAR_PAPUS=41
    CONTEO=42
    DESVIACION_PRO=43
    GRAFICAR_MOMOS_EN_BARRAS=44
    GRAFICAR_MOMOS_EN_LINEAS=45
    GRAFICAR_MOMOS_EN_HISTOGRAMA=46
    GRAFICAR_MOMOS_EN_DISPERSION=47
    GRAFICAR_MOMOS_EN_CAJAS=48
    SI_EL_PAPU=49
    ENTONCES=50
    SINO_CALLESE_SENORA=51
    FIN_DEL_MOMO=52
    SEPARADOR=53
    EN=54
    TITULO=55
    EJE_X=56
    EJE_Y=57
    GUARDAR=58
    COMA=59
    DOS_PUNTOS=60
    PAREN_IZQ=61
    PAREN_DER=62
    CORCH_IZQ=63
    CORCH_DER=64
    MAS=65
    MENOS=66
    MULT=67
    DIV=68
    MOD=69
    POT=70
    MAYOR_IGUAL=71
    MENOR_IGUAL=72
    IGUAL_IGUAL=73
    DIFERENTE=74
    MAYOR=75
    MENOR=76
    ID=77
    NUMERO=78
    CADENA=79
    COMENTARIO=80
    WS=81

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LenguajeMomoXDParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LenguajeMomoXDParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2306968908046795536) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 7) != 0):
                self.state = 62
                self.sentencia()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(LenguajeMomoXDParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SentenciaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.AsignacionContext,0)


        def XD(self):
            return self.getToken(LenguajeMomoXDParser.XD, 0)

        def instruccionImprimir(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.InstruccionImprimirContext,0)


        def instruccionGuardado(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.InstruccionGuardadoContext,0)


        def instruccionVisualizacion(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.InstruccionVisualizacionContext,0)


        def instruccionSi(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.InstruccionSiContext,0)


        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_sentencia

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSentencia" ):
                listener.enterSentencia(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSentencia" ):
                listener.exitSentencia(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSentencia" ):
                return visitor.visitSentencia(self)
            else:
                return visitor.visitChildren(self)




    def sentencia(self):

        localctx = LenguajeMomoXDParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 88
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.asignacion()
                self.state = 71
                self.match(LenguajeMomoXDParser.XD)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.instruccionImprimir()
                self.state = 74
                self.match(LenguajeMomoXDParser.XD)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.instruccionGuardado()
                self.state = 77
                self.match(LenguajeMomoXDParser.XD)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 79
                self.instruccionVisualizacion()
                self.state = 80
                self.match(LenguajeMomoXDParser.XD)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.instruccionSi()
                self.state = 83
                self.match(LenguajeMomoXDParser.XD)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 85
                self.expresionAritmetica()
                self.state = 86
                self.match(LenguajeMomoXDParser.XD)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def expresionPipeline(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionPipelineContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = LenguajeMomoXDParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            self.match(LenguajeMomoXDParser.ID)
            self.state = 91
            self.match(LenguajeMomoXDParser.T__0)
            self.state = 92
            self.expresionPipeline()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionPipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionBase(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionBaseContext,0)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.PIPE)
            else:
                return self.getToken(LenguajeMomoXDParser.PIPE, i)

        def operacionPipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.OperacionPipelineContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionPipelineContext,i)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_expresionPipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionPipeline" ):
                listener.enterExpresionPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionPipeline" ):
                listener.exitExpresionPipeline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionPipeline" ):
                return visitor.visitExpresionPipeline(self)
            else:
                return visitor.visitChildren(self)




    def expresionPipeline(self):

        localctx = LenguajeMomoXDParser.ExpresionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expresionPipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 94
            self.expresionBase()
            self.state = 99
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 95
                self.match(LenguajeMomoXDParser.PIPE)
                self.state = 96
                self.operacionPipeline()
                self.state = 101
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionBaseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def instruccionCarga(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.InstruccionCargaContext,0)


        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_expresionBase

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionBase" ):
                listener.enterExpresionBase(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionBase" ):
                listener.exitExpresionBase(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionBase" ):
                return visitor.visitExpresionBase(self)
            else:
                return visitor.visitChildren(self)




    def expresionBase(self):

        localctx = LenguajeMomoXDParser.ExpresionBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expresionBase)
        try:
            self.state = 104
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [5, 6, 7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 102
                self.instruccionCarga()
                pass
            elif token in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 61, 77, 78, 79]:
                self.enterOuterAlt(localctx, 2)
                self.state = 103
                self.expresionAritmetica()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionCargaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.CADENA)
            else:
                return self.getToken(LenguajeMomoXDParser.CADENA, i)

        def PASA_EL_PACK(self):
            return self.getToken(LenguajeMomoXDParser.PASA_EL_PACK, 0)

        def PASA_EL_ZELDA(self):
            return self.getToken(LenguajeMomoXDParser.PASA_EL_ZELDA, 0)

        def ROBAR_MOMO(self):
            return self.getToken(LenguajeMomoXDParser.ROBAR_MOMO, 0)

        def SEPARADOR(self):
            return self.getToken(LenguajeMomoXDParser.SEPARADOR, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_instruccionCarga

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionCarga" ):
                listener.enterInstruccionCarga(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionCarga" ):
                listener.exitInstruccionCarga(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionCarga" ):
                return visitor.visitInstruccionCarga(self)
            else:
                return visitor.visitChildren(self)




    def instruccionCarga(self):

        localctx = LenguajeMomoXDParser.InstruccionCargaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instruccionCarga)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 224) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 107
            self.match(LenguajeMomoXDParser.CADENA)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==53:
                self.state = 108
                self.match(LenguajeMomoXDParser.SEPARADOR)
                self.state = 109
                self.match(LenguajeMomoXDParser.CADENA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionImprimirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN_HACES(self):
            return self.getToken(LenguajeMomoXDParser.WHEN_HACES, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,0)


        def CADENA(self):
            return self.getToken(LenguajeMomoXDParser.CADENA, 0)

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_instruccionImprimir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionImprimir" ):
                listener.enterInstruccionImprimir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionImprimir" ):
                listener.exitInstruccionImprimir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionImprimir" ):
                return visitor.visitInstruccionImprimir(self)
            else:
                return visitor.visitChildren(self)




    def instruccionImprimir(self):

        localctx = LenguajeMomoXDParser.InstruccionImprimirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instruccionImprimir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(LenguajeMomoXDParser.WHEN_HACES)
            self.state = 116
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 113
                self.expresionAritmetica()
                pass

            elif la_ == 2:
                self.state = 114
                self.match(LenguajeMomoXDParser.CADENA)
                pass

            elif la_ == 3:
                self.state = 115
                self.match(LenguajeMomoXDParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionGuardadoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def EN(self):
            return self.getToken(LenguajeMomoXDParser.EN, 0)

        def CADENA(self):
            return self.getToken(LenguajeMomoXDParser.CADENA, 0)

        def SUBIR_AL_GRUPO(self):
            return self.getToken(LenguajeMomoXDParser.SUBIR_AL_GRUPO, 0)

        def GUARDAR_MOMO(self):
            return self.getToken(LenguajeMomoXDParser.GUARDAR_MOMO, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_instruccionGuardado

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionGuardado" ):
                listener.enterInstruccionGuardado(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionGuardado" ):
                listener.exitInstruccionGuardado(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionGuardado" ):
                return visitor.visitInstruccionGuardado(self)
            else:
                return visitor.visitChildren(self)




    def instruccionGuardado(self):

        localctx = LenguajeMomoXDParser.InstruccionGuardadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_instruccionGuardado)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 119
            self.match(LenguajeMomoXDParser.ID)
            self.state = 120
            self.match(LenguajeMomoXDParser.EN)
            self.state = 121
            self.match(LenguajeMomoXDParser.CADENA)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionPipelineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operacionSeleccionar(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionSeleccionarContext,0)


        def operacionFiltrar(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionFiltrarContext,0)


        def operacionOrdenar(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionOrdenarContext,0)


        def operacionCrearColumna(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionCrearColumnaContext,0)


        def operacionAgrupar(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionAgruparContext,0)


        def operacionResumir(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OperacionResumirContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionPipeline

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionPipeline" ):
                listener.enterOperacionPipeline(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionPipeline" ):
                listener.exitOperacionPipeline(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionPipeline" ):
                return visitor.visitOperacionPipeline(self)
            else:
                return visitor.visitChildren(self)




    def operacionPipeline(self):

        localctx = LenguajeMomoXDParser.OperacionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operacionPipeline)
        try:
            self.state = 129
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 11, 12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 123
                self.operacionSeleccionar()
                pass
            elif token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 2)
                self.state = 124
                self.operacionFiltrar()
                pass
            elif token in [17, 18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 125
                self.operacionOrdenar()
                pass
            elif token in [23, 24, 25]:
                self.enterOuterAlt(localctx, 4)
                self.state = 126
                self.operacionCrearColumna()
                pass
            elif token in [26, 27]:
                self.enterOuterAlt(localctx, 5)
                self.state = 127
                self.operacionAgrupar()
                pass
            elif token in [28, 29]:
                self.enterOuterAlt(localctx, 6)
                self.state = 128
                self.operacionResumir()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionSeleccionarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaIDs(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ListaIDsContext,0)


        def ESCOJO_A(self):
            return self.getToken(LenguajeMomoXDParser.ESCOJO_A, 0)

        def ESCOJO_A_LOS_PAPUS(self):
            return self.getToken(LenguajeMomoXDParser.ESCOJO_A_LOS_PAPUS, 0)

        def SELECCIONAR_MOMOS(self):
            return self.getToken(LenguajeMomoXDParser.SELECCIONAR_MOMOS, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionSeleccionar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionSeleccionar" ):
                listener.enterOperacionSeleccionar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionSeleccionar" ):
                listener.exitOperacionSeleccionar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionSeleccionar" ):
                return visitor.visitOperacionSeleccionar(self)
            else:
                return visitor.visitChildren(self)




    def operacionSeleccionar(self):

        localctx = LenguajeMomoXDParser.OperacionSeleccionarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operacionSeleccionar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7168) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 132
            self.listaIDs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionFiltrarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionBooleana(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionBooleanaContext,0)


        def BUT_TE_ENTERAS_QUE(self):
            return self.getToken(LenguajeMomoXDParser.BUT_TE_ENTERAS_QUE, 0)

        def BUT_ELLA_NO_TE_AMA(self):
            return self.getToken(LenguajeMomoXDParser.BUT_ELLA_NO_TE_AMA, 0)

        def NO_LO_SE_RICK(self):
            return self.getToken(LenguajeMomoXDParser.NO_LO_SE_RICK, 0)

        def FILTRAR_GRASOSOS(self):
            return self.getToken(LenguajeMomoXDParser.FILTRAR_GRASOSOS, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionFiltrar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionFiltrar" ):
                listener.enterOperacionFiltrar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionFiltrar" ):
                listener.exitOperacionFiltrar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionFiltrar" ):
                return visitor.visitOperacionFiltrar(self)
            else:
                return visitor.visitChildren(self)




    def operacionFiltrar(self):

        localctx = LenguajeMomoXDParser.OperacionFiltrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operacionFiltrar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 135
            self.expresionBooleana()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionOrdenarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def ORDENAR_A_LOS_PAPUS(self):
            return self.getToken(LenguajeMomoXDParser.ORDENAR_A_LOS_PAPUS, 0)

        def ORDENAR_MOMOS(self):
            return self.getToken(LenguajeMomoXDParser.ORDENAR_MOMOS, 0)

        def DE_ARRIBA_A_ABAJO(self):
            return self.getToken(LenguajeMomoXDParser.DE_ARRIBA_A_ABAJO, 0)

        def DE_ABAJO_A_ARRIBA(self):
            return self.getToken(LenguajeMomoXDParser.DE_ABAJO_A_ARRIBA, 0)

        def ASCENDENTE(self):
            return self.getToken(LenguajeMomoXDParser.ASCENDENTE, 0)

        def DESCENDENTE(self):
            return self.getToken(LenguajeMomoXDParser.DESCENDENTE, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionOrdenar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionOrdenar" ):
                listener.enterOperacionOrdenar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionOrdenar" ):
                listener.exitOperacionOrdenar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionOrdenar" ):
                return visitor.visitOperacionOrdenar(self)
            else:
                return visitor.visitChildren(self)




    def operacionOrdenar(self):

        localctx = LenguajeMomoXDParser.OperacionOrdenarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operacionOrdenar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            _la = self._input.LA(1)
            if not(_la==17 or _la==18):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 138
            self.match(LenguajeMomoXDParser.ID)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0):
                self.state = 139
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 7864320) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionCrearColumnaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,0)


        def EL_FUTURO_ES_HOY_OISTE_VIEJO(self):
            return self.getToken(LenguajeMomoXDParser.EL_FUTURO_ES_HOY_OISTE_VIEJO, 0)

        def METANLE_SABOR_A(self):
            return self.getToken(LenguajeMomoXDParser.METANLE_SABOR_A, 0)

        def CREAR_MOMO(self):
            return self.getToken(LenguajeMomoXDParser.CREAR_MOMO, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionCrearColumna

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionCrearColumna" ):
                listener.enterOperacionCrearColumna(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionCrearColumna" ):
                listener.exitOperacionCrearColumna(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionCrearColumna" ):
                return visitor.visitOperacionCrearColumna(self)
            else:
                return visitor.visitChildren(self)




    def operacionCrearColumna(self):

        localctx = LenguajeMomoXDParser.OperacionCrearColumnaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operacionCrearColumna)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 58720256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 143
            self.match(LenguajeMomoXDParser.ID)
            self.state = 144
            self.match(LenguajeMomoXDParser.T__0)
            self.state = 145
            self.expresionAritmetica()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionAgruparContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaIDs(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ListaIDsContext,0)


        def JUNTAR_A_LA_GRASA_POR(self):
            return self.getToken(LenguajeMomoXDParser.JUNTAR_A_LA_GRASA_POR, 0)

        def AGRUPAR_A_LOS_PAPUS_POR(self):
            return self.getToken(LenguajeMomoXDParser.AGRUPAR_A_LOS_PAPUS_POR, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionAgrupar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionAgrupar" ):
                listener.enterOperacionAgrupar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionAgrupar" ):
                listener.exitOperacionAgrupar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionAgrupar" ):
                return visitor.visitOperacionAgrupar(self)
            else:
                return visitor.visitChildren(self)




    def operacionAgrupar(self):

        localctx = LenguajeMomoXDParser.OperacionAgruparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operacionAgrupar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            _la = self._input.LA(1)
            if not(_la==26 or _la==27):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 148
            self.listaIDs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionResumirContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaAgregaciones(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ListaAgregacionesContext,0)


        def SACAR_CUENTAS(self):
            return self.getToken(LenguajeMomoXDParser.SACAR_CUENTAS, 0)

        def RESUMIR_MOMOS(self):
            return self.getToken(LenguajeMomoXDParser.RESUMIR_MOMOS, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_operacionResumir

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacionResumir" ):
                listener.enterOperacionResumir(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacionResumir" ):
                listener.exitOperacionResumir(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperacionResumir" ):
                return visitor.visitOperacionResumir(self)
            else:
                return visitor.visitChildren(self)




    def operacionResumir(self):

        localctx = LenguajeMomoXDParser.OperacionResumirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_operacionResumir)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            _la = self._input.LA(1)
            if not(_la==28 or _la==29):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 151
            self.listaAgregaciones()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaAgregacionesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def agregacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.AgregacionContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.AgregacionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.COMA)
            else:
                return self.getToken(LenguajeMomoXDParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_listaAgregaciones

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaAgregaciones" ):
                listener.enterListaAgregaciones(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaAgregaciones" ):
                listener.exitListaAgregaciones(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaAgregaciones" ):
                return visitor.visitListaAgregaciones(self)
            else:
                return visitor.visitChildren(self)




    def listaAgregaciones(self):

        localctx = LenguajeMomoXDParser.ListaAgregacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_listaAgregaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 153
            self.agregacion()
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 154
                self.match(LenguajeMomoXDParser.COMA)
                self.state = 155
                self.agregacion()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgregacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.ID)
            else:
                return self.getToken(LenguajeMomoXDParser.ID, i)

        def funcionAgg(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.FuncionAggContext,0)


        def PAREN_IZQ(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_DER, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_agregacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAgregacion" ):
                listener.enterAgregacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAgregacion" ):
                listener.exitAgregacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgregacion" ):
                return visitor.visitAgregacion(self)
            else:
                return visitor.visitChildren(self)




    def agregacion(self):

        localctx = LenguajeMomoXDParser.AgregacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_agregacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.match(LenguajeMomoXDParser.ID)
            self.state = 162
            self.match(LenguajeMomoXDParser.T__0)
            self.state = 163
            self.funcionAgg()
            self.state = 164
            self.match(LenguajeMomoXDParser.PAREN_IZQ)
            self.state = 166
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==77:
                self.state = 165
                self.match(LenguajeMomoXDParser.ID)


            self.state = 168
            self.match(LenguajeMomoXDParser.PAREN_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionAggContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SUMA(self):
            return self.getToken(LenguajeMomoXDParser.SUMA, 0)

        def MULTIPLICACION(self):
            return self.getToken(LenguajeMomoXDParser.MULTIPLICACION, 0)

        def RESTA(self):
            return self.getToken(LenguajeMomoXDParser.RESTA, 0)

        def DIVISION(self):
            return self.getToken(LenguajeMomoXDParser.DIVISION, 0)

        def PROMEDIO(self):
            return self.getToken(LenguajeMomoXDParser.PROMEDIO, 0)

        def MEDIA(self):
            return self.getToken(LenguajeMomoXDParser.MEDIA, 0)

        def MEDIANA(self):
            return self.getToken(LenguajeMomoXDParser.MEDIANA, 0)

        def EL_MAS_PRO(self):
            return self.getToken(LenguajeMomoXDParser.EL_MAS_PRO, 0)

        def MAXIMO(self):
            return self.getToken(LenguajeMomoXDParser.MAXIMO, 0)

        def EL_MAS_MANCO(self):
            return self.getToken(LenguajeMomoXDParser.EL_MAS_MANCO, 0)

        def MINIMO(self):
            return self.getToken(LenguajeMomoXDParser.MINIMO, 0)

        def CONTAR_PAPUS(self):
            return self.getToken(LenguajeMomoXDParser.CONTAR_PAPUS, 0)

        def CONTEO(self):
            return self.getToken(LenguajeMomoXDParser.CONTEO, 0)

        def DESVIACION_PRO(self):
            return self.getToken(LenguajeMomoXDParser.DESVIACION_PRO, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_funcionAgg

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionAgg" ):
                listener.enterFuncionAgg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionAgg" ):
                listener.exitFuncionAgg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionAgg" ):
                return visitor.visitFuncionAgg(self)
            else:
                return visitor.visitChildren(self)




    def funcionAgg(self):

        localctx = LenguajeMomoXDParser.FuncionAggContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_funcionAgg)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17591112302592) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionVisualizacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tipoGrafico(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.TipoGraficoContext,0)


        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def TITULO(self):
            return self.getToken(LenguajeMomoXDParser.TITULO, 0)

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.CADENA)
            else:
                return self.getToken(LenguajeMomoXDParser.CADENA, i)

        def EJE_X(self):
            return self.getToken(LenguajeMomoXDParser.EJE_X, 0)

        def EJE_Y(self):
            return self.getToken(LenguajeMomoXDParser.EJE_Y, 0)

        def GUARDAR(self):
            return self.getToken(LenguajeMomoXDParser.GUARDAR, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_instruccionVisualizacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionVisualizacion" ):
                listener.enterInstruccionVisualizacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionVisualizacion" ):
                listener.exitInstruccionVisualizacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionVisualizacion" ):
                return visitor.visitInstruccionVisualizacion(self)
            else:
                return visitor.visitChildren(self)




    def instruccionVisualizacion(self):

        localctx = LenguajeMomoXDParser.InstruccionVisualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_instruccionVisualizacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.tipoGrafico()
            self.state = 173
            self.match(LenguajeMomoXDParser.ID)
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==55:
                self.state = 174
                self.match(LenguajeMomoXDParser.TITULO)
                self.state = 175
                self.match(LenguajeMomoXDParser.CADENA)


            self.state = 180
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==56:
                self.state = 178
                self.match(LenguajeMomoXDParser.EJE_X)
                self.state = 179
                self.match(LenguajeMomoXDParser.CADENA)


            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==57:
                self.state = 182
                self.match(LenguajeMomoXDParser.EJE_Y)
                self.state = 183
                self.match(LenguajeMomoXDParser.CADENA)


            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 186
                self.match(LenguajeMomoXDParser.GUARDAR)
                self.state = 187
                self.match(LenguajeMomoXDParser.CADENA)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoGraficoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAFICAR_MOMOS_EN_BARRAS(self):
            return self.getToken(LenguajeMomoXDParser.GRAFICAR_MOMOS_EN_BARRAS, 0)

        def GRAFICAR_MOMOS_EN_LINEAS(self):
            return self.getToken(LenguajeMomoXDParser.GRAFICAR_MOMOS_EN_LINEAS, 0)

        def GRAFICAR_MOMOS_EN_HISTOGRAMA(self):
            return self.getToken(LenguajeMomoXDParser.GRAFICAR_MOMOS_EN_HISTOGRAMA, 0)

        def GRAFICAR_MOMOS_EN_DISPERSION(self):
            return self.getToken(LenguajeMomoXDParser.GRAFICAR_MOMOS_EN_DISPERSION, 0)

        def GRAFICAR_MOMOS_EN_CAJAS(self):
            return self.getToken(LenguajeMomoXDParser.GRAFICAR_MOMOS_EN_CAJAS, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_tipoGrafico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoGrafico" ):
                listener.enterTipoGrafico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoGrafico" ):
                listener.exitTipoGrafico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoGrafico" ):
                return visitor.visitTipoGrafico(self)
            else:
                return visitor.visitChildren(self)




    def tipoGrafico(self):

        localctx = LenguajeMomoXDParser.TipoGraficoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_tipoGrafico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 545357767376896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstruccionSiContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SI_EL_PAPU(self):
            return self.getToken(LenguajeMomoXDParser.SI_EL_PAPU, 0)

        def expresionBooleana(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionBooleanaContext,0)


        def ENTONCES(self):
            return self.getToken(LenguajeMomoXDParser.ENTONCES, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.BloqueContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.BloqueContext,i)


        def FIN_DEL_MOMO(self):
            return self.getToken(LenguajeMomoXDParser.FIN_DEL_MOMO, 0)

        def SINO_CALLESE_SENORA(self):
            return self.getToken(LenguajeMomoXDParser.SINO_CALLESE_SENORA, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_instruccionSi

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruccionSi" ):
                listener.enterInstruccionSi(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruccionSi" ):
                listener.exitInstruccionSi(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruccionSi" ):
                return visitor.visitInstruccionSi(self)
            else:
                return visitor.visitChildren(self)




    def instruccionSi(self):

        localctx = LenguajeMomoXDParser.InstruccionSiContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_instruccionSi)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(LenguajeMomoXDParser.SI_EL_PAPU)
            self.state = 193
            self.expresionBooleana()
            self.state = 194
            self.match(LenguajeMomoXDParser.ENTONCES)
            self.state = 195
            self.bloque()
            self.state = 198
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==51:
                self.state = 196
                self.match(LenguajeMomoXDParser.SINO_CALLESE_SENORA)
                self.state = 197
                self.bloque()


            self.state = 200
            self.match(LenguajeMomoXDParser.FIN_DEL_MOMO)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = LenguajeMomoXDParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 202
                self.sentencia()
                self.state = 205 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2306968908046795536) != 0) or ((((_la - 77)) & ~0x3f) == 0 and ((1 << (_la - 77)) & 7) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.ExpresionAritmeticaContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,i)


        def opRelacional(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.OpRelacionalContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_expresionBooleana

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionBooleana" ):
                listener.enterExpresionBooleana(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionBooleana" ):
                listener.exitExpresionBooleana(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionBooleana" ):
                return visitor.visitExpresionBooleana(self)
            else:
                return visitor.visitChildren(self)




    def expresionBooleana(self):

        localctx = LenguajeMomoXDParser.ExpresionBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expresionBooleana)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.expresionAritmetica()
            self.state = 208
            self.opRelacional()
            self.state = 209
            self.expresionAritmetica()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpRelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAYOR_IGUAL(self):
            return self.getToken(LenguajeMomoXDParser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(LenguajeMomoXDParser.MENOR_IGUAL, 0)

        def IGUAL_IGUAL(self):
            return self.getToken(LenguajeMomoXDParser.IGUAL_IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(LenguajeMomoXDParser.DIFERENTE, 0)

        def MAYOR(self):
            return self.getToken(LenguajeMomoXDParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(LenguajeMomoXDParser.MENOR, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_opRelacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpRelacional" ):
                listener.enterOpRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpRelacional" ):
                listener.exitOpRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpRelacional" ):
                return visitor.visitOpRelacional(self)
            else:
                return visitor.visitChildren(self)




    def opRelacional(self):

        localctx = LenguajeMomoXDParser.OpRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_opRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            _la = self._input.LA(1)
            if not(((((_la - 71)) & ~0x3f) == 0 and ((1 << (_la - 71)) & 63) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionAritmeticaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.TerminoContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.TerminoContext,i)


        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.MAS)
            else:
                return self.getToken(LenguajeMomoXDParser.MAS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.MENOS)
            else:
                return self.getToken(LenguajeMomoXDParser.MENOS, i)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_expresionAritmetica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresionAritmetica" ):
                listener.enterExpresionAritmetica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresionAritmetica" ):
                listener.exitExpresionAritmetica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresionAritmetica" ):
                return visitor.visitExpresionAritmetica(self)
            else:
                return visitor.visitChildren(self)




    def expresionAritmetica(self):

        localctx = LenguajeMomoXDParser.ExpresionAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expresionAritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.termino()
            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==65 or _la==66:
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==65 or _la==66):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.termino()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.FactorContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.MULT)
            else:
                return self.getToken(LenguajeMomoXDParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.DIV)
            else:
                return self.getToken(LenguajeMomoXDParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.MOD)
            else:
                return self.getToken(LenguajeMomoXDParser.MOD, i)

        def POT(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.POT)
            else:
                return self.getToken(LenguajeMomoXDParser.POT, i)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = LenguajeMomoXDParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.factor()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0):
                self.state = 222
                _la = self._input.LA(1)
                if not(((((_la - 67)) & ~0x3f) == 0 and ((1 << (_la - 67)) & 15) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 223
                self.factor()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PAREN_IZQ(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_IZQ, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,0)


        def PAREN_DER(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_DER, 0)

        def llamadaFuncion(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.LlamadaFuncionContext,0)


        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def NUMERO(self):
            return self.getToken(LenguajeMomoXDParser.NUMERO, 0)

        def CADENA(self):
            return self.getToken(LenguajeMomoXDParser.CADENA, 0)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LenguajeMomoXDParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_factor)
        try:
            self.state = 237
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 229
                self.match(LenguajeMomoXDParser.PAREN_IZQ)
                self.state = 230
                self.expresionAritmetica()
                self.state = 231
                self.match(LenguajeMomoXDParser.PAREN_DER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.llamadaFuncion()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(LenguajeMomoXDParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(LenguajeMomoXDParser.NUMERO)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(LenguajeMomoXDParser.CADENA)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LlamadaFuncionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcionNombre(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.FuncionNombreContext,0)


        def PAREN_IZQ(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(LenguajeMomoXDParser.PAREN_DER, 0)

        def listaArgumentos(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.ListaArgumentosContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_llamadaFuncion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLlamadaFuncion" ):
                listener.enterLlamadaFuncion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLlamadaFuncion" ):
                listener.exitLlamadaFuncion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLlamadaFuncion" ):
                return visitor.visitLlamadaFuncion(self)
            else:
                return visitor.visitChildren(self)




    def llamadaFuncion(self):

        localctx = LenguajeMomoXDParser.LlamadaFuncionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_llamadaFuncion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            self.funcionNombre()
            self.state = 240
            self.match(LenguajeMomoXDParser.PAREN_IZQ)
            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 30)) & ~0x3f) == 0 and ((1 << (_la - 30)) & 985164565987327) != 0):
                self.state = 241
                self.listaArgumentos()


            self.state = 244
            self.match(LenguajeMomoXDParser.PAREN_DER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionNombreContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeMomoXDParser.ID, 0)

        def funcionAgg(self):
            return self.getTypedRuleContext(LenguajeMomoXDParser.FuncionAggContext,0)


        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_funcionNombre

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuncionNombre" ):
                listener.enterFuncionNombre(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuncionNombre" ):
                listener.exitFuncionNombre(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionNombre" ):
                return visitor.visitFuncionNombre(self)
            else:
                return visitor.visitChildren(self)




    def funcionNombre(self):

        localctx = LenguajeMomoXDParser.FuncionNombreContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_funcionNombre)
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [77]:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.match(LenguajeMomoXDParser.ID)
                pass
            elif token in [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43]:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.funcionAgg()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaArgumentosContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeMomoXDParser.ExpresionAritmeticaContext)
            else:
                return self.getTypedRuleContext(LenguajeMomoXDParser.ExpresionAritmeticaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.COMA)
            else:
                return self.getToken(LenguajeMomoXDParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_listaArgumentos

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaArgumentos" ):
                listener.enterListaArgumentos(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaArgumentos" ):
                listener.exitListaArgumentos(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaArgumentos" ):
                return visitor.visitListaArgumentos(self)
            else:
                return visitor.visitChildren(self)




    def listaArgumentos(self):

        localctx = LenguajeMomoXDParser.ListaArgumentosContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_listaArgumentos)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expresionAritmetica()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==59:
                self.state = 251
                self.match(LenguajeMomoXDParser.COMA)
                self.state = 252
                self.expresionAritmetica()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaIDsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCH_IZQ(self):
            return self.getToken(LenguajeMomoXDParser.CORCH_IZQ, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.ID)
            else:
                return self.getToken(LenguajeMomoXDParser.ID, i)

        def CORCH_DER(self):
            return self.getToken(LenguajeMomoXDParser.CORCH_DER, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeMomoXDParser.COMA)
            else:
                return self.getToken(LenguajeMomoXDParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeMomoXDParser.RULE_listaIDs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaIDs" ):
                listener.enterListaIDs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaIDs" ):
                listener.exitListaIDs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListaIDs" ):
                return visitor.visitListaIDs(self)
            else:
                return visitor.visitChildren(self)




    def listaIDs(self):

        localctx = LenguajeMomoXDParser.ListaIDsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_listaIDs)
        self._la = 0 # Token type
        try:
            self.state = 269
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [63]:
                self.enterOuterAlt(localctx, 1)
                self.state = 258
                self.match(LenguajeMomoXDParser.CORCH_IZQ)
                self.state = 259
                self.match(LenguajeMomoXDParser.ID)
                self.state = 264
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==59:
                    self.state = 260
                    self.match(LenguajeMomoXDParser.COMA)
                    self.state = 261
                    self.match(LenguajeMomoXDParser.ID)
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 267
                self.match(LenguajeMomoXDParser.CORCH_DER)
                pass
            elif token in [77]:
                self.enterOuterAlt(localctx, 2)
                self.state = 268
                self.match(LenguajeMomoXDParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





