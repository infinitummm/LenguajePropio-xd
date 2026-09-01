"""
Suite de Pruebas Léxicas y Sintácticas - Corte 1
================================================
Asignatura: Lenguajes de Programación y Transducción
Universidad Sergio Arboleda (2026-2)

Objetivo:
Validar que el front-end de MomoLang XD (.xd) acepte todos los programas
sintácticamente válidos y rechace con precisión diagnóstica los programas mal formados.
"""

import os
import sys
import unittest

# Asegurar importación de módulos del proyecto
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.validador_momo_xd import validar_codigo_momo, validar_archivo_momo


class TestCorte1FrontEnd(unittest.TestCase):

    def setUp(self):
        self.ruta_correcto1 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../ejemplos/programa_correcto1.xd')
        )
        self.ruta_correcto2 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../ejemplos/programa_correcto2.xd')
        )
        self.ruta_incorrecto1 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../ejemplos/programa_incorrecto1.xd')
        )
        self.ruta_incorrecto2 = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '../ejemplos/programa_incorrecto2.xd')
        )

    # -------------------------------------------------------------------------
    # 1. Pruebas de Aceptación (Programas Válidos)
    # -------------------------------------------------------------------------

    def test_aceptar_programa_correcto_1_xd(self):
        """Valida que el programa de ventas completo sea aceptado sin errores."""
        resultado = validar_archivo_momo(self.ruta_correcto1)
        self.assertTrue(resultado["aceptado"], f"Errores encontrados: {resultado['errores']}")
        self.assertEqual(len(resultado["errores"]), 0)
        self.assertIsNotNone(resultado["arbol"])
        self.assertGreater(resultado["estadisticas"]["total_sentencias"], 0)
        self.assertEqual(resultado["estadisticas"]["total_sentencias"], 7)

    def test_aceptar_programa_correcto_2_xd(self):
        """Valida que el programa de análisis exploratorio sea aceptado sin errores."""
        resultado = validar_archivo_momo(self.ruta_correcto2)
        self.assertTrue(resultado["aceptado"], f"Errores encontrados: {resultado['errores']}")
        self.assertEqual(len(resultado["errores"]), 0)
        self.assertIsNotNone(resultado["arbol"])
        self.assertEqual(resultado["estadisticas"]["total_sentencias"], 6)

    def test_aceptar_sentencia_imprimir_when_haces_xd(self):
        """Valida la sintaxis de 'when haces' para imprimir textos y expresiones."""
        codigo = 'when haces "Hola mundo grasoso papu" xd\nwhen haces 42 + 8 xd\n'
        resultado = validar_codigo_momo(codigo)
        self.assertTrue(resultado["aceptado"])
        self.assertEqual(resultado["estadisticas"]["impresiones"], 2)

    def test_aceptar_pipeline_completo_con_operador_momo_xd(self):
        """Valida encadenamientos con el operador de tubería |:v>."""
        codigo = (
            'df = pasa_el_pack "datos.csv" xd\n'
            'df_filtrado = df\n'
            '    |:v> escojo_a [edad, salario]\n'
            '    |:v> but_te_enteras_que edad >= 18\n'
            '    |:v> el_futuro_es_hoy_oiste_viejo bono = salario * 0.10 xd\n'
        )
        resultado = validar_codigo_momo(codigo)
        self.assertTrue(resultado["aceptado"])
        self.assertEqual(resultado["estadisticas"]["asignaciones"], 2)

    def test_aceptar_instrucciones_visualizacion_todas_xd(self):
        """Valida que todos los tipos de gráficos sean reconocidos sintácticamente."""
        codigo = (
            'graficar_momos_en_barras df titulo "Barras" eje_x "X" eje_y "Y" guardar "b.svg" xd\n'
            'graficar_momos_en_lineas df titulo "Lineas" guardar "l.svg" xd\n'
            'graficar_momos_en_histograma df titulo "Histo" xd\n'
            'graficar_momos_en_dispersion df titulo "Disp" eje_x "A" eje_y "B" xd\n'
            'graficar_momos_en_cajas df titulo "Cajas" xd\n'
        )
        resultado = validar_codigo_momo(codigo)
        self.assertTrue(resultado["aceptado"])
        self.assertEqual(resultado["estadisticas"]["visualizaciones"], 5)

    # -------------------------------------------------------------------------
    # 2. Pruebas de Rechazo (Programas Inválidos)
    # -------------------------------------------------------------------------

    def test_rechazar_programa_sin_terminador_xd(self):
        """Valida el rechazo estricto cuando se omite 'xd' al final de la sentencia."""
        resultado = validar_archivo_momo(self.ruta_incorrecto1)
        self.assertFalse(resultado["aceptado"])
        self.assertGreater(len(resultado["errores"]), 0)
        self.assertTrue(any(e["linea"] > 0 for e in resultado["errores"]))

    def test_rechazar_programa_con_sintaxis_corrupta_xd(self):
        """Valida el rechazo de expresiones mal formadas en pipelines."""
        resultado = validar_archivo_momo(self.ruta_incorrecto2)
        self.assertFalse(resultado["aceptado"])
        self.assertGreater(len(resultado["errores"]), 0)

    def test_rechazar_operador_relacional_faltante_xd(self):
        """Valida que una comparación sin operador relacional sea rechazada."""
        codigo = 'df2 = df |:v> but_te_enteras_que precio xd\n'
        resultado = validar_codigo_momo(codigo)
        self.assertFalse(resultado["aceptado"])
        self.assertGreater(len(resultado["errores"]), 0)

    def test_rechazar_palabra_desconocida_o_token_invalido_xd(self):
        """Valida el rechazo cuando se usan sentencias no reconocidas."""
        codigo = 'instruccion_inventada_que_no_existe "test" xd\n'
        resultado = validar_codigo_momo(codigo)
        self.assertFalse(resultado["aceptado"])
        self.assertGreater(len(resultado["errores"]), 0)


if __name__ == '__main__':
    unittest.main()
