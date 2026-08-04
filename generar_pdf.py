"""
Script para generar el PDF del Manual de Usuario e Intérprete del DSL LenguajeDatos xd
"""

from fpdf import FPDF
import os

class PDFManual(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, 'Manual de Usuario - DSL LenguajeDatos xd', 0, 1, 'R')
        self.set_draw_color(200, 200, 200)
        self.line(10, 20, 200, 20)
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 9)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def titulo_seccion(self, titulo):
        self.set_font('Arial', 'B', 14)
        self.set_fill_color(230, 240, 255)
        self.set_text_color(30, 60, 120)
        self.cell(0, 10, f'  {titulo}', 0, 1, 'L', True)
        self.ln(3)

    def subtitulo(self, texto):
        self.set_font('Arial', 'B', 11)
        self.set_text_color(40, 80, 150)
        self.cell(0, 8, texto, 0, 1, 'L')
        self.ln(1)

    def texto_normal(self, texto):
        self.set_font('Arial', '', 10)
        self.set_text_color(40, 40, 40)
        self.multi_cell(0, 6, texto)
        self.ln(2)

    def codigo_bloque(self, codigo):
        self.set_font('Courier', '', 9)
        self.set_fill_color(245, 245, 245)
        self.set_text_color(30, 30, 30)
        lines = codigo.strip().split('\n')
        for line in lines:
            self.cell(0, 5, f'  {line}', 0, 1, 'L', True)
        self.ln(3)


def crear_pdf_manual():
    pdf = PDFManual()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # --- PORTADA / ENCABEZADO PRINCIPAL ---
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(20, 50, 100)
    pdf.cell(0, 15, 'DSL LenguajeDatos xd', 0, 1, 'C')
    pdf.set_font('Arial', 'B', 13)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(0, 8, 'Manual Técnico de Librerías, Sintaxis y Ejecución', 0, 1, 'C')
    pdf.set_font('Arial', 'I', 10)
    pdf.cell(0, 6, 'Programa de Ciencias de la Computación e Inteligencia Artificial', 0, 1, 'C')
    pdf.cell(0, 6, 'Universidad Sergio Arboleda - Semestre 2026-2', 0, 1, 'C')
    pdf.ln(8)

    # --- SECCIÓN 1 ---
    pdf.titulo_seccion('1. Cómo Funcionan las 3 Librerías Propias')
    pdf.texto_normal(
        'El proyecto cuenta con tres librerías desarrolladas desde cero en Python puro, sin dependencias de terceos '
        '(como NumPy, Pandas o Matplotlib). Cada librería responde al sufijo _xd en sus funciones.'
    )

    pdf.subtitulo('A. matematica_propia (Reemplazo de NumPy)')
    pdf.texto_normal(
        'Maneja vectores numéricos mediante la clase Arreglo. Permite realizar aritmética elemento a elemento, '
        'máscaras booleanas para filtrado y reducciones estadísticas.'
    )
    pdf.codigo_bloque(
        'arr = Arreglo([10, 20, 30, 40])\n'
        'prom = arr.promedio_xd()           # 25.0\n'
        'desv = arr.desviacion_estandar_xd() # 12.91\n'
        'mascara = arr.mayor_que_xd(20)     # [False, False, True, True]'
    )

    pdf.subtitulo('B. datos_propios (Reemplazo de Pandas)')
    pdf.texto_normal(
        'Ofrece almacenamiento y manipulación de datos tabulares mediante las clases Serie y TablaDatos. '
        'Permite carga/escritura CSV, filtrado, selección de columnas, ordenamiento y agrupamiento.'
    )
    pdf.codigo_bloque(
        'tabla = cargar_csv_xd("datos.csv")\n'
        'tabla["total"] = tabla["unidades"].arreglo * tabla["precio"].arreglo\n'
        'sub = tabla.seleccionar_xd(["ciudad", "total"])\n'
        'res = tabla.agrupar_por_xd("ciudad").resumir_xd(total_ventas=("total", "suma"))\n'
        'guardar_csv_xd(res, "salida.csv")'
    )

    pdf.subtitulo('C. graficos_propios (Reemplazo de Matplotlib)')
    pdf.texto_normal(
        'Genera gráficos en formato SVG vectorial utilizando la clase Figura. Soporta 5 tipos de gráficas principales.'
    )
    pdf.codigo_bloque(
        'fig = crear_figura_xd(titulo="Ventas xd", etiqueta_x="Ciudad", etiqueta_y="Ventas")\n'
        'fig.graficar_barras_xd(["Bogota", "Medellin"], [3500, 2800])\n'
        'fig.guardar_svg_xd("salidas/barras.svg")'
    )

    pdf.ln(5)

    # --- SECCIÓN 2 ---
    pdf.titulo_seccion('2. Sintaxis del DSL (LenguajeDatos)')
    pdf.texto_normal(
        'El DSL es declarativo y utiliza el operador tubería (|>) para encadenar transformaciones de datos. '
        'Todas las funciones principales finalizan con el sufijo _xd.'
    )

    pdf.subtitulo('Estructura de un Programa en el DSL:')
    pdf.codigo_bloque(
        '# 1. Cargar archivo CSV\n'
        'ventas = cargar_csv_xd "datos/ventas_prueba.csv"\n\n'
        '# 2. Encadenar transformaciones con |>\n'
        'ventas_limpias = ventas \n'
        '  |> seleccionar_xd [fecha, ciudad, categoria, unidades, precio]\n'
        '  |> filtrar_xd unidades > 10\n'
        '  |> crear_columna_xd total = unidades * precio\n\n'
        '# 3. Agrupar y resumir\n'
        'resumen = ventas_limpias \n'
        '  |> agrupar_por_xd [ciudad] \n'
        '  |> resumir_xd total_ventas = suma(total), promedio_u = promedio(unidades)\n\n'
        '# 4. Guardar resultado y visualizar\n'
        'guardar_csv_xd resumen "salidas/resumen_ciudades_dsl.csv"\n'
        'graficar_barras_xd resumen titulo "Ventas por Ciudad xd" guardar "salidas/grafico.svg"'
    )

    pdf.ln(5)

    # --- SECCIÓN 3 ---
    pdf.titulo_seccion('3. Cómo Ejecutarlo ("Runearlo")')

    pdf.subtitulo('Paso 1: Ejecutar un programa .dsl desde la Consola CLI')
    pdf.texto_normal('Abre la terminal en la raíz del proyecto y ejecuta el archivo CLI del intérprete:')
    pdf.codigo_bloque('python ejecutar_dsl.py ejemplos/programa_correcto1.dsl')

    pdf.subtitulo('Paso 2: Ejecutar las Pruebas Unitarias Automatizadas')
    pdf.texto_normal('Para validar la correctitud del motor interno y del análisis sintáctico ANTLR4:')
    pdf.codigo_bloque('python -m unittest tests/test_corte1.py')

    pdf.subtitulo('Paso 3: Probar el Diagnóstico de Errores Sintácticos')
    pdf.texto_normal('Al ejecutar un archivo con errores sintácticos, el intérprete reporta la línea y columna exactas:')
    pdf.codigo_bloque('python ejecutar_dsl.py ejemplos/programa_incorrecto.dsl')

    # Guardar PDF
    ruta_pdf = 'Manual_Usuario_DSL_LenguajeDatos.pdf'
    pdf.output(ruta_pdf)
    print(f"PDF generado exitosamente en: '{ruta_pdf}' xd")
    return ruta_pdf

if __name__ == '__main__':
    crear_pdf_manual()
