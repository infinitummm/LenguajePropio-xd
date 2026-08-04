"""
Módulo de Ejecución y Diagnóstico Sintáctico (Corte 1 xd)
Lee programas del DSL LenguajeDatos, realiza análisis léxico y sintáctico con ANTLR4,
y reporta errores sintácticos con número de línea y columna.
"""

from antlr4 import InputStream, CommonTokenStream
from antlr4.error.ErrorListener import ErrorListener

from src.parser.LenguajeDatosLexer import LenguajeDatosLexer
from src.parser.LenguajeDatosParser import LenguajeDatosParser

class SintaxisErrorListener(ErrorListener):
    """Manejador personalizado de errores léxicos y sintácticos xd"""
    def __init__(self):
        super().__init__()
        self.errores = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"[Error Sintáctico xd] Línea {line}:{column} - {msg}"
        self.errores.append(error_msg)

def analizar_codigo_dsl(codigo_fuente):
    """
    Analiza una cadena de código DSL.
    Retorna (parse_tree, parser, lista_errores) xd
    """
    input_stream = InputStream(codigo_fuente)
    lexer = LenguajeDatosLexer(input_stream)

    # Reemplazar listener de error por defecto
    error_listener = SintaxisErrorListener()
    lexer.removeErrorListeners()
    lexer.addErrorListener(error_listener)

    stream = CommonTokenStream(lexer)
    parser = LenguajeDatosParser(stream)

    parser.removeErrorListeners()
    parser.addErrorListener(error_listener)

    tree = parser.programa()
    return tree, parser, error_listener.errores

def analizar_archivo_dsl(ruta_archivo):
    """Lee y analiza un archivo con extensión .dsl xd"""
    with open(ruta_archivo, mode="r", encoding="utf-8") as f:
        codigo = f.read()
    return analizar_codigo_dsl(codigo)
