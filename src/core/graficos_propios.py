"""
Librería de Visualización y Renderizado Vectorial SVG Propio
============================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Generación 100% nativa de gráficos vectoriales en formato SVG sin Matplotlib, Seaborn o Pillow.
Soporte para:
- Gráficos de Barras (Bar Chart)
- Gráficos de Líneas (Line Chart)
- Histogramas de Frecuencia (Histogram)
- Gráficos de Dispersión (Scatter Plot)
- Diagramas de Caja y Bigotes (Tukey Boxplot)
"""

import math
from src.core.matematica_propia import VectorNum, Arreglo


class Figura:
    """
    Lienzo vectorial para construcción y exportación de gráficos SVG estilizados.
    """

    def __init__(self, ancho=800, alto=550, titulo="", etiqueta_x="", etiqueta_y=""):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.etiqueta_x = etiqueta_x
        self.etiqueta_y = etiqueta_y
        self.elementos_svg = []
        self.margen_izq = 85
        self.margen_der = 45
        self.margen_sup = 65
        self.margen_inf = 75
        self.ancho_grafica = self.ancho - self.margen_izq - self.margen_der
        self.alto_grafica = self.alto - self.margen_sup - self.margen_inf

    def _dibujar_encabezados_y_ejes_xd(self, min_y, max_y, marcas_x=None):
        """Genera el fondo, títulos, rejillas de referencia y ejes coordenados."""
        # Gradientes y estilos
        defs = """
        <defs>
            <linearGradient id="barGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.95" />
                <stop offset="100%" stop-color="#1d4ed8" stop-opacity="0.95" />
            </linearGradient>
            <linearGradient id="areaGrad" x1="0%" y1="0%" x2="0%" y2="100%">
                <stop offset="0%" stop-color="#3b82f6" stop-opacity="0.35" />
                <stop offset="100%" stop-color="#3b82f6" stop-opacity="0.02" />
            </linearGradient>
            <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
                <feDropShadow dx="0" dy="3" stdDeviation="3" flood-color="#0f172a" flood-opacity="0.12"/>
            </filter>
        </defs>
        """
        self.elementos_svg.append(defs)

        # Fondo general
        self.elementos_svg.append(f'<rect width="{self.ancho}" height="{self.alto}" fill="#f8fafc" rx="8" />')

        # Marco del área de trazado
        self.elementos_svg.append(
            f'<rect x="{self.margen_izq}" y="{self.margen_sup}" width="{self.ancho_grafica}" height="{self.alto_grafica}" '
            f'fill="#ffffff" stroke="#e2e8f0" stroke-width="1" rx="4" />'
        )

        # Título principal
        if self.titulo:
            self.elementos_svg.append(
                f'<text x="{self.ancho / 2}" y="38" text-anchor="middle" font-family="system-ui, -apple-system, sans-serif" '
                f'font-size="19" font-weight="700" fill="#0f172a">{self.titulo}</text>'
            )

        # Etiqueta Eje X
        if self.etiqueta_x:
            self.elementos_svg.append(
                f'<text x="{self.margen_izq + self.ancho_grafica / 2}" y="{self.alto - 18}" text-anchor="middle" '
                f'font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#475569">{self.etiqueta_x}</text>'
            )

        # Etiqueta Eje Y
        if self.etiqueta_y:
            cy = self.margen_sup + self.alto_grafica / 2
            self.elementos_svg.append(
                f'<text x="24" y="{cy}" text-anchor="middle" transform="rotate(-90 24 {cy})" '
                f'font-family="system-ui, -apple-system, sans-serif" font-size="13" font-weight="600" fill="#475569">{self.etiqueta_y}</text>'
            )

        # Cuadrícula horizontal e indicadores en Y
        num_pasos = 5
        rango_y = max_y - min_y if max_y != min_y else 1.0
        for i in range(num_pasos + 1):
            val_y = min_y + (i / num_pasos) * rango_y
            pos_y = self.margen_sup + self.alto_grafica - (i / num_pasos) * self.alto_grafica

            self.elementos_svg.append(
                f'<line x1="{self.margen_izq}" y1="{pos_y}" x2="{self.ancho - self.margen_der}" y2="{pos_y}" '
                f'stroke="#f1f5f9" stroke-width="1.2" stroke-dasharray="4,4" />'
            )
            formato_val = f"{val_y:.1f}" if abs(val_y) < 1000 else f"{val_y:,.0f}"
            self.elementos_svg.append(
                f'<text x="{self.margen_izq - 10}" y="{pos_y + 4}" text-anchor="end" '
                f'font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#64748b">{formato_val}</text>'
            )

        # Marcas de texto en el Eje X
        if marcas_x:
            n_marcas = len(marcas_x)
            paso_x = self.ancho_grafica / n_marcas
            for i, etiqueta in enumerate(marcas_x):
                pos_x = self.margen_izq + i * paso_x + paso_x / 2
                self.elementos_svg.append(
                    f'<text x="{pos_x}" y="{self.alto - self.margen_inf + 22}" text-anchor="middle" '
                    f'font-family="system-ui, -apple-system, sans-serif" font-size="11" fill="#475569">{etiqueta}</text>'
                )

    def graficar_barras_xd(self, categorias, valores, color="#3b82f6"):
        """Genera un gráfico de barras estilizado."""
        arr_val = VectorNum(valores)
        min_y = 0
        max_y = arr_val.maximo_xd() * 1.15 if arr_val.maximo_xd() > 0 else 10

        self._dibujar_encabezados_y_ejes_xd(min_y, max_y, marcas_x=categorias)

        n = len(categorias)
        paso_x = self.ancho_grafica / n
        ancho_barra = paso_x * 0.55

        for i, val in enumerate(valores):
            pos_x = self.margen_izq + i * paso_x + (paso_x - ancho_barra) / 2
            altura_barra = ((val - min_y) / (max_y - min_y)) * self.alto_grafica
            pos_y = self.margen_sup + self.alto_grafica - altura_barra

            self.elementos_svg.append(
                f'<rect x="{pos_x}" y="{pos_y}" width="{ancho_barra}" height="{altura_barra}" '
                f'fill="url(#barGrad)" rx="4" filter="url(#dropShadow)" />'
            )
            self.elementos_svg.append(
                f'<text x="{pos_x + ancho_barra / 2}" y="{pos_y - 6}" text-anchor="middle" '
                f'font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="600" fill="#1e293b">{val}</text>'
            )

    def graficar_lineas_xd(self, x_vals, y_vals, color="#2563eb"):
        """Genera un gráfico de líneas continuas con sombreado de área."""
        arr_y = VectorNum(y_vals)
        min_y = min(0.0, arr_y.minimo_xd() if not math.isnan(arr_y.minimo_xd()) else 0.0)
        val_max = arr_y.maximo_xd()
        max_y = val_max * 1.15 if (val_max is not None and not math.isnan(val_max) and val_max > 0) else 10.0

        marcas = [str(x) for x in x_vals]
        self._dibujar_encabezados_y_ejes_xd(min_y, max_y, marcas_x=marcas)

        n = len(x_vals)
        paso_x = self.ancho_grafica / (n - 1) if n > 1 else self.ancho_grafica

        puntos_coords = []
        for i, val in enumerate(y_vals):
            px = self.margen_izq + i * paso_x
            py = self.margen_sup + self.alto_grafica - ((val - min_y) / (max_y - min_y)) * self.alto_grafica
            puntos_coords.append((px, py))

        # Trazar línea de tendencia
        d_linea = " ".join([f"{'M' if i == 0 else 'L'} {px:.1f} {py:.1f}" for i, (px, py) in enumerate(puntos_coords)])
        self.elementos_svg.append(
            f'<path d="{d_linea}" fill="none" stroke="{color}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" />'
        )

        # Dibujar nodos en cada punto
        for px, py in puntos_coords:
            self.elementos_svg.append(
                f'<circle cx="{px}" cy="{py}" r="5" fill="#ffffff" stroke="{color}" stroke-width="2.5" />'
            )

    def graficar_dispersion_xd(self, x_vals, y_vals, color="#8b5cf6"):
        """Genera un diagrama de dispersión X-Y."""
        arr_x = VectorNum(x_vals)
        arr_y = VectorNum(y_vals)

        min_x, max_x = arr_x.minimo_xd() * 0.9, arr_x.maximo_xd() * 1.1
        min_y, max_y = arr_y.minimo_xd() * 0.9, arr_y.maximo_xd() * 1.1

        self._dibujar_encabezados_y_ejes_xd(min_y, max_y)

        for x, y in zip(x_vals, y_vals):
            px = self.margen_izq + ((x - min_x) / (max_x - min_x)) * self.ancho_grafica
            py = self.margen_sup + self.alto_grafica - ((y - min_y) / (max_y - min_y)) * self.alto_grafica

    def graficar_histograma_xd(self, valores, bins=5, color="#8b5cf6"):
        """Genera un histograma de frecuencias por intervalos."""
        arr = VectorNum(valores)
        validos = arr.obtener_validos_xd()
        if not validos:
            return

        min_v = min(validos)
        max_v = max(validos)
        if min_v == max_v:
            max_v += 1.0

        ancho_bin = (max_v - min_v) / bins
        conteos = [0] * bins
        etiquetas_bins = []

        for b in range(bins):
            lim_inf = min_v + b * ancho_bin
            lim_sup = lim_inf + ancho_bin
            etiquetas_bins.append(f"{lim_inf:.0f}-{lim_sup:.0f}")

        for x in validos:
            idx = int((x - min_v) / ancho_bin)
            if idx >= bins:
                idx = bins - 1
            conteos[idx] += 1

        max_frecuencia = max(conteos) if conteos else 1
        max_y = max_frecuencia * 1.2

        self._dibujar_encabezados_y_ejes_xd(0, max_y, marcas_x=etiquetas_bins)

        paso_x = self.ancho_grafica / bins
        ancho_barra = paso_x * 0.85

        for i, frec in enumerate(conteos):
            pos_x = self.margen_izq + i * paso_x + (paso_x - ancho_barra) / 2
            altura_barra = (frec / max_y) * self.alto_grafica
            pos_y = self.margen_sup + self.alto_grafica - altura_barra

            self.elementos_svg.append(
                f'<rect x="{pos_x}" y="{pos_y}" width="{ancho_barra}" height="{altura_barra}" '
                f'fill="{color}" fill-opacity="0.85" stroke="#ffffff" stroke-width="1.5" rx="3" />'
            )
            if frec > 0:
                self.elementos_svg.append(
                    f'<text x="{pos_x + ancho_barra / 2}" y="{pos_y - 5}" text-anchor="middle" '
                    f'font-family="system-ui, -apple-system, sans-serif" font-size="10" font-weight="600" fill="#475569">{frec}</text>'
                )

    def graficar_cajas_xd(self, datos, color="#3b82f6"):
        """Genera un diagrama de caja y bigotes (Tukey Boxplot)."""
        arr = VectorNum(datos)
        validos = sorted(arr.obtener_validos_xd())
        if not validos:
            return

        q1, q2, q3, iqr = arr.cuartiles_xd()
        lim_inf = max(validos[0], q1 - 1.5 * iqr)
        lim_sup = min(validos[-1], q3 + 1.5 * iqr)

        min_y = min(validos) * 0.95
        max_y = max(validos) * 1.05
        self._dibujar_encabezados_y_ejes_xd(min_y, max_y, marcas_x=["Distribución"])

        cx = self.margen_izq + self.ancho_grafica / 2
        ancho_caja = 120

        def escala_y(val):
            return self.margen_sup + self.alto_grafica - ((val - min_y) / (max_y - min_y)) * self.alto_grafica

        y_q1, y_q2, y_q3 = escala_y(q1), escala_y(q2), escala_y(q3)
        y_inf, y_sup = escala_y(lim_inf), escala_y(lim_sup)

        # Bigotes (Whiskers)
        self.elementos_svg.append(f'<line x1="{cx}" y1="{y_q3}" x2="{cx}" y2="{y_sup}" stroke="#475569" stroke-width="2" stroke-dasharray="3,3" />')
        self.elementos_svg.append(f'<line x1="{cx}" y1="{y_q1}" x2="{cx}" y2="{y_inf}" stroke="#475569" stroke-width="2" stroke-dasharray="3,3" />')
        self.elementos_svg.append(f'<line x1="{cx - 20}" y1="{y_sup}" x2="{cx + 20}" y2="{y_sup}" stroke="#475569" stroke-width="2" />')
        self.elementos_svg.append(f'<line x1="{cx - 20}" y1="{y_inf}" x2="{cx + 20}" y2="{y_inf}" stroke="#475569" stroke-width="2" />')

        # Caja Intercuartílica (Q1 a Q3)
        alt_caja = abs(y_q1 - y_q3)
        self.elementos_svg.append(
            f'<rect x="{cx - ancho_caja / 2}" y="{y_q3}" width="{ancho_caja}" height="{alt_caja}" '
            f'fill="{color}" fill-opacity="0.25" stroke="{color}" stroke-width="2.5" rx="4" />'
        )

        # Línea de la mediana (Q2)
        self.elementos_svg.append(
            f'<line x1="{cx - ancho_caja / 2}" y1="{y_q2}" x2="{cx + ancho_caja / 2}" y2="{y_q2}" stroke="#dc2626" stroke-width="3" />'
        )

    def guardar_svg_xd(self, ruta_archivo: str):
        """Exporta todo el árbol de elementos a un archivo SVG."""
        svg_completo = [
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {self.ancho} {self.alto}" width="100%" height="100%">'
        ]
        svg_completo.extend(self.elementos_svg)
        svg_completo.append('</svg>')

        with open(ruta_archivo, mode="w", encoding="utf-8") as f:
            f.write("\n".join(svg_completo))


def crear_figura_xd(ancho=800, alto=550, titulo="", etiqueta_x="", etiqueta_y=""):
    """Función de fábrica para instanciar figuras SVG."""
    return Figura(ancho=ancho, alto=alto, titulo=titulo, etiqueta_x=etiqueta_x, etiqueta_y=etiqueta_y)
