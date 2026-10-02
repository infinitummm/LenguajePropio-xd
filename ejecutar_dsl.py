"""
Intérprete y Ejecutor Semántico CLI - MomoLang XD (.xd)
=======================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Uso:
    python ejecutar_dsl.py <ruta_archivo.xd> [--validar] [--arbol]
"""

import sys
import os

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

from src.validador_momo_xd import validar_archivo_momo
from src.semantica import VisitorEjecutor, ErrorSemantico


def principal():
    if len(sys.argv) < 2:
        print("\nUso correcto:")
        print("    python ejecutar_dsl.py <archivo.xd> [--validar] [--arbol]")
        print("\nEjemplos:")
        print("    python ejecutar_dsl.py ejemplos/programa_control_funciones.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_ventas_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_empleados_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_estudiantes_fase2.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_correcto1.xd")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    mostrar_arbol = "--arbol" in sys.argv
    solo_validar = "--validar" in sys.argv or "--solo-validar" in sys.argv

    if not os.path.exists(ruta_archivo):
        print(f"\n[Error]: El archivo especificado no existe: '{ruta_archivo}' xd")
        sys.exit(1)

    resultado = validar_archivo_momo(ruta_archivo)

    # 1. Manejo de Errores Sintácticos
    if not resultado["aceptado"]:
        print("\n" + "=" * 65)
        print("  [ERROR DE SINTAXIS EN EL CÓDIGO FUENTE]")
        print("=" * 65)
        for idx, err in enumerate(resultado["errores"], 1):
            print(f"  {idx}. {err['detalle']}")
        print("=" * 65)
        sys.exit(1)

    # 2. Modo opcional de solo validación o árbol sintáctico
    if solo_validar or mostrar_arbol:
        stats = resultado["estadisticas"]
        print("=" * 65)
        print("  ESTADO SINTÁCTICO: [ PROGRAMA ACEPTADO :v ]")
        print("=" * 65)
        print(f"   • Total de Sentencias:    {stats['total_sentencias']}")
        print(f"   • Asignaciones/Pipelines: {stats['asignaciones']}")
        print(f"   • Impresiones (when):     {stats['impresiones']}")
        print(f"   • Exportaciones (guardar):{stats['guardados']}")
        print(f"   • Visualizaciones:        {stats['visualizaciones']}")
        if mostrar_arbol:
            print("\n>> Árbol de Análisis Sintáctico Jerárquico:")
            print(resultado["arbol_jerarquico"])
        if solo_validar:
            sys.exit(0)

    # 3. Ejecución Directa del Programa (Fase 2)
    visitor = VisitorEjecutor()

    try:
        visitor.visit(resultado["arbol"])
        sys.exit(0)

    except ErrorSemantico as e:
        print("\n" + "=" * 65)
        print("  ESTADO: [ ERROR SEMÁNTICO DETECTADO xd ]")
        print("=" * 65)
        print(f"  {e}")
        print("=" * 65)
        sys.exit(2)
    except Exception as e:
        print("\n" + "=" * 65)
        print(f"  [Error en Tiempo de Ejecución]: {e}")
        print("=" * 65)
        sys.exit(3)


if __name__ == "__main__":
    principal()
