# Generated from grammar/LenguajeDatos.g4 by ANTLR 4.13.2
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
        4,1,45,204,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,3,1,60,8,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,5,3,
        69,8,3,10,3,12,3,72,9,3,1,4,1,4,1,4,1,4,3,4,78,8,4,1,5,1,5,1,5,1,
        5,3,5,84,8,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,3,7,96,8,7,
        1,8,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,3,10,107,8,10,1,11,1,11,1,
        11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,5,14,123,
        8,14,10,14,12,14,126,9,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,3,15,139,8,15,1,16,1,16,1,16,1,16,3,16,145,8,16,1,
        16,1,16,3,16,149,8,16,1,16,1,16,3,16,153,8,16,1,16,1,16,3,16,157,
        8,16,1,17,1,17,1,18,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,20,5,20,
        170,8,20,10,20,12,20,173,9,20,1,21,1,21,1,21,5,21,178,8,21,10,21,
        12,21,181,9,21,1,22,1,22,1,22,1,22,1,22,1,22,3,22,189,8,22,1,23,
        1,23,1,23,1,23,5,23,195,8,23,10,23,12,23,198,9,23,1,23,1,23,3,23,
        202,8,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,0,5,1,0,16,17,1,0,10,14,1,0,35,40,1,0,30,
        31,1,0,32,34,205,0,51,1,0,0,0,2,59,1,0,0,0,4,61,1,0,0,0,6,65,1,0,
        0,0,8,77,1,0,0,0,10,79,1,0,0,0,12,85,1,0,0,0,14,95,1,0,0,0,16,97,
        1,0,0,0,18,100,1,0,0,0,20,103,1,0,0,0,22,108,1,0,0,0,24,113,1,0,
        0,0,26,116,1,0,0,0,28,119,1,0,0,0,30,138,1,0,0,0,32,140,1,0,0,0,
        34,158,1,0,0,0,36,160,1,0,0,0,38,164,1,0,0,0,40,166,1,0,0,0,42,174,
        1,0,0,0,44,188,1,0,0,0,46,201,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,
        0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,
        1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,60,3,4,2,0,57,60,3,12,6,0,
        58,60,3,32,16,0,59,56,1,0,0,0,59,57,1,0,0,0,59,58,1,0,0,0,60,3,1,
        0,0,0,61,62,5,41,0,0,62,63,5,1,0,0,63,64,3,6,3,0,64,5,1,0,0,0,65,
        70,3,8,4,0,66,67,5,23,0,0,67,69,3,14,7,0,68,66,1,0,0,0,69,72,1,0,
        0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,7,1,0,0,0,72,70,1,0,0,0,73,78,
        3,10,5,0,74,78,5,41,0,0,75,78,5,43,0,0,76,78,5,42,0,0,77,73,1,0,
        0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,9,1,0,0,0,79,80,
        5,2,0,0,80,83,5,43,0,0,81,82,5,18,0,0,82,84,5,43,0,0,83,81,1,0,0,
        0,83,84,1,0,0,0,84,11,1,0,0,0,85,86,5,3,0,0,86,87,5,41,0,0,87,88,
        5,43,0,0,88,13,1,0,0,0,89,96,3,16,8,0,90,96,3,18,9,0,91,96,3,20,
        10,0,92,96,3,22,11,0,93,96,3,24,12,0,94,96,3,26,13,0,95,89,1,0,0,
        0,95,90,1,0,0,0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,
        1,0,0,0,96,15,1,0,0,0,97,98,5,4,0,0,98,99,3,46,23,0,99,17,1,0,0,
        0,100,101,5,5,0,0,101,102,3,36,18,0,102,19,1,0,0,0,103,104,5,6,0,
        0,104,106,5,41,0,0,105,107,7,0,0,0,106,105,1,0,0,0,106,107,1,0,0,
        0,107,21,1,0,0,0,108,109,5,7,0,0,109,110,5,41,0,0,110,111,5,1,0,
        0,111,112,3,40,20,0,112,23,1,0,0,0,113,114,5,8,0,0,114,115,3,46,
        23,0,115,25,1,0,0,0,116,117,5,9,0,0,117,118,3,28,14,0,118,27,1,0,
        0,0,119,124,3,30,15,0,120,121,5,24,0,0,121,123,3,30,15,0,122,120,
        1,0,0,0,123,126,1,0,0,0,124,122,1,0,0,0,124,125,1,0,0,0,125,29,1,
        0,0,0,126,124,1,0,0,0,127,128,5,41,0,0,128,129,5,1,0,0,129,130,5,
        15,0,0,130,131,5,26,0,0,131,132,5,41,0,0,132,139,5,27,0,0,133,134,
        5,41,0,0,134,135,5,1,0,0,135,136,5,15,0,0,136,137,5,26,0,0,137,139,
        5,27,0,0,138,127,1,0,0,0,138,133,1,0,0,0,139,31,1,0,0,0,140,141,
        3,34,17,0,141,144,5,41,0,0,142,143,5,19,0,0,143,145,5,43,0,0,144,
        142,1,0,0,0,144,145,1,0,0,0,145,148,1,0,0,0,146,147,5,20,0,0,147,
        149,5,43,0,0,148,146,1,0,0,0,148,149,1,0,0,0,149,152,1,0,0,0,150,
        151,5,21,0,0,151,153,5,43,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,
        156,1,0,0,0,154,155,5,22,0,0,155,157,5,43,0,0,156,154,1,0,0,0,156,
        157,1,0,0,0,157,33,1,0,0,0,158,159,7,1,0,0,159,35,1,0,0,0,160,161,
        3,40,20,0,161,162,3,38,19,0,162,163,3,40,20,0,163,37,1,0,0,0,164,
        165,7,2,0,0,165,39,1,0,0,0,166,171,3,42,21,0,167,168,7,3,0,0,168,
        170,3,42,21,0,169,167,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,
        172,1,0,0,0,172,41,1,0,0,0,173,171,1,0,0,0,174,179,3,44,22,0,175,
        176,7,4,0,0,176,178,3,44,22,0,177,175,1,0,0,0,178,181,1,0,0,0,179,
        177,1,0,0,0,179,180,1,0,0,0,180,43,1,0,0,0,181,179,1,0,0,0,182,183,
        5,26,0,0,183,184,3,40,20,0,184,185,5,27,0,0,185,189,1,0,0,0,186,
        189,5,41,0,0,187,189,5,42,0,0,188,182,1,0,0,0,188,186,1,0,0,0,188,
        187,1,0,0,0,189,45,1,0,0,0,190,191,5,28,0,0,191,196,5,41,0,0,192,
        193,5,24,0,0,193,195,5,41,0,0,194,192,1,0,0,0,195,198,1,0,0,0,196,
        194,1,0,0,0,196,197,1,0,0,0,197,199,1,0,0,0,198,196,1,0,0,0,199,
        202,5,29,0,0,200,202,5,41,0,0,201,190,1,0,0,0,201,200,1,0,0,0,202,
        47,1,0,0,0,18,51,59,70,77,83,95,106,124,138,144,148,152,156,171,
        179,188,196,201
    ]

