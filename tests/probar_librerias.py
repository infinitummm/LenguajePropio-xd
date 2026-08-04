"""
Pruebas Unitarias para las Librerías Propias en Español xd
"""

import os
import unittest
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.core.matematica_propia import Arreglo, crear_arreglo_xd, rango_xd
from src.core.datos_propios import TablaDatos, cargar_csv_xd, guardar_csv_xd
from src.core.graficos_propios import Figura, crear_figura_xd

class PruebaMatematicaPropia(unittest.TestCase):
    def test_operaciones_basicas_xd(self):
        arr1 = Arreglo([10, 20, 30])
        arr2 = Arreglo([2, 4, 5])

        self.assertEqual((arr1 + arr2).datos, [12, 24, 35])
        self.assertEqual((arr1 - arr2).datos, [8, 16, 25])
        self.assertEqual((arr1 * arr2).datos, [20, 80, 150])
        self.assertEqual((arr1 / arr2).datos, [5.0, 5.0, 6.0])

    def test_estadisticas_xd(self):
        arr = Arreglo([10, 20, 30, 40, 50])
        self.assertEqual(arr.suma_xd(), 150)
        self.assertEqual(arr.promedio_xd(), 30.0)
        self.assertEqual(arr.mediana_xd(), 30.0)
        self.assertEqual(arr.minimo_xd(), 10)
        self.assertEqual(arr.maximo_xd(), 50)
        self.assertAlmostEqual(arr.desviacion_estandar_xd(), 15.8113883, places=4)


class PruebaDatosPropios(unittest.TestCase):
    def setUp(self):
        self.ruta_csv = os.path.abspath(os.path.join(os.path.dirname(__file__), '../datos/ventas_prueba.csv'))

    def test_cargar_y_filtrar_csv_xd(self):
        tabla = cargar_csv_xd(self.ruta_csv)
        self.assertGreater(tabla.numero_filas, 0)
        self.assertIn("ciudad", tabla.nombres_columnas)

        unidades = tabla["unidades"].arreglo
        mascara = unidades.mayor_que_xd(15)
        tabla_filtrada = tabla.filtrar_xd(mascara)
        self.assertTrue(all(u > 15 for u in tabla_filtrada["unidades"].datos))

    def test_agrupar_por_xd(self):
        tabla = cargar_csv_xd(self.ruta_csv)
        unidades = tabla["unidades"].arreglo
        precio = tabla["precio"].arreglo
        tabla["total"] = unidades * precio

        agrupado = tabla.agrupar_por_xd("ciudad").resumir_xd(
            total_ventas=("total", "suma"),
            promedio_unidades=("unidades", "promedio")
        )
        self.assertIn("total_ventas", agrupado.nombres_columnas)
        self.assertGreater(agrupado.numero_filas, 0)


class PruebaGraficosPropios(unittest.TestCase):
    def test_generacion_graficos_svg_xd(self):
        ruta_salida = os.path.abspath(os.path.join(os.path.dirname(__file__), 'grafico_test.svg'))
        fig = crear_figura_xd(titulo="Ventas por Ciudad xd", etiqueta_x="Ciudad", etiqueta_y="Ventas")
        fig.graficar_barras_xd(["Bogota", "Medellin", "Cali"], [1000, 1500, 800])
        fig.guardar_svg_xd(ruta_salida)

        self.assertTrue(os.path.exists(ruta_salida))
        with open(ruta_salida, 'r', encoding='utf-8') as f:
            contenido = f.read()
            self.assertIn("<svg", contenido)
            self.assertIn("Bogota", contenido)

        if os.path.exists(ruta_salida):
            os.remove(ruta_salida)

if __name__ == '__main__':
    unittest.main()
