"""
Pruebas Léxicas, Sintácticas y de Integración para el primer corte (Corte 1 xd)
"""

import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.lexer_parser_runner import analizar_codigo_dsl, analizar_archivo_dsl
from src.visitor_ejecutor import EvaluadorDSLVisitor

class PruebaCorte1(unittest.TestCase):
    def setUp(self):
        self.ruta_ejemplo1 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ejemplos/programa_correcto1.dsl'))
        self.ruta_ejemplo2 = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ejemplos/programa_correcto2.dsl'))
        self.ruta_incorrecto = os.path.abspath(os.path.join(os.path.dirname(__file__), '../ejemplos/programa_incorrecto.dsl'))

    def test_analisis_sintactico_correcto_xd(self):
        """Valida que programas sintácticamente correctos generen 0 errores xd"""
        tree1, parser1, errores1 = analizar_archivo_dsl(self.ruta_ejemplo1)
        self.assertEqual(len(errores1), 0, f"No se esperaban errores en ejemplo 1: {errores1}")
        self.assertIsNotNone(tree1)

        tree2, parser2, errores2 = analizar_archivo_dsl(self.ruta_ejemplo2)
        self.assertEqual(len(errores2), 0, f"No se esperaban errores en ejemplo 2: {errores2}")
        self.assertIsNotNone(tree2)

    def test_analisis_sintactico_incorrecto_xd(self):
        """Valida que programas con errores sintácticos reporten mensajes claros con línea y columna xd"""
        tree, parser, errores = analizar_archivo_dsl(self.ruta_incorrecto)
        self.assertGreater(len(errores), 0, "Se esperaban errores sintácticos en el archivo incorrecto.")
        self.assertTrue(any("Línea" in err for err in errores))

    def test_ejecucion_completa_visitor_corte1_xd(self):
        """Valida la ejecución semántica del DSL de Corte 1 a través del Visitor xd"""
        tree, parser, errores = analizar_archivo_dsl(self.ruta_ejemplo1)
        self.assertEqual(len(errores), 0)

        evaluador = EvaluadorDSLVisitor()
        entorno = evaluador.visitPrograma(tree)

        self.assertIn("ventas", entorno)
        self.assertIn("ventas_limpias", entorno)
        self.assertIn("resumen_ciudad", entorno)

        # Verificar generación de archivos CSV y SVG
        self.assertTrue(os.path.exists("salidas/resumen_ciudades_dsl.csv"))
        self.assertTrue(os.path.exists("salidas/grafico_dsl_barras.svg"))

if __name__ == '__main__':
    unittest.main()