class LenguajeDatosParser ( Parser ):

    grammarFileName = "LenguajeDatos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'cargar_csv_xd'", "'guardar_csv_xd'", 
                     "'seleccionar_xd'", "'filtrar_xd'", "'ordenar_por_xd'", 
                     "'crear_columna_xd'", "'agrupar_por_xd'", "'resumir_xd'", 
                     "'graficar_barras_xd'", "'graficar_lineas_xd'", "'graficar_histograma_xd'", 
                     "'graficar_dispersion_xd'", "'graficar_cajas_xd'", 
                     "<INVALID>", "'ascendente'", "'descendente'", "'separador'", 
                     "'titulo'", "'eje_x'", "'eje_y'", "'guardar'", "'|>'", 
                     "','", "':'", "'('", "')'", "'['", "']'", "'+'", "'-'", 
                     "'*'", "'/'", "'%'", "'>='", "'<='", "'=='", "'!='", 
                     "'>'", "'<'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "CARGAR_CSV_XD", "GUARDAR_CSV_XD", 
                      "SELECCIONAR_XD", "FILTRAR_XD", "ORDENAR_POR_XD", 
                      "CREAR_COLUMNA_XD", "AGRUPAR_POR_XD", "RESUMIR_XD", 
                      "GRAFICAR_BARRAS_XD", "GRAFICAR_LINEAS_XD", "GRAFICAR_HISTOGRAMA_XD", 
                      "GRAFICAR_DISPERSION_XD", "GRAFICAR_CAJAS_XD", "FUNCION_AGG", 
                      "ASCENDENTE", "DESCENDENTE", "SEPARADOR", "TITULO", 
                      "EJE_X", "EJE_Y", "GUARDAR", "PIPE", "COMA", "DOS_PUNTOS", 
                      "PAREN_IZQ", "PAREN_DER", "CORCH_IZQ", "CORCH_DER", 
                      "MAS", "MENOS", "MULT", "DIV", "MOD", "MAYOR_IGUAL", 
                      "MENOR_IGUAL", "IGUAL_IGUAL", "DIFERENTE", "MAYOR", 
                      "MENOR", "ID", "NUMERO", "CADENA", "COMENTARIO", "WS" ]

    RULE_programa = 0
    RULE_sentencia = 1
    RULE_asignacion = 2
    RULE_expresionPipeline = 3
    RULE_expresionBase = 4
    RULE_instruccionCarga = 5
    RULE_instruccionGuardado = 6
    RULE_operacionPipeline = 7
    RULE_operacionSeleccionar = 8
    RULE_operacionFiltrar = 9
    RULE_operacionOrdenar = 10
    RULE_operacionCrearColumna = 11
    RULE_operacionAgrupar = 12
    RULE_operacionResumir = 13
    RULE_listaAgregaciones = 14
    RULE_agregacion = 15
    RULE_instruccionVisualizacion = 16
    RULE_tipoGrafico = 17
    RULE_expresionBooleana = 18
    RULE_opRelacional = 19
    RULE_expresionAritmetica = 20
    RULE_termino = 21
    RULE_factor = 22
    RULE_listaIDs = 23

    ruleNames =  [ "programa", "sentencia", "asignacion", "expresionPipeline", 
                   "expresionBase", "instruccionCarga", "instruccionGuardado", 
                   "operacionPipeline", "operacionSeleccionar", "operacionFiltrar", 
                   "operacionOrdenar", "operacionCrearColumna", "operacionAgrupar", 
                   "operacionResumir", "listaAgregaciones", "agregacion", 
                   "instruccionVisualizacion", "tipoGrafico", "expresionBooleana", 
                   "opRelacional", "expresionAritmetica", "termino", "factor", 
                   "listaIDs" ]

    EOF = Token.EOF
    T__0=1
    CARGAR_CSV_XD=2
    GUARDAR_CSV_XD=3
    SELECCIONAR_XD=4
    FILTRAR_XD=5
    ORDENAR_POR_XD=6
    CREAR_COLUMNA_XD=7
    AGRUPAR_POR_XD=8
    RESUMIR_XD=9
    GRAFICAR_BARRAS_XD=10
    GRAFICAR_LINEAS_XD=11
    GRAFICAR_HISTOGRAMA_XD=12
    GRAFICAR_DISPERSION_XD=13
    GRAFICAR_CAJAS_XD=14
    FUNCION_AGG=15
    ASCENDENTE=16
    DESCENDENTE=17
    SEPARADOR=18
    TITULO=19
    EJE_X=20
    EJE_Y=21
    GUARDAR=22
    PIPE=23
    COMA=24
    DOS_PUNTOS=25
    PAREN_IZQ=26
    PAREN_DER=27
    CORCH_IZQ=28
    CORCH_DER=29
    MAS=30
    MENOS=31
    MULT=32
    DIV=33
    MOD=34
    MAYOR_IGUAL=35
    MENOR_IGUAL=36
    IGUAL_IGUAL=37
    DIFERENTE=38
    MAYOR=39
    MENOR=40
    ID=41
    NUMERO=42
    CADENA=43
    COMENTARIO=44
    WS=45

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
            return self.getToken(LenguajeDatosParser.EOF, 0)

        def sentencia(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDatosParser.SentenciaContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.SentenciaContext,i)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_programa

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

        localctx = LenguajeDatosParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2199023287304) != 0):
                self.state = 48
                self.sentencia()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(LenguajeDatosParser.EOF)
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
            return self.getTypedRuleContext(LenguajeDatosParser.AsignacionContext,0)


        def instruccionGuardado(self):
            return self.getTypedRuleContext(LenguajeDatosParser.InstruccionGuardadoContext,0)


        def instruccionVisualizacion(self):
            return self.getTypedRuleContext(LenguajeDatosParser.InstruccionVisualizacionContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_sentencia

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

        localctx = LenguajeDatosParser.SentenciaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_sentencia)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [41]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.asignacion()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.instruccionGuardado()
                pass
            elif token in [10, 11, 12, 13, 14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.instruccionVisualizacion()
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


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def expresionPipeline(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ExpresionPipelineContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_asignacion

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

        localctx = LenguajeDatosParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(LenguajeDatosParser.ID)
            self.state = 62
            self.match(LenguajeDatosParser.T__0)
            self.state = 63
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
            return self.getTypedRuleContext(LenguajeDatosParser.ExpresionBaseContext,0)


        def PIPE(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.PIPE)
            else:
                return self.getToken(LenguajeDatosParser.PIPE, i)

        def operacionPipeline(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDatosParser.OperacionPipelineContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.OperacionPipelineContext,i)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_expresionPipeline

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

        localctx = LenguajeDatosParser.ExpresionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expresionPipeline)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self.expresionBase()
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 66
                self.match(LenguajeDatosParser.PIPE)
                self.state = 67
                self.operacionPipeline()
                self.state = 72
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
            return self.getTypedRuleContext(LenguajeDatosParser.InstruccionCargaContext,0)


        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def CADENA(self):
            return self.getToken(LenguajeDatosParser.CADENA, 0)

        def NUMERO(self):
            return self.getToken(LenguajeDatosParser.NUMERO, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_expresionBase

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

        localctx = LenguajeDatosParser.ExpresionBaseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expresionBase)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 73
                self.instruccionCarga()
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 74
                self.match(LenguajeDatosParser.ID)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 3)
                self.state = 75
                self.match(LenguajeDatosParser.CADENA)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 76
                self.match(LenguajeDatosParser.NUMERO)
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

        def CARGAR_CSV_XD(self):
            return self.getToken(LenguajeDatosParser.CARGAR_CSV_XD, 0)

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.CADENA)
            else:
                return self.getToken(LenguajeDatosParser.CADENA, i)

        def SEPARADOR(self):
            return self.getToken(LenguajeDatosParser.SEPARADOR, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_instruccionCarga

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

        localctx = LenguajeDatosParser.InstruccionCargaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_instruccionCarga)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(LenguajeDatosParser.CARGAR_CSV_XD)
            self.state = 80
            self.match(LenguajeDatosParser.CADENA)
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 81
                self.match(LenguajeDatosParser.SEPARADOR)
                self.state = 82
                self.match(LenguajeDatosParser.CADENA)


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

        def GUARDAR_CSV_XD(self):
            return self.getToken(LenguajeDatosParser.GUARDAR_CSV_XD, 0)

        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def CADENA(self):
            return self.getToken(LenguajeDatosParser.CADENA, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_instruccionGuardado

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

        localctx = LenguajeDatosParser.InstruccionGuardadoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_instruccionGuardado)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(LenguajeDatosParser.GUARDAR_CSV_XD)
            self.state = 86
            self.match(LenguajeDatosParser.ID)
            self.state = 87
            self.match(LenguajeDatosParser.CADENA)
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
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionSeleccionarContext,0)


        def operacionFiltrar(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionFiltrarContext,0)


        def operacionOrdenar(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionOrdenarContext,0)


        def operacionCrearColumna(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionCrearColumnaContext,0)


        def operacionAgrupar(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionAgruparContext,0)


        def operacionResumir(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OperacionResumirContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionPipeline

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

        localctx = LenguajeDatosParser.OperacionPipelineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operacionPipeline)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.operacionSeleccionar()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 90
                self.operacionFiltrar()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 91
                self.operacionOrdenar()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 4)
                self.state = 92
                self.operacionCrearColumna()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 5)
                self.state = 93
                self.operacionAgrupar()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 6)
                self.state = 94
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

        def SELECCIONAR_XD(self):
            return self.getToken(LenguajeDatosParser.SELECCIONAR_XD, 0)

        def listaIDs(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ListaIDsContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionSeleccionar

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

        localctx = LenguajeDatosParser.OperacionSeleccionarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_operacionSeleccionar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(LenguajeDatosParser.SELECCIONAR_XD)
            self.state = 98
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

        def FILTRAR_XD(self):
            return self.getToken(LenguajeDatosParser.FILTRAR_XD, 0)

        def expresionBooleana(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ExpresionBooleanaContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionFiltrar

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

        localctx = LenguajeDatosParser.OperacionFiltrarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_operacionFiltrar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(LenguajeDatosParser.FILTRAR_XD)
            self.state = 101
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

        def ORDENAR_POR_XD(self):
            return self.getToken(LenguajeDatosParser.ORDENAR_POR_XD, 0)

        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def ASCENDENTE(self):
            return self.getToken(LenguajeDatosParser.ASCENDENTE, 0)

        def DESCENDENTE(self):
            return self.getToken(LenguajeDatosParser.DESCENDENTE, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionOrdenar

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

        localctx = LenguajeDatosParser.OperacionOrdenarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_operacionOrdenar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(LenguajeDatosParser.ORDENAR_POR_XD)
            self.state = 104
            self.match(LenguajeDatosParser.ID)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16 or _la==17:
                self.state = 105
                _la = self._input.LA(1)
                if not(_la==16 or _la==17):
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

        def CREAR_COLUMNA_XD(self):
            return self.getToken(LenguajeDatosParser.CREAR_COLUMNA_XD, 0)

        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ExpresionAritmeticaContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionCrearColumna

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

        localctx = LenguajeDatosParser.OperacionCrearColumnaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_operacionCrearColumna)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 108
            self.match(LenguajeDatosParser.CREAR_COLUMNA_XD)
            self.state = 109
            self.match(LenguajeDatosParser.ID)
            self.state = 110
            self.match(LenguajeDatosParser.T__0)
            self.state = 111
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

        def AGRUPAR_POR_XD(self):
            return self.getToken(LenguajeDatosParser.AGRUPAR_POR_XD, 0)

        def listaIDs(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ListaIDsContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionAgrupar

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

        localctx = LenguajeDatosParser.OperacionAgruparContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_operacionAgrupar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(LenguajeDatosParser.AGRUPAR_POR_XD)
            self.state = 114
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

        def RESUMIR_XD(self):
            return self.getToken(LenguajeDatosParser.RESUMIR_XD, 0)

        def listaAgregaciones(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ListaAgregacionesContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_operacionResumir

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

        localctx = LenguajeDatosParser.OperacionResumirContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_operacionResumir)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(LenguajeDatosParser.RESUMIR_XD)
            self.state = 117
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
                return self.getTypedRuleContexts(LenguajeDatosParser.AgregacionContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.AgregacionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.COMA)
            else:
                return self.getToken(LenguajeDatosParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_listaAgregaciones

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

        localctx = LenguajeDatosParser.ListaAgregacionesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_listaAgregaciones)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.agregacion()
            self.state = 124
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24:
                self.state = 120
                self.match(LenguajeDatosParser.COMA)
                self.state = 121
                self.agregacion()
                self.state = 126
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
                return self.getTokens(LenguajeDatosParser.ID)
            else:
                return self.getToken(LenguajeDatosParser.ID, i)

        def FUNCION_AGG(self):
            return self.getToken(LenguajeDatosParser.FUNCION_AGG, 0)

        def PAREN_IZQ(self):
            return self.getToken(LenguajeDatosParser.PAREN_IZQ, 0)

        def PAREN_DER(self):
            return self.getToken(LenguajeDatosParser.PAREN_DER, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_agregacion

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

        localctx = LenguajeDatosParser.AgregacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_agregacion)
        try:
            self.state = 138
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.match(LenguajeDatosParser.ID)
                self.state = 128
                self.match(LenguajeDatosParser.T__0)
                self.state = 129
                self.match(LenguajeDatosParser.FUNCION_AGG)
                self.state = 130
                self.match(LenguajeDatosParser.PAREN_IZQ)
                self.state = 131
                self.match(LenguajeDatosParser.ID)
                self.state = 132
                self.match(LenguajeDatosParser.PAREN_DER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 133
                self.match(LenguajeDatosParser.ID)
                self.state = 134
                self.match(LenguajeDatosParser.T__0)
                self.state = 135
                self.match(LenguajeDatosParser.FUNCION_AGG)
                self.state = 136
                self.match(LenguajeDatosParser.PAREN_IZQ)
                self.state = 137
                self.match(LenguajeDatosParser.PAREN_DER)
                pass


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
            return self.getTypedRuleContext(LenguajeDatosParser.TipoGraficoContext,0)


        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def TITULO(self):
            return self.getToken(LenguajeDatosParser.TITULO, 0)

        def CADENA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.CADENA)
            else:
                return self.getToken(LenguajeDatosParser.CADENA, i)

        def EJE_X(self):
            return self.getToken(LenguajeDatosParser.EJE_X, 0)

        def EJE_Y(self):
            return self.getToken(LenguajeDatosParser.EJE_Y, 0)

        def GUARDAR(self):
            return self.getToken(LenguajeDatosParser.GUARDAR, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_instruccionVisualizacion

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

        localctx = LenguajeDatosParser.InstruccionVisualizacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_instruccionVisualizacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.tipoGrafico()
            self.state = 141
            self.match(LenguajeDatosParser.ID)
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==19:
                self.state = 142
                self.match(LenguajeDatosParser.TITULO)
                self.state = 143
                self.match(LenguajeDatosParser.CADENA)


            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==20:
                self.state = 146
                self.match(LenguajeDatosParser.EJE_X)
                self.state = 147
                self.match(LenguajeDatosParser.CADENA)


            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==21:
                self.state = 150
                self.match(LenguajeDatosParser.EJE_Y)
                self.state = 151
                self.match(LenguajeDatosParser.CADENA)


            self.state = 156
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 154
                self.match(LenguajeDatosParser.GUARDAR)
                self.state = 155
                self.match(LenguajeDatosParser.CADENA)


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

        def GRAFICAR_BARRAS_XD(self):
            return self.getToken(LenguajeDatosParser.GRAFICAR_BARRAS_XD, 0)

        def GRAFICAR_LINEAS_XD(self):
            return self.getToken(LenguajeDatosParser.GRAFICAR_LINEAS_XD, 0)

        def GRAFICAR_HISTOGRAMA_XD(self):
            return self.getToken(LenguajeDatosParser.GRAFICAR_HISTOGRAMA_XD, 0)

        def GRAFICAR_DISPERSION_XD(self):
            return self.getToken(LenguajeDatosParser.GRAFICAR_DISPERSION_XD, 0)

        def GRAFICAR_CAJAS_XD(self):
            return self.getToken(LenguajeDatosParser.GRAFICAR_CAJAS_XD, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_tipoGrafico

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

        localctx = LenguajeDatosParser.TipoGraficoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_tipoGrafico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31744) != 0)):
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


    class ExpresionBooleanaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresionAritmetica(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LenguajeDatosParser.ExpresionAritmeticaContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.ExpresionAritmeticaContext,i)


        def opRelacional(self):
            return self.getTypedRuleContext(LenguajeDatosParser.OpRelacionalContext,0)


        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_expresionBooleana

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

        localctx = LenguajeDatosParser.ExpresionBooleanaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expresionBooleana)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.expresionAritmetica()
            self.state = 161
            self.opRelacional()
            self.state = 162
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
            return self.getToken(LenguajeDatosParser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(LenguajeDatosParser.MENOR_IGUAL, 0)

        def IGUAL_IGUAL(self):
            return self.getToken(LenguajeDatosParser.IGUAL_IGUAL, 0)

        def DIFERENTE(self):
            return self.getToken(LenguajeDatosParser.DIFERENTE, 0)

        def MAYOR(self):
            return self.getToken(LenguajeDatosParser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(LenguajeDatosParser.MENOR, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_opRelacional

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

        localctx = LenguajeDatosParser.OpRelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_opRelacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2164663517184) != 0)):
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
                return self.getTypedRuleContexts(LenguajeDatosParser.TerminoContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.TerminoContext,i)


        def MAS(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.MAS)
            else:
                return self.getToken(LenguajeDatosParser.MAS, i)

        def MENOS(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.MENOS)
            else:
                return self.getToken(LenguajeDatosParser.MENOS, i)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_expresionAritmetica

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

        localctx = LenguajeDatosParser.ExpresionAritmeticaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expresionAritmetica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.termino()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 167
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 168
                self.termino()
                self.state = 173
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
                return self.getTypedRuleContexts(LenguajeDatosParser.FactorContext)
            else:
                return self.getTypedRuleContext(LenguajeDatosParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.MULT)
            else:
                return self.getToken(LenguajeDatosParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.DIV)
            else:
                return self.getToken(LenguajeDatosParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.MOD)
            else:
                return self.getToken(LenguajeDatosParser.MOD, i)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_termino

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

        localctx = LenguajeDatosParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.factor()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0):
                self.state = 175
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 30064771072) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 176
                self.factor()
                self.state = 181
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
            return self.getToken(LenguajeDatosParser.PAREN_IZQ, 0)

        def expresionAritmetica(self):
            return self.getTypedRuleContext(LenguajeDatosParser.ExpresionAritmeticaContext,0)


        def PAREN_DER(self):
            return self.getToken(LenguajeDatosParser.PAREN_DER, 0)

        def ID(self):
            return self.getToken(LenguajeDatosParser.ID, 0)

        def NUMERO(self):
            return self.getToken(LenguajeDatosParser.NUMERO, 0)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_factor

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

        localctx = LenguajeDatosParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_factor)
        try:
            self.state = 188
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [26]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.match(LenguajeDatosParser.PAREN_IZQ)
                self.state = 183
                self.expresionAritmetica()
                self.state = 184
                self.match(LenguajeDatosParser.PAREN_DER)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.match(LenguajeDatosParser.ID)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 3)
                self.state = 187
                self.match(LenguajeDatosParser.NUMERO)
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


    class ListaIDsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CORCH_IZQ(self):
            return self.getToken(LenguajeDatosParser.CORCH_IZQ, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.ID)
            else:
                return self.getToken(LenguajeDatosParser.ID, i)

        def CORCH_DER(self):
            return self.getToken(LenguajeDatosParser.CORCH_DER, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(LenguajeDatosParser.COMA)
            else:
                return self.getToken(LenguajeDatosParser.COMA, i)

        def getRuleIndex(self):
            return LenguajeDatosParser.RULE_listaIDs

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

        localctx = LenguajeDatosParser.ListaIDsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_listaIDs)
        self._la = 0 # Token type
        try:
            self.state = 201
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 190
                self.match(LenguajeDatosParser.CORCH_IZQ)
                self.state = 191
                self.match(LenguajeDatosParser.ID)
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 192
                    self.match(LenguajeDatosParser.COMA)
                    self.state = 193
                    self.match(LenguajeDatosParser.ID)
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 199
                self.match(LenguajeDatosParser.CORCH_DER)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 2)
                self.state = 200
                self.match(LenguajeDatosParser.ID)
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





