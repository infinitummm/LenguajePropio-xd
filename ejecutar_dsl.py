"""
Intérprete de Línea de Comandos para el DSL LenguajeDatos (Corte 1 xd)
Permite ejecutar cualquier archivo de código .dsl desde la consola.
"""

import sys
import os
from src.lexer_parser_runner import analizar_archivo_dsl
from src.visitor_ejecutor import EvaluadorDSLVisitor

def principal():
    if len(sys.argv) < 2:
        print("Uso: python ejecutar_dsl.py <archivo.dsl> xd")
        sys.exit(1)

    ruta_dsl = sys.argv[1]
    if not os.path.exists(ruta_dsl):
        print(f"Error: El archivo '{ruta_dsl}' no existe xd.")
        sys.exit(1)

    print("=" * 60)
    print(f"EJECUTANDO PROGRAMA DSL: {ruta_dsl} xd")
    print("=" * 60)

    # 1. Análisis Léxico y Sintáctico con ANTLR4
    tree, parser, errores = analizar_archivo_dsl(ruta_dsl)

    if errores:
        print("\n[ERROR] Se encontraron errores de sintaxis en el archivo xd:")
        for err in errores:
            print(f"  {err}")
        sys.exit(1)

    print("[OK] Analisis lexico y sintactico completado sin errores xd.")

    # 2. Evaluación Semántica mediante el patrón Visitor
    try:
        evaluador = EvaluadorDSLVisitor()
        entorno = evaluador.visitPrograma(tree)
        print("[OK] Ejecucion semantica completada exitosamente xd.")
        print(f"\nVariables creadas en el entorno: {list(entorno.keys())}")
    except Exception as e:
        print(f"\n[ERROR] Error de ejecucion semantica xd: {e}")
        sys.exit(1)

    print("=" * 60)

if __name__ == "__main__":
    principal()
