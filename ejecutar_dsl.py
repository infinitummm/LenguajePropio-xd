"""
Intérprete y Validador CLI - LenguajeMomoXD (.xd) - Corte 1
===========================================================
Asignatura: Lenguajes de Programación y Transducción
Universidad Sergio Arboleda (2026-2)

Uso:
    python ejecutar_dsl.py <ruta_archivo.xd> [--arbol]
"""

import sys
import os

from src.validador_momo_xd import validar_archivo_momo


def mostrar_banner():
    print("=" * 70)
    print("  MEME-LANG XD (MomoLang) - DSL DE CIENCIA DE DATOS Y VISUALIZACIÓN :v")
    print("  Reconocedor Léxico y Sintáctico (Corte 1) - ANTLR4 + Python")
    print("=" * 70)


def principal():
    mostrar_banner()

    if len(sys.argv) < 2:
        print("\nUso correcto:")
        print("    python ejecutar_dsl.py <archivo.xd> [--arbol]")
        print("\nEjemplos:")
        print("    python ejecutar_dsl.py ejemplos/programa_correcto1.xd")
        print("    python ejecutar_dsl.py ejemplos/programa_correcto1.xd --arbol")
        print("    python ejecutar_dsl.py ejemplos/programa_incorrecto1.xd")
        sys.exit(1)

    ruta_archivo = sys.argv[1]
    mostrar_arbol = "--arbol" in sys.argv

    if not os.path.exists(ruta_archivo):
        print(f"\n[ERROR] El archivo especificado no existe: '{ruta_archivo}' xd")
        sys.exit(1)

    print(f"\n>> Analizando archivo: {ruta_archivo}")
    resultado = validar_archivo_momo(ruta_archivo)

    print("-" * 70)
    if resultado["aceptado"]:
        print("  ESTADO: [ PROGRAMA ACEPTADO :v ]")
        print("-" * 70)
        print("  El archivo cumple al 100% las reglas léxicas y sintácticas del DSL.")
        
        stats = resultado["estadisticas"]
        print("\n>> Métricas del Código Fuente Reconocido:")
        print(f"   • Total de Sentencias:    {stats['total_sentencias']}")
        print(f"   • Asignaciones/Pipelines: {stats['asignaciones']}")
        print(f"   • Impresiones (when):     {stats['impresiones']}")
        print(f"   • Exportaciones (guardar):{stats['guardados']}")
        print(f"   • Visualizaciones:        {stats['visualizaciones']}")

        if mostrar_arbol:
            print("\n>> Árbol de Análisis Sintáctico Jerárquico:")
            print(resultado["arbol_jerarquico"])
        else:
            print("\n>> Representación LISP del Parse Tree (resumen):")
            tree_str = resultado["arbol_lisp"]
            if len(tree_str) > 200:
                print(f"   {tree_str[:200]} ... [Usa --arbol para ver el árbol completo]")
            else:
                print(f"   {tree_str}")

        print("\n" + "=" * 70)
        print("  Validación de Corte 1 exitosa. Todo correcto papu xd.")
        print("=" * 70)
        sys.exit(0)
    else:
        print("  ESTADO: [ PROGRAMA RECHAZADO xd ]")
        print("-" * 70)
        print(f"  Se encontraron {len(resultado['errores'])} error(es) en el código fuente:\n")
        for idx, err in enumerate(resultado["errores"], 1):
            print(f"  {idx}. {err['detalle']}")

        print("\n" + "=" * 70)
        print("  Corrige los errores de sintaxis indicados para que el programa sea aceptado.")
        print("=" * 70)
        sys.exit(1)


if __name__ == "__main__":
    principal()
