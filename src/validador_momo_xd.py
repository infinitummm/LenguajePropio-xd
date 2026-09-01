"""
Validador Léxico y Sintáctico para LenguajeMomoXD (.xd) - Corte 1
==================================================================
Asignatura: Lenguajes de Programación y Transducción
Universidad Sergio Arboleda (2026-2)

Propósito:
- Analizar léxica y sintácticamente programas escritos en el DSL (.xd).
- Determinar de forma determinista si el programa es ACEPTADO o RECHAZADO.
- En caso de aceptación: Generar el árbol de análisis sintáctico (Parse Tree)
  y métricas estructurales del código fuente.
- En caso de rechazo: Reportar con precisión la línea, columna y causa
  específica del error sintáctico o léxico.
"""

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener
from antlr4.tree.Trees import Trees

from src.parser.LenguajeMomoXDLexer import LenguajeMomoXDLexer
from src.parser.LenguajeMomoXDParser import LenguajeMomoXDParser


class MomoSintaxisErrorListener(ErrorListener):
    """
    Listener personalizado para capturar y diagnosticar errores léxicos y sintácticos
    con mensajes claros y comprensibles en español.
    """

    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Obtener el texto del token ofensivo si está disponible
        token_texto = offendingSymbol.text if offendingSymbol is not None else "desconocido"
        
        # Sugerencias contextuales según el error detectado
        sugerencia = ""
        if "missing 'xd'" in msg.lower() or "mismatched input" in msg.lower() and token_texto not in ["xd", "XD", "xD"]:
            sugerencia = " -> ¿Olvidaste terminar la sentencia con 'xd'?"
        elif "no viable alternative" in msg.lower():
            sugerencia = " -> Instrucción no reconocida en la gramática de MomoLang."
        elif "extraneous input" in msg.lower():
            sugerencia = f" -> Elemento inesperado '{token_texto}'."

        error_formateado = (
            f"[Error Sintáctico xd] Línea {line}, Columna {column}: "
            f"Token conflictivo '{token_texto}'. {msg}{sugerencia}"
        )
        self.errores.append({
            "linea": line,
            "columna": column,
            "token": token_texto,
            "mensaje": msg,
            "detalle": error_formateado
        })


def formatear_arbol_sintactico(tree, parser, nivel=0) -> str:
    """
    Genera una representación jerárquica indentada legible del árbol de análisis sintáctico.
    """
    nombre_regla = Trees.getNodeText(tree, parser.ruleNames)
    resultado = ["  " * nivel + f"├── ({nombre_regla})"]

    if hasattr(tree, "children") and tree.children:
        for hijo in tree.children:
            if hasattr(hijo, "getRuleIndex"):
                resultado.append(formatear_arbol_sintactico(hijo, parser, nivel + 1))
            else:
                # Nodo hoja (Token)
                token_text = hijo.getText().strip()
                if token_text:
                    resultado.append("  " * (nivel + 1) + f"└── [Token: '{token_text}']")

    return "\n".join(resultado)


def validar_codigo_momo(codigo_fuente: str) -> dict:
    """
    Valida léxica y sintácticamente una cadena de código fuente en MomoLang (.xd).
    Retorna un diccionario estructurado con el estado (ACEPTADO/RECHAZADO),
    errores y árbol de derivación.
    """
    input_stream = InputStream(codigo_fuente)
    lexer = LenguajeMomoXDLexer(input_stream)

    error_listener = MomoSintaxisErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    parser = LenguajeMomoXDParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    # Invocar la regla inicial 'programa'
    tree = parser.programa()

    errores = error_listener.errores
    es_aceptado = len(errores) == 0

    arbol_lisp = ""
    arbol_jerarquico = ""
    estadisticas = {
        "total_sentencias": 0,
        "asignaciones": 0,
        "impresiones": 0,
        "guardados": 0,
        "visualizaciones": 0
    }

    if es_aceptado:
        arbol_lisp = Trees.toStringTree(tree, None, parser)
        arbol_jerarquico = formatear_arbol_sintactico(tree, parser)
        
        # Calcular estadísticas sintácticas de sentencias reconocidas
        if hasattr(tree, "sentencia") and callable(tree.sentencia):
            sentencias = tree.sentencia()
            if sentencias is not None:
                if not isinstance(sentencias, list):
                    sentencias = [sentencias]
                estadisticas["total_sentencias"] = len(sentencias)
                for s in sentencias:
                    if s.asignacion():
                        estadisticas["asignaciones"] += 1
                    elif s.instruccionImprimir():
                        estadisticas["impresiones"] += 1
                    elif s.instruccionGuardado():
                        estadisticas["guardados"] += 1
                    elif s.instruccionVisualizacion():
                        estadisticas["visualizaciones"] += 1

    return {
        "aceptado": es_aceptado,
        "arbol": tree,
        "parser": parser,
        "arbol_lisp": arbol_lisp,
        "arbol_jerarquico": arbol_jerarquico,
        "errores": errores,
        "estadisticas": estadisticas
    }


def validar_archivo_momo(ruta_archivo: str) -> dict:
    """
    Lee un archivo con código fuente .xd y realiza la validación léxica y sintáctica.
    """
    with open(ruta_archivo, mode="r", encoding="utf-8") as f:
        codigo = f.read()
    return validar_codigo_momo(codigo)
