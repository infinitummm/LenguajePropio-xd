# Generated from grammar/LenguajeDatos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LenguajeDatosParser import LenguajeDatosParser
else:
    from LenguajeDatosParser import LenguajeDatosParser

# This class defines a complete generic visitor for a parse tree produced by LenguajeDatosParser.

class LenguajeDatosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LenguajeDatosParser#programa.
    def visitPrograma(self, ctx:LenguajeDatosParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#sentencia.
    def visitSentencia(self, ctx:LenguajeDatosParser.SentenciaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#asignacion.
    def visitAsignacion(self, ctx:LenguajeDatosParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#expresionPipeline.
    def visitExpresionPipeline(self, ctx:LenguajeDatosParser.ExpresionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#expresionBase.
    def visitExpresionBase(self, ctx:LenguajeDatosParser.ExpresionBaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#instruccionCarga.
    def visitInstruccionCarga(self, ctx:LenguajeDatosParser.InstruccionCargaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#instruccionGuardado.
    def visitInstruccionGuardado(self, ctx:LenguajeDatosParser.InstruccionGuardadoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionPipeline.
    def visitOperacionPipeline(self, ctx:LenguajeDatosParser.OperacionPipelineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionSeleccionar.
    def visitOperacionSeleccionar(self, ctx:LenguajeDatosParser.OperacionSeleccionarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionFiltrar.
    def visitOperacionFiltrar(self, ctx:LenguajeDatosParser.OperacionFiltrarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionOrdenar.
    def visitOperacionOrdenar(self, ctx:LenguajeDatosParser.OperacionOrdenarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionCrearColumna.
    def visitOperacionCrearColumna(self, ctx:LenguajeDatosParser.OperacionCrearColumnaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionAgrupar.
    def visitOperacionAgrupar(self, ctx:LenguajeDatosParser.OperacionAgruparContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#operacionResumir.
    def visitOperacionResumir(self, ctx:LenguajeDatosParser.OperacionResumirContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#listaAgregaciones.
    def visitListaAgregaciones(self, ctx:LenguajeDatosParser.ListaAgregacionesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#agregacion.
    def visitAgregacion(self, ctx:LenguajeDatosParser.AgregacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#instruccionVisualizacion.
    def visitInstruccionVisualizacion(self, ctx:LenguajeDatosParser.InstruccionVisualizacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#tipoGrafico.
    def visitTipoGrafico(self, ctx:LenguajeDatosParser.TipoGraficoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#expresionBooleana.
    def visitExpresionBooleana(self, ctx:LenguajeDatosParser.ExpresionBooleanaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#opRelacional.
    def visitOpRelacional(self, ctx:LenguajeDatosParser.OpRelacionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#expresionAritmetica.
    def visitExpresionAritmetica(self, ctx:LenguajeDatosParser.ExpresionAritmeticaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#termino.
    def visitTermino(self, ctx:LenguajeDatosParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#factor.
    def visitFactor(self, ctx:LenguajeDatosParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LenguajeDatosParser#listaIDs.
    def visitListaIDs(self, ctx:LenguajeDatosParser.ListaIDsContext):
        return self.visitChildren(ctx)



del LenguajeDatosParser