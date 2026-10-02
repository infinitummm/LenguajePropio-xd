"""
Intérprete, Validador y Ejecutor Semántico CLI - MomoLang XD (.xd)
=================================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Uso:
    python ejecutar_dsl.py <ruta_archivo.xd> [--solo-validar] [--arbol]
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from src.validador_momo_xd import validar_archivo_momo
from src.semantica import VisitorEjecutor, ErrorSemantico


def mostrar_banner():
    print("=" * 70)
    print("  MEME-LANG XD (MomoLang) - DSL DE CIENCIA DE DATOS Y VISUALIZACIÓN :v")
    print("  Intérprete Semántico y Validador - ANTLR4 + Python Puro")
    print("=" * 70)


def principal():
    mostrar_banner()

    if len(sys.argv) < 2:
        print("\nUso correcto:")
        print("    python ejecutar_dsl.py <archivo.xd> [--solo-validar] [--arbol]")
        print("\nEjemplos:")
        print("    python ejecutar_dsl.py ejemplos/programa_ventas_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_empleados_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_estudiantes_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_correcto1.xd --arbol")
        print("    python ejecutar_dsl.py ejemplos/programa_incorrecto1.xd")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    mostrar_arbol = "--arbol" in sys.argv
    solo_validar = "--solo-validar" in sys.argv

    if not os.path.exists(ruta_archivo):
        print(f"\n[ERROR] El archivo especificado no existe: '{ruta_archivo}' xd")
        sys.exit(1)

    print(f"\n>> Analizando archivo: {ruta_archivo}")
    resultado = validar_archivo_momo(ruta_archivo)

    print("-" * 70)
    if not resultado["aceptado"]:
        print("  ESTADO SINTÁCTICO: [ PROGRAMA RECHAZADO xd ]")
        print("-" * 70)
        print(f"  Se encontraron {len(resultado['errores'])} error(es) en el código fuente:\n")
        for idx, err in enumerate(resultado["errores"], 1):
            print(f"  {idx}. {err['detalle']}")

        print(chr(10) + "=" * 70)
        print("  Corrige los errores de sintaxis indicados para continuar.")
        print("=" * 70)
        sys.exit(1)

    # El programa es sintácticamente aceptado
    print("  ESTADO SINTÁCTICO: [ PROGRAMA ACEPTADO :v ]")
    print("-" * 70)
    print("  El archivo cumple al 100% las reglas léxicas y sintácticas del DSL.")

    stats = resultado["estadisticas"]
    print("\n>> Métricas de la Estructura Sintáctica:")
    print(f"   • Total de Sentencias:    {stats['total_sentencias']}")
    print(f"   • Asignaciones/Pipelines: {stats['asignaciones']}")
    print(f"   • Impresiones (when):     {stats['impresiones']}")
    print(f"   • Exportaciones (guardar):{stats['guardados']}")
    print(f"   • Visualizaciones:        {stats['visualizaciones']}")
    if stats.get("expresiones", 0) > 0:
        print(f"   • Expresiones Aritméticas:{stats['expresiones']}")

    if mostrar_arbol:
        print("\n>> Árbol de Análisis Sintáctico Jerárquico:")
        print(resultado["arbol_jerarquico"])

    if solo_validar:
        print(chr(10) + "=" * 70)
        print("  [Modo solo validación] No se ejecutaron las operaciones semánticas.")
        print("=" * 70)
        sys.exit(0)

    # -------------------------------------------------------------------------
    # EJECUCIÓN SEMÁNTICA (FASE 2)
    # -------------------------------------------------------------------------
    print("\n>> Iniciando Ejecución Semántica con Motores Propios (Visitor)...\n")
    visitor = VisitorEjecutor()

    try:
        visitor.visit(resultado["arbol"])
        print(chr(10) + "=" * 70)
        print("  ESTADO SEMÁNTICO: [ EJECUCIÓN EXITOSA PAPU :v ]")
        print("=" * 70)
        variables_creadas = list(visitor.ts.obtener_todas_las_variables().keys())
        print(f"  • Variables procesadas en memoria: {variables_creadas}")
        if visitor.salidas_generadas:
            print(f"  • Archivos CSV exportados con éxito: {visitor.salidas_generadas}")
        print("=" * 70)
        sys.exit(0)

    except ErrorSemantico as e:
        print(chr(10) + "=" * 70)
        print("  ESTADO SEMÁNTICO: [ ERROR SEMÁNTICO DETECTADO xd ]")
        print("=" * 70)
        print(f"  {e}")
        print("=" * 70)
        sys.exit(2)
    except Exception as e:
        print(chr(10) + "=" * 70)
        print(f"  [Error en Tiempo de Ejecución]: {e}")
        print("=" * 70)
        sys.exit(3)


if __name__ == "__main__":
    principal()
