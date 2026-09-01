# Generated from grammar/LenguajeMomoXD.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeMomoXDParser import LenguajeMomoXDParser
else:
    from LenguajeMomoXDParser import LenguajeMomoXDParser

# This class defines a complete generic visitor for a parse tree produced by LenguajeMomoXDParser.

class LenguajeMomoXDVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeMomoXDParser#programa.
    def visitPrograma(self, ctx:LenguajeMomoXDParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#sentencia.
    def visitSentencia(self, ctx:LenguajeMomoXDParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#asignacion.
    def visitAsignacion(self, ctx:LenguajeMomoXDParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#expresionPipeline.
    def visitExpresionPipeline(self, ctx:LenguajeMomoXDParser.ExpresionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#expresionBase.
    def visitExpresionBase(self, ctx:LenguajeMomoXDParser.ExpresionBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#instruccionCarga.
    def visitInstruccionCarga(self, ctx:LenguajeMomoXDParser.InstruccionCargaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#instruccionImprimir.
    def visitInstruccionImprimir(self, ctx:LenguajeMomoXDParser.InstruccionImprimirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#instruccionGuardado.
    def visitInstruccionGuardado(self, ctx:LenguajeMomoXDParser.InstruccionGuardadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionPipeline.
    def visitOperacionPipeline(self, ctx:LenguajeMomoXDParser.OperacionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionSeleccionar.
    def visitOperacionSeleccionar(self, ctx:LenguajeMomoXDParser.OperacionSeleccionarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionFiltrar.
    def visitOperacionFiltrar(self, ctx:LenguajeMomoXDParser.OperacionFiltrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionOrdenar.
    def visitOperacionOrdenar(self, ctx:LenguajeMomoXDParser.OperacionOrdenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionCrearColumna.
    def visitOperacionCrearColumna(self, ctx:LenguajeMomoXDParser.OperacionCrearColumnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionAgrupar.
    def visitOperacionAgrupar(self, ctx:LenguajeMomoXDParser.OperacionAgruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#operacionResumir.
    def visitOperacionResumir(self, ctx:LenguajeMomoXDParser.OperacionResumirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#listaAgregaciones.
    def visitListaAgregaciones(self, ctx:LenguajeMomoXDParser.ListaAgregacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#agregacion.
    def visitAgregacion(self, ctx:LenguajeMomoXDParser.AgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#funcionAgg.
    def visitFuncionAgg(self, ctx:LenguajeMomoXDParser.FuncionAggContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#instruccionVisualizacion.
    def visitInstruccionVisualizacion(self, ctx:LenguajeMomoXDParser.InstruccionVisualizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#tipoGrafico.
    def visitTipoGrafico(self, ctx:LenguajeMomoXDParser.TipoGraficoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#instruccionSi.
    def visitInstruccionSi(self, ctx:LenguajeMomoXDParser.InstruccionSiContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#bloque.
    def visitBloque(self, ctx:LenguajeMomoXDParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#expresionBooleana.
    def visitExpresionBooleana(self, ctx:LenguajeMomoXDParser.ExpresionBooleanaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#opRelacional.
    def visitOpRelacional(self, ctx:LenguajeMomoXDParser.OpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#expresionAritmetica.
    def visitExpresionAritmetica(self, ctx:LenguajeMomoXDParser.ExpresionAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#termino.
    def visitTermino(self, ctx:LenguajeMomoXDParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#factor.
    def visitFactor(self, ctx:LenguajeMomoXDParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeMomoXDParser#listaIDs.
    def visitListaIDs(self, ctx:LenguajeMomoXDParser.ListaIDsContext):
        return self.visitChildren(ctx)



del LenguajeMomoXDParser