"""
Visitor Intérprete y Ejecutor Semántico - MomoLang XD
=====================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Recorre el Árbol de Análisis Sintáctico (Parse Tree) de ANTLR4,
evalúa semánticamente las sentencias, gestiona ámbitos en la Tabla de Símbolos,
ejecuta funciones de usuario, bucles (while/for), condicionales y operaciones
vectoriales y tabulares propias (cero dependencias externas).
"""

import os
from src.parser.LenguajeMomoXDVisitor import LenguajeMomoXDVisitor
from src.parser.LenguajeMomoXDParser import LenguajeMomoXDParser
from src.core.datos_propios import TablaMomo, SerieMomo, AgrupamientoMomo
from src.core.matematica_propia import (
    VectorMomo,
    sumar_papus,
    multiplicacion,
    resta,
    division
)
from src.semantica.tabla_simbolos import TablaSimbolos, ErrorSemantico, SimboloFuncion


class RetornoMomoException(Exception):
    """Excepción interna para desenrollar la pila en sentencias de retorno (suelta_el_momo)."""

    def __init__(self, valor=None):
        self.valor = valor


class VisitorEjecutor(LenguajeMomoXDVisitor):
    """
    Intérprete semántico que recorre el Parse Tree y ejecuta el programa .xd
    """

    def __init__(self, tabla_simbolos=None):
        super().__init__()
        self.ts = tabla_simbolos or TablaSimbolos()
        self.tabla_actual = None  # Contexto activo para resolución de columnas en pipelines
        self.salidas_generadas = []

    def visitPrograma(self, ctx: LenguajeMomoXDParser.ProgramaContext):
        resultado = None
        for sentencia in ctx.sentencia():
            resultado = self.visit(sentencia)
        return resultado

    def visitSentencia(self, ctx: LenguajeMomoXDParser.SentenciaContext):
        if ctx.asignacion():
            return self.visit(ctx.asignacion())
        elif ctx.instruccionImprimir():
            return self.visit(ctx.instruccionImprimir())
        elif ctx.instruccionGuardado():
            return self.visit(ctx.instruccionGuardado())
        elif ctx.instruccionVisualizacion():
            return self.visit(ctx.instruccionVisualizacion())
        elif ctx.instruccionSi():
            return self.visit(ctx.instruccionSi())
        elif ctx.instruccionMientras():
            return self.visit(ctx.instruccionMientras())
        elif ctx.instruccionPara():
            return self.visit(ctx.instruccionPara())
        elif ctx.definicionFuncion():
            return self.visit(ctx.definicionFuncion())
        elif ctx.instruccionRetorno():
            return self.visit(ctx.instruccionRetorno())
        elif ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        elif ctx.expresionAritmetica():
            return self.visit(ctx.expresionAritmetica())
        return None

    # -------------------------------------------------------------------------
    # Asignaciones y Pipelines
    # -------------------------------------------------------------------------

    def visitAsignacion(self, ctx: LenguajeMomoXDParser.AsignacionContext):
        nombre_var = ctx.ID().getText()
        valor = self.visit(ctx.expresionPipeline())
        self.ts.asignar_existente_o_local(nombre_var, valor)
        return valor

    def visitExpresionPipeline(self, ctx: LenguajeMomoXDParser.ExpresionPipelineContext):
        resultado = self.visit(ctx.expresionBase())

        for op in ctx.operacionPipeline():
            anterior_tabla = self.tabla_actual
            self.tabla_actual = resultado
            try:
                resultado = self.visit(op)
            finally:
                self.tabla_actual = anterior_tabla

        return resultado

    def visitExpresionBase(self, ctx: LenguajeMomoXDParser.ExpresionBaseContext):
        if ctx.instruccionCarga():
            return self.visit(ctx.instruccionCarga())
        elif ctx.expresionAritmetica():
            return self.visit(ctx.expresionAritmetica())
        return None

    # -------------------------------------------------------------------------
    # Carga, Guardado e Impresión
    # -------------------------------------------------------------------------

    def visitInstruccionCarga(self, ctx: LenguajeMomoXDParser.InstruccionCargaContext):
        ruta_archivo = ctx.CADENA(0).getText().strip('"\'')
        separador = ","
        if ctx.SEPARADOR():
            separador = ctx.CADENA(1).getText().strip('"\'')

        linea = ctx.start.line
        col = ctx.start.column

        if not os.path.exists(ruta_archivo):
            raise ErrorSemantico(
                mensaje=f"No se encuentra el archivo CSV '{ruta_archivo}'. Revisa la ruta especificada.",
                linea=linea,
                columna=col,
                tipo_error="ARCHIVO_NO_ENCONTRADO"
            )

        tabla = TablaMomo.pasa_el_pack(ruta_archivo, separador=separador)
        return tabla

    def visitInstruccionGuardado(self, ctx: LenguajeMomoXDParser.InstruccionGuardadoContext):
        nombre_var = ctx.ID().getText()
        ruta_salida = ctx.CADENA().getText().strip('"\'')
        linea = ctx.start.line
        col = ctx.start.column

        objeto = self.ts.obtener(nombre_var, linea=linea, columna=col)
        if not isinstance(objeto, TablaMomo):
            raise ErrorSemantico(
                mensaje=f"Solo se pueden guardar tablas de datos en CSV. La variable '{nombre_var}' es de tipo '{self.ts.inferir_tipo(objeto)}'.",
                linea=linea,
                columna=col,
                tipo_error="TIPO_INCOMPATIBLE"
            )

        objeto.subir_al_grupo(ruta_salida)
        self.salidas_generadas.append(ruta_salida)
        print(f"[CSV Exportado :v] Tabla '{nombre_var}' guardada en '{ruta_salida}' ({objeto.num_filas} filas).")
        return ruta_salida

    def visitInstruccionImprimir(self, ctx: LenguajeMomoXDParser.InstruccionImprimirContext):
        if ctx.expresionAritmetica():
            val = self.visit(ctx.expresionAritmetica())
        elif ctx.CADENA():
            val = ctx.CADENA().getText().strip('"\'')
        elif ctx.ID():
            nombre = ctx.ID().getText()
            val = self.ts.obtener(nombre, linea=ctx.start.line, columna=ctx.start.column)
        else:
            val = ""

        if isinstance(val, TablaMomo):
            print(val.ver_primeras_filas(5))
        elif isinstance(val, VectorMomo):
            print(val.datos)
        else:
            print(val)
        return val

    # -------------------------------------------------------------------------
    # Operaciones del Pipeline (|:v>)
    # -------------------------------------------------------------------------

    def visitOperacionPipeline(self, ctx: LenguajeMomoXDParser.OperacionPipelineContext):
        return self.visitChildren(ctx)

    def visitOperacionSeleccionar(self, ctx: LenguajeMomoXDParser.OperacionSeleccionarContext):
        if not isinstance(self.tabla_actual, TablaMomo):
            raise ErrorSemantico(
                mensaje="La operación 'escojo_a' solo puede aplicarse sobre una tabla de datos.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        columnas_pedidas = self.visit(ctx.listaIDs())
        for col in columnas_pedidas:
            if col not in self.tabla_actual.columnas:
                raise ErrorSemantico(
                    mensaje=f"La columna '{col}' no existe en el dataset. Columnas disponibles: {self.tabla_actual.columnas}",
                    linea=ctx.start.line,
                    columna=ctx.start.column,
                    tipo_error="COLUMNA_INEXISTENTE"
                )

        return self.tabla_actual.escojo_a(columnas_pedidas)

    def visitOperacionFiltrar(self, ctx: LenguajeMomoXDParser.OperacionFiltrarContext):
        if not isinstance(self.tabla_actual, TablaMomo):
            raise ErrorSemantico(
                mensaje="La operación de filtrado 'but_te_enteras_que' requiere una tabla de datos.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        mascara = self.visit(ctx.expresionBooleana())
        return self.tabla_actual.but_te_enteras_que(mascara)

    def visitOperacionCrearColumna(self, ctx: LenguajeMomoXDParser.OperacionCrearColumnaContext):
        if not isinstance(self.tabla_actual, TablaMomo):
            raise ErrorSemantico(
                mensaje="La creación de columnas 'el_futuro_es_hoy_oiste_viejo' requiere una tabla de datos.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        nombre_col = ctx.ID().getText()
        valores_calculados = self.visit(ctx.expresionAritmetica())

        nueva_tabla = TablaMomo(dict(self.tabla_actual._columnas))
        nueva_tabla.el_futuro_es_hoy_oiste_viejo(nombre_col, valores_calculados)
        return nueva_tabla

    def visitOperacionOrdenar(self, ctx: LenguajeMomoXDParser.OperacionOrdenarContext):
        if not isinstance(self.tabla_actual, TablaMomo):
            raise ErrorSemantico(
                mensaje="La operación 'ordenar_a_los_papus' requiere una tabla de datos.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        columna = ctx.ID().getText()
        if columna not in self.tabla_actual.columnas:
            raise ErrorSemantico(
                mensaje=f"No se puede ordenar por la columna '{columna}' porque no existe. Columnas: {self.tabla_actual.columnas}",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="COLUMNA_INEXISTENTE"
            )

        ascendente = True
        if ctx.DE_ARRIBA_A_ABAJO() or ctx.DESCENDENTE():
            ascendente = False

        return self.tabla_actual.ordenar_a_los_papus(columna, ascendente=ascendente)

    def visitOperacionAgrupar(self, ctx: LenguajeMomoXDParser.OperacionAgruparContext):
        if not isinstance(self.tabla_actual, TablaMomo):
            raise ErrorSemantico(
                mensaje="La agrupación 'juntar_a_la_grasa_por' requiere una tabla de datos.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        columnas_agrupar = self.visit(ctx.listaIDs())
        for col in columnas_agrupar:
            if col not in self.tabla_actual.columnas:
                raise ErrorSemantico(
                    mensaje=f"No se puede agrupar por '{col}' porque no existe en la tabla. Columnas: {self.tabla_actual.columnas}",
                    linea=ctx.start.line,
                    columna=ctx.start.column,
                    tipo_error="COLUMNA_INEXISTENTE"
                )

        agrupamiento = self.tabla_actual.juntar_a_la_grasa_por(columnas_agrupar)
        if ctx.listaAgregaciones():
            lista_aggs = self.visit(ctx.listaAgregaciones())
            return agrupamiento.sacar_cuentas(lista_aggs)
        return agrupamiento

    def visitOperacionResumir(self, ctx: LenguajeMomoXDParser.OperacionResumirContext):
        if not isinstance(self.tabla_actual, AgrupamientoMomo):
            raise ErrorSemantico(
                mensaje="La operación 'sacar_cuentas' o 'calcular' debe aplicarse después de agrupar con 'juntar_a_la_grasa_por'.",
                linea=ctx.start.line,
                columna=ctx.start.column,
                tipo_error="OPERACION_INVALIDA"
            )

        lista_aggs = self.visit(ctx.listaAgregaciones())
        return self.tabla_actual.sacar_cuentas(lista_aggs)

    def visitListaAgregaciones(self, ctx: LenguajeMomoXDParser.ListaAgregacionesContext):
        agregaciones = []
        for agg_ctx in ctx.agregacion():
            nombre_salida, func_nombre, col_origen = self.visit(agg_ctx)
            agregaciones.append((nombre_salida, func_nombre, col_origen))
        return agregaciones

    def visitAgregacion(self, ctx: LenguajeMomoXDParser.AgregacionContext):
        if ctx.COMO():
            func_nombre = ctx.funcionAgg(0).getText()
            col_origen = None
            if len(ctx.funcionAgg()) > 1:
                col_origen = ctx.funcionAgg(1).getText()
            elif len(ctx.ID()) > 1:
                col_origen = ctx.ID(0).getText()
                nombre_salida = ctx.ID(1).getText()
                return (nombre_salida, func_nombre, col_origen)
            
            # Si solo hay 1 ID, es el nombre_salida tras COMO
            nombre_salida = ctx.ID(0).getText() if ctx.ID() else f"{func_nombre}_res"
            return (nombre_salida, func_nombre, col_origen)
        else:
            nombre_salida = ctx.ID(0).getText() if ctx.ID() else "resultado"
            func_nombre = ctx.funcionAgg(0).getText()
            col_origen = None
            if len(ctx.ID()) > 1:
                col_origen = ctx.ID(1).getText()
            elif len(ctx.funcionAgg()) > 1:
                col_origen = ctx.funcionAgg(1).getText()
            return (nombre_salida, func_nombre, col_origen)

    # -------------------------------------------------------------------------
    # Visualizaciones (Fase 3 informativa)
    # -------------------------------------------------------------------------

    def visitInstruccionVisualizacion(self, ctx: LenguajeMomoXDParser.InstruccionVisualizacionContext):
        nombre_tabla = ctx.ID().getText()
        tipo_graf = ctx.tipoGrafico().getText()
        self.ts.obtener(nombre_tabla, linea=ctx.start.line, columna=ctx.start.column)
        print(f"[Visualización :v] Sintaxis reconocida para {tipo_graf} sobre '{nombre_tabla}' (Generación gráfica programada para Fase 3).")
        return None

    # -------------------------------------------------------------------------
    # Condicionales (si_el_papu / si_pasa_esto)
    # -------------------------------------------------------------------------

    def visitInstruccionSi(self, ctx: LenguajeMomoXDParser.InstruccionSiContext):
        condicion = self.visit(ctx.expresionBooleana())
        if isinstance(condicion, VectorMomo):
            es_verdad = any(condicion.datos)
        else:
            es_verdad = bool(condicion)

        if es_verdad:
            return self.visit(ctx.bloque(0))
        elif len(ctx.bloque()) > 1:
            return self.visit(ctx.bloque(1))
        return None

    # -------------------------------------------------------------------------
    # Ciclos (mientras_el_papu & para_cada_papu)
    # -------------------------------------------------------------------------

    def visitInstruccionMientras(self, ctx: LenguajeMomoXDParser.InstruccionMientrasContext):
        limite_seguridad = 1000000
        iteraciones = 0
        resultado = None

        while True:
            condicion = self.visit(ctx.expresionBooleana())
            if isinstance(condicion, VectorMomo):
                es_verdad = any(condicion.datos)
            else:
                es_verdad = bool(condicion)

            if not es_verdad:
                break

            resultado = self.visit(ctx.bloque())
            iteraciones += 1
            if iteraciones > limite_seguridad:
                raise ErrorSemantico(
                    f"Bucle 'mientras_el_papu' excedió el límite de seguridad de {limite_seguridad} iteraciones.",
                    linea=ctx.start.line,
                    columna=ctx.start.column,
                    tipo_error="BUCLE_INFINITO"
                )

        return resultado

    def visitInstruccionPara(self, ctx: LenguajeMomoXDParser.InstruccionParaContext):
        nombre_var = ctx.ID().getText()
        inicio = self.visit(ctx.expresionAritmetica(0))
        fin = self.visit(ctx.expresionAritmetica(1))

        if not isinstance(inicio, int) or not isinstance(fin, int):
            try:
                inicio = int(inicio)
                fin = int(fin)
            except Exception:
                raise ErrorSemantico(
                    f"Los límites de 'para_cada_papu' deben ser enteros. Se recibió desde={inicio}, hasta={fin}.",
                    linea=ctx.start.line,
                    columna=ctx.start.column,
                    tipo_error="TIPO_INCOMPATIBLE"
                )

        paso = 1 if inicio <= fin else -1
        resultado = None
        for val in range(inicio, fin + paso, paso):
            self.ts.asignar_existente_o_local(nombre_var, val)
            resultado = self.visit(ctx.bloque())

        return resultado

    # -------------------------------------------------------------------------
    # Funciones de Usuario y Retornos
    # -------------------------------------------------------------------------

    def visitDefinicionFuncion(self, ctx: LenguajeMomoXDParser.DefinicionFuncionContext):
        nombre_func = ctx.ID().getText()
        parametros = []
        if ctx.listaParametros():
            parametros = [p.getText() for p in ctx.listaParametros().parametro()]

        cuerpo_bloque = ctx.bloque()
        self.ts.definir_funcion(nombre_func, parametros, cuerpo_bloque)
        return None

    def visitInstruccionRetorno(self, ctx: LenguajeMomoXDParser.InstruccionRetornoContext):
        valor = None
        if ctx.expresionAritmetica():
            valor = self.visit(ctx.expresionAritmetica())
        raise RetornoMomoException(valor)

    def visitBloque(self, ctx: LenguajeMomoXDParser.BloqueContext):
        resultado = None
        for s in ctx.sentencia():
            resultado = self.visit(s)
        return resultado

    # -------------------------------------------------------------------------
    # Expresiones Booleanas y Lógicas
    # -------------------------------------------------------------------------

    def visitExpresionBooleana(self, ctx: LenguajeMomoXDParser.ExpresionBooleanaContext):
        return self.visit(ctx.expresionLogicaOr())

    def visitExpresionLogicaOr(self, ctx: LenguajeMomoXDParser.ExpresionLogicaOrContext):
        resultado = self.visit(ctx.expresionLogicaAnd(0))
        for i in range(1, len(ctx.expresionLogicaAnd())):
            siguiente = self.visit(ctx.expresionLogicaAnd(i))
            if isinstance(resultado, VectorMomo) or isinstance(siguiente, VectorMomo):
                d1 = resultado.datos if isinstance(resultado, VectorMomo) else [bool(resultado)]
                d2 = siguiente.datos if isinstance(siguiente, VectorMomo) else [bool(siguiente)]
                max_len = max(len(d1), len(d2))
                d1_ext = d1 * max_len if len(d1) == 1 else d1
                d2_ext = d2 * max_len if len(d2) == 1 else d2
                resultado = VectorMomo([a or b for a, b in zip(d1_ext, d2_ext)])
            else:
                resultado = bool(resultado) or bool(siguiente)
        return resultado

    def visitExpresionLogicaAnd(self, ctx: LenguajeMomoXDParser.ExpresionLogicaAndContext):
        resultado = self.visit(ctx.expresionLogicaNot(0))
        for i in range(1, len(ctx.expresionLogicaNot())):
            siguiente = self.visit(ctx.expresionLogicaNot(i))
            if isinstance(resultado, VectorMomo) or isinstance(siguiente, VectorMomo):
                d1 = resultado.datos if isinstance(resultado, VectorMomo) else [bool(resultado)]
                d2 = siguiente.datos if isinstance(siguiente, VectorMomo) else [bool(siguiente)]
                max_len = max(len(d1), len(d2))
                d1_ext = d1 * max_len if len(d1) == 1 else d1
                d2_ext = d2 * max_len if len(d2) == 1 else d2
                resultado = VectorMomo([a and b for a, b in zip(d1_ext, d2_ext)])
            else:
                resultado = bool(resultado) and bool(siguiente)
        return resultado

    def visitExpresionLogicaNot(self, ctx: LenguajeMomoXDParser.ExpresionLogicaNotContext):
        val = self.visit(ctx.expresionRelacional())
        if ctx.NO_ES_CIERTO() or ctx.NOT_OP():
            if isinstance(val, VectorMomo):
                return VectorMomo([not x for x in val.datos])
            return not bool(val)
        return val

    def visitExpresionRelacional(self, ctx: LenguajeMomoXDParser.ExpresionRelacionalContext):
        if ctx.PAREN_IZQ():
            return self.visit(ctx.expresionBooleana())
        if ctx.opRelacional():
            izq = self.visit(ctx.expresionAritmetica(0))
            der = self.visit(ctx.expresionAritmetica(1))
            op = ctx.opRelacional().getText()
            if op == ">":
                return izq > der
            elif op == ">=":
                return izq >= der
            elif op == "<":
                return izq < der
            elif op == "<=":
                return izq <= der
            elif op == "==":
                return izq == der
            elif op == "!=":
                return izq != der
            raise ErrorSemantico(f"Operador relacional desconocido: '{op}'", linea=ctx.start.line, columna=ctx.start.column)
        return self.visit(ctx.expresionAritmetica(0))

    # -------------------------------------------------------------------------
    # Expresiones Aritméticas, Términos y Factores
    # -------------------------------------------------------------------------

    def visitExpresionAritmetica(self, ctx: LenguajeMomoXDParser.ExpresionAritmeticaContext):
        resultado = self.visit(ctx.termino(0))
        num_terminos = len(ctx.termino())

        for i in range(1, num_terminos):
            hijo_op = ctx.getChild(2 * i - 1).getText()
            siguiente = self.visit(ctx.termino(i))
            if hijo_op == "+":
                if isinstance(resultado, str) or isinstance(siguiente, str):
                    resultado = str(resultado) + str(siguiente)
                else:
                    resultado = resultado + siguiente
            elif hijo_op == "-":
                resultado = resultado - siguiente
        return resultado

    def visitTermino(self, ctx: LenguajeMomoXDParser.TerminoContext):
        resultado = self.visit(ctx.factor(0))
        num_factores = len(ctx.factor())

        for i in range(1, num_factores):
            hijo_op = ctx.getChild(2 * i - 1).getText()
            siguiente = self.visit(ctx.factor(i))
            if hijo_op == "*":
                resultado = resultado * siguiente
            elif hijo_op == "/":
                resultado = resultado / siguiente
            elif hijo_op == "%":
                resultado = resultado % siguiente
            elif hijo_op == "^":
                resultado = resultado ** siguiente
        return resultado

    def visitFactor(self, ctx: LenguajeMomoXDParser.FactorContext):
        if ctx.PAREN_IZQ():
            return self.visit(ctx.expresionAritmetica())
        elif ctx.llamadaFuncion():
            return self.visit(ctx.llamadaFuncion())
        elif ctx.NUMERO():
            texto = ctx.NUMERO().getText()
            return float(texto) if "." in texto else int(texto)
        elif ctx.CADENA():
            return ctx.CADENA().getText().strip('"\'')
        elif ctx.ID():
            nombre_id = ctx.ID().getText()
            if self.tabla_actual is not None and isinstance(self.tabla_actual, TablaMomo):
                if nombre_id in self.tabla_actual.columnas:
                    return self.tabla_actual[nombre_id].vector
            return self.ts.obtener(nombre_id, linea=ctx.start.line, columna=ctx.start.column)
        elif ctx.funcionAgg():
            nombre_id = ctx.funcionAgg().getText()
            if self.tabla_actual is not None and isinstance(self.tabla_actual, TablaMomo):
                if nombre_id in self.tabla_actual.columnas:
                    return self.tabla_actual[nombre_id].vector
            return self.ts.obtener(nombre_id, linea=ctx.start.line, columna=ctx.start.column)
        return None

    def visitLlamadaFuncion(self, ctx: LenguajeMomoXDParser.LlamadaFuncionContext):
        func_nombre = ctx.funcionNombre().getText()
        argumentos = self.visit(ctx.listaArgumentos()) if ctx.listaArgumentos() else []

        # 1. Función definida por el usuario
        func_usuario = self.ts.obtener_funcion(func_nombre, linea=ctx.start.line, columna=ctx.start.column)
        if func_usuario is not None:
            if len(argumentos) != len(func_usuario.parametros):
                raise ErrorSemantico(
                    f"La función '{func_nombre}' espera {len(func_usuario.parametros)} argumento(s) pero recibió {len(argumentos)}.",
                    linea=ctx.start.line,
                    columna=ctx.start.column,
                    tipo_error="ARIDAD_INCORRECTA"
                )

            ts_anterior = self.ts
            self.ts = func_usuario.ambito_definicion.crear_hijo()
            for param, arg in zip(func_usuario.parametros, argumentos):
                self.ts.definir(param, arg)

            try:
                self.visit(func_usuario.cuerpo_ctx)
                return None
            except RetornoMomoException as ret:
                return ret.valor
            finally:
                self.ts = ts_anterior

        # 2. Funciones integradas (built-ins)
        func_nombre_lower = func_nombre.lower().strip()

        if func_nombre_lower in ("sumar_papus", "suma", "sumar"):
            if len(argumentos) == 1:
                return argumentos[0].suma() if isinstance(argumentos[0], VectorMomo) else argumentos[0]
            elif len(argumentos) == 2:
                return sumar_papus(argumentos[0], argumentos[1])
            raise ErrorSemantico(f"La función '{func_nombre}' recibe 1 o 2 argumentos, no {len(argumentos)}.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("multiplicacion", "multiplicar"):
            if len(argumentos) == 2:
                return multiplicacion(argumentos[0], argumentos[1])
            raise ErrorSemantico(f"La función 'multiplicacion' recibe 2 argumentos, no {len(argumentos)}.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("resta", "restar"):
            if len(argumentos) == 2:
                return resta(argumentos[0], argumentos[1])
            raise ErrorSemantico(f"La función 'resta' recibe 2 argumentos, no {len(argumentos)}.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("division", "dividir"):
            if len(argumentos) == 2:
                return division(argumentos[0], argumentos[1])
            raise ErrorSemantico(f"La función 'division' recibe 2 argumentos, no {len(argumentos)}.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("promedio", "media"):
            if len(argumentos) == 1 and isinstance(argumentos[0], VectorMomo):
                return argumentos[0].promedio()
            raise ErrorSemantico(f"'promedio' requiere 1 columna o vector de datos.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("el_mas_pro", "maximo"):
            if len(argumentos) == 1 and isinstance(argumentos[0], VectorMomo):
                return argumentos[0].el_mas_pro()
            raise ErrorSemantico(f"'el_mas_pro' requiere 1 columna o vector de datos.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("el_mas_manco", "minimo"):
            if len(argumentos) == 1 and isinstance(argumentos[0], VectorMomo):
                return argumentos[0].el_mas_manco()
            raise ErrorSemantico(f"'el_mas_manco' requiere 1 columna o vector de datos.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("desviacion_pro", "desviacion"):
            if len(argumentos) == 1 and isinstance(argumentos[0], VectorMomo):
                return argumentos[0].desviacion_pro()
            raise ErrorSemantico(f"'desviacion_pro' requiere 1 columna o vector de datos.", linea=ctx.start.line, columna=ctx.start.column)

        elif func_nombre_lower in ("contar_papus", "conteo"):
            if len(argumentos) == 1 and isinstance(argumentos[0], VectorMomo):
                return argumentos[0].contar_papus()
            elif len(argumentos) == 0:
                return 0
            raise ErrorSemantico(f"'contar_papus' recibe 0 o 1 argumento.", linea=ctx.start.line, columna=ctx.start.column)

        raise ErrorSemantico(f"Función desconocida o no definida: '{func_nombre}'", linea=ctx.start.line, columna=ctx.start.column)

    def visitListaArgumentos(self, ctx: LenguajeMomoXDParser.ListaArgumentosContext):
        return [self.visit(exp) for exp in ctx.expresionAritmetica()]

    def visitListaIDs(self, ctx: LenguajeMomoXDParser.ListaIDsContext):
        return [id_node.getText() for id_node in ctx.idOAgg()]
