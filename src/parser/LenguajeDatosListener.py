# Generated from grammar/LenguajeDatos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDatosParser import LenguajeDatosParser
else:
    from LenguajeDatosParser import LenguajeDatosParser

# This class defines a complete listener for a parse tree produced by LenguajeDatosParser.
class LenguajeDatosListener(ParseTreeListener):

    # Enter a parse tree produced by LenguajeDatosParser#programa.
    def enterPrograma(self, ctx:LenguajeDatosParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#programa.
    def exitPrograma(self, ctx:LenguajeDatosParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#sentencia.
    def enterSentencia(self, ctx:LenguajeDatosParser.SentenciaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#sentencia.
    def exitSentencia(self, ctx:LenguajeDatosParser.SentenciaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#asignacion.
    def enterAsignacion(self, ctx:LenguajeDatosParser.AsignacionContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#asignacion.
    def exitAsignacion(self, ctx:LenguajeDatosParser.AsignacionContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#expresionPipeline.
    def enterExpresionPipeline(self, ctx:LenguajeDatosParser.ExpresionPipelineContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#expresionPipeline.
    def exitExpresionPipeline(self, ctx:LenguajeDatosParser.ExpresionPipelineContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#expresionBase.
    def enterExpresionBase(self, ctx:LenguajeDatosParser.ExpresionBaseContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#expresionBase.
    def exitExpresionBase(self, ctx:LenguajeDatosParser.ExpresionBaseContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#instruccionCarga.
    def enterInstruccionCarga(self, ctx:LenguajeDatosParser.InstruccionCargaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#instruccionCarga.
    def exitInstruccionCarga(self, ctx:LenguajeDatosParser.InstruccionCargaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#instruccionGuardado.
    def enterInstruccionGuardado(self, ctx:LenguajeDatosParser.InstruccionGuardadoContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#instruccionGuardado.
    def exitInstruccionGuardado(self, ctx:LenguajeDatosParser.InstruccionGuardadoContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionPipeline.
    def enterOperacionPipeline(self, ctx:LenguajeDatosParser.OperacionPipelineContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionPipeline.
    def exitOperacionPipeline(self, ctx:LenguajeDatosParser.OperacionPipelineContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionSeleccionar.
    def enterOperacionSeleccionar(self, ctx:LenguajeDatosParser.OperacionSeleccionarContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionSeleccionar.
    def exitOperacionSeleccionar(self, ctx:LenguajeDatosParser.OperacionSeleccionarContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionFiltrar.
    def enterOperacionFiltrar(self, ctx:LenguajeDatosParser.OperacionFiltrarContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionFiltrar.
    def exitOperacionFiltrar(self, ctx:LenguajeDatosParser.OperacionFiltrarContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionOrdenar.
    def enterOperacionOrdenar(self, ctx:LenguajeDatosParser.OperacionOrdenarContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionOrdenar.
    def exitOperacionOrdenar(self, ctx:LenguajeDatosParser.OperacionOrdenarContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionCrearColumna.
    def enterOperacionCrearColumna(self, ctx:LenguajeDatosParser.OperacionCrearColumnaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionCrearColumna.
    def exitOperacionCrearColumna(self, ctx:LenguajeDatosParser.OperacionCrearColumnaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionAgrupar.
    def enterOperacionAgrupar(self, ctx:LenguajeDatosParser.OperacionAgruparContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionAgrupar.
    def exitOperacionAgrupar(self, ctx:LenguajeDatosParser.OperacionAgruparContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#operacionResumir.
    def enterOperacionResumir(self, ctx:LenguajeDatosParser.OperacionResumirContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#operacionResumir.
    def exitOperacionResumir(self, ctx:LenguajeDatosParser.OperacionResumirContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#listaAgregaciones.
    def enterListaAgregaciones(self, ctx:LenguajeDatosParser.ListaAgregacionesContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#listaAgregaciones.
    def exitListaAgregaciones(self, ctx:LenguajeDatosParser.ListaAgregacionesContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#agregacion.
    def enterAgregacion(self, ctx:LenguajeDatosParser.AgregacionContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#agregacion.
    def exitAgregacion(self, ctx:LenguajeDatosParser.AgregacionContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#instruccionVisualizacion.
    def enterInstruccionVisualizacion(self, ctx:LenguajeDatosParser.InstruccionVisualizacionContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#instruccionVisualizacion.
    def exitInstruccionVisualizacion(self, ctx:LenguajeDatosParser.InstruccionVisualizacionContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#tipoGrafico.
    def enterTipoGrafico(self, ctx:LenguajeDatosParser.TipoGraficoContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#tipoGrafico.
    def exitTipoGrafico(self, ctx:LenguajeDatosParser.TipoGraficoContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#expresionBooleana.
    def enterExpresionBooleana(self, ctx:LenguajeDatosParser.ExpresionBooleanaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#expresionBooleana.
    def exitExpresionBooleana(self, ctx:LenguajeDatosParser.ExpresionBooleanaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#opRelacional.
    def enterOpRelacional(self, ctx:LenguajeDatosParser.OpRelacionalContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#opRelacional.
    def exitOpRelacional(self, ctx:LenguajeDatosParser.OpRelacionalContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#expresionAritmetica.
    def enterExpresionAritmetica(self, ctx:LenguajeDatosParser.ExpresionAritmeticaContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#expresionAritmetica.
    def exitExpresionAritmetica(self, ctx:LenguajeDatosParser.ExpresionAritmeticaContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#termino.
    def enterTermino(self, ctx:LenguajeDatosParser.TerminoContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#termino.
    def exitTermino(self, ctx:LenguajeDatosParser.TerminoContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#factor.
    def enterFactor(self, ctx:LenguajeDatosParser.FactorContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#factor.
    def exitFactor(self, ctx:LenguajeDatosParser.FactorContext):
        pass


    # Enter a parse tree produced by LenguajeDatosParser#listaIDs.
    def enterListaIDs(self, ctx:LenguajeDatosParser.ListaIDsContext):
        pass

    # Exit a parse tree produced by LenguajeDatosParser#listaIDs.
    def exitListaIDs(self, ctx:LenguajeDatosParser.ListaIDsContext):
        pass



del LenguajeDatosParser