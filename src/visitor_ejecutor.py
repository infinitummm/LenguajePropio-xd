"""
Visitor Evaluador y Ejecutor Semántico para el DSL LenguajeDatos xd
Conecta el Árbol Sintáctico (Parse Tree) de ANTLR4 con las 3 librerías propias en español.
"""
from src.parser.LenguajeDatosVisitor import LenguajeDatosVisitor
from src.core import cargar_csv_xd, guardar_csv_xd, crear_figura_xd

class EvaluadorDSLVisitor(LenguajeDatosVisitor):
    def __init__(self):
        super().__init__()
        self.entorno = {}

    def visitPrograma(self, ctx):
        for s_ctx in ctx.sentencia():
            self.visit(s_ctx)
        return self.entorno

    def visitAsignacion(self, ctx):
        nombre_var = ctx.ID().getText()
        valor = self.visit(ctx.expresionPipeline())
        self.entorno[nombre_var] = valor
        return valor

    def visitExpresionPipeline(self, ctx):
        actual = self.visit(ctx.expresionBase())
        for op_ctx in ctx.operacionPipeline():
            actual = self.aplicar_operacion_pipeline(actual, op_ctx)
        return actual

    def visitExpresionBase(self, ctx):
        if ctx.instruccionCarga():
            c_ctx = ctx.instruccionCarga()
            ruta = c_ctx.CADENA(0).getText().strip('"\'')
            return cargar_csv_xd(ruta)
        elif ctx.ID():
            nombre_var = ctx.ID().getText()
            if nombre_var in self.entorno:
                return self.entorno[nombre_var]
            raise NameError(f"La variable '{nombre_var}' no existe en el entorno xd.")
        elif ctx.CADENA():
            return ctx.CADENA().getText().strip('"\'')
        elif ctx.NUMERO():
            val = ctx.NUMERO().getText()
            return float(val) if '.' in val else int(val)

    def aplicar_operacion_pipeline(self, tabla, op_ctx):
        if op_ctx.operacionSeleccionar():
            cols = self.obtener_lista_ids(op_ctx.operacionSeleccionar().listaIDs())
            return tabla.seleccionar_xd(cols)
        elif op_ctx.operacionFiltrar():
            mascara = self.evaluar_expresion_booleana(tabla, op_ctx.operacionFiltrar().expresionBooleana())
            return tabla.filtrar_xd(mascara)
        elif op_ctx.operacionOrdenar():
            ord_ctx = op_ctx.operacionOrdenar()
            col = ord_ctx.ID().getText()
            asc = True
            if ord_ctx.DESCENDENTE():
                asc = False
            return tabla.ordenar_por_xd(col, ascendente=asc)
        elif op_ctx.operacionCrearColumna():
            c_ctx = op_ctx.operacionCrearColumna()
            nombre_col = c_ctx.ID().getText()
            valores = self.evaluar_expresion_aritmetica(tabla, c_ctx.expresionAritmetica())
            return tabla.crear_columna_xd(nombre_col, valores)
        elif op_ctx.operacionAgrupar():
            cols = self.obtener_lista_ids(op_ctx.operacionAgrupar().listaIDs())
            return tabla.agrupar_por_xd(cols)
        elif op_ctx.operacionResumir():
            if not hasattr(tabla, 'resumir_xd'):
                raise TypeError("resumir_xd requiere que la tabla haya sido agrupada previamente con agrupar_por_xd xd.")
            specs = {}
            for agg_ctx in op_ctx.operacionResumir().listaAgregaciones().agregacion():
                alias = agg_ctx.ID(0).getText()
                fn_agg = agg_ctx.FUNCION_AGG().getText()
                col_orig = agg_ctx.ID(1).getText() if len(agg_ctx.ID()) > 1 else alias
                specs[alias] = (col_orig, fn_agg)
            return tabla.resumir_xd(**specs)
        return tabla

    def evaluar_expresion_booleana(self, tabla, ctx):
        izq = self.evaluar_expresion_aritmetica(tabla, ctx.expresionAritmetica(0))
        der = self.evaluar_expresion_aritmetica(tabla, ctx.expresionAritmetica(1))
        op = ctx.opRelacional().getText()

        if hasattr(izq, 'mayor_que_xd'):
            if op == '>': return izq.mayor_que_xd(der)
            elif op == '<': return izq.menor_que_xd(der)
            elif op == '>=': return izq.mayor_igual_xd(der)
            elif op == '<=': return izq.menor_igual_xd(der)
            elif op == '==': return izq.igual_a_xd(der)
            elif op == '!=': return izq.diferente_de_xd(der)
        raise ValueError(f"Operador relacional '{op}' no soportado xd.")

    def evaluar_expresion_aritmetica(self, tabla, ctx):
        val = self.evaluar_termino(tabla, ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            sig_val = self.evaluar_termino(tabla, ctx.termino(i))
            val = val + sig_val
        return val

    def evaluar_termino(self, tabla, ctx):
        val = self.evaluar_factor(tabla, ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            sig_val = self.evaluar_factor(tabla, ctx.factor(i))
            val = val * sig_val
        return val

    def evaluar_factor(self, tabla, ctx):
        if ctx.ID():
            nombre_col = ctx.ID().getText()
            if nombre_col in tabla.nombres_columnas:
                return tabla[nombre_col].arreglo
            elif nombre_col in self.entorno:
                return self.entorno[nombre_col]
            raise KeyError(f"Columna o variable '{nombre_col}' no encontrada xd.")
        elif ctx.NUMERO():
            v = ctx.NUMERO().getText()
            return float(v) if '.' in v else int(v)
        elif ctx.expresionAritmetica():
            return self.evaluar_expresion_aritmetica(tabla, ctx.expresionAritmetica())

    def obtener_lista_ids(self, ctx):
        return [id_node.getText() for id_node in ctx.ID()]

    def visitInstruccionGuardado(self, ctx):
        nombre_var = ctx.ID().getText()
        ruta = ctx.CADENA().getText().strip('"\'')
        if nombre_var not in self.entorno:
            raise NameError(f"Variable '{nombre_var}' no existe xd.")
        guardar_csv_xd(self.entorno[nombre_var], ruta)
        return True

    def visitInstruccionVisualizacion(self, ctx):
        nombre_var = ctx.ID().getText()
        if nombre_var not in self.entorno:
            raise NameError(f"Variable '{nombre_var}' no existe xd.")
        tabla = self.entorno[nombre_var]

        cadenas = [c.getText().strip('"\'') for c in ctx.CADENA()]
        titulo = cadenas[0] if ctx.TITULO() and len(cadenas) > 0 else "Gráfico DSL xd"
        eje_x = cadenas[1] if ctx.EJE_X() and len(cadenas) > 1 else ""
        eje_y = cadenas[2] if ctx.EJE_Y() and len(cadenas) > 2 else ""
        guardar_ruta = cadenas[-1] if ctx.GUARDAR() and len(cadenas) > 0 else "salidas/grafico_dsl.svg"

        fig = crear_figura_xd(titulo=titulo, etiqueta_x=eje_x, etiqueta_y=eje_y)
        cols = tabla.nombres_columnas
        col_x = cols[0]
        col_y = cols[1] if len(cols) > 1 else cols[0]

        t_grafico = ctx.tipoGrafico()
        if t_grafico.GRAFICAR_BARRAS_XD():
            fig.graficar_barras_xd(tabla[col_x].datos, tabla[col_y].datos)
        elif t_grafico.GRAFICAR_LINEAS_XD():
            fig.graficar_lineas_xd(tabla[col_x].datos, tabla[col_y].datos)
        elif t_grafico.GRAFICAR_HISTOGRAMA_XD():
            fig.graficar_histograma_xd(tabla[col_x].datos)
        elif t_grafico.GRAFICAR_DISPERSION_XD():
            fig.graficar_dispersion_xd(tabla[col_x].datos, tabla[col_y].datos)
        elif t_grafico.GRAFICAR_CAJAS_XD():
            fig.graficar_cajas_xd(tabla[col_x].datos)

        fig.guardar_svg_xd(guardar_ruta)
        return True
