"""
Librería Gráficos Propios (Reemplazo propio de Matplotlib desde cero en español xd)
Generación de gráficos SVG vectoriales en Python puro sin dependencias de terceros.
"""

import math
from src.core.matematica_propia import Arreglo

class Figura:
    """Clase Figura para contener y exportar gráficos xd"""
    def __init__(self, ancho=800, alto=600, titulo="", etiqueta_x="", etiqueta_y=""):
        self.ancho = ancho
        self.alto = alto
        self.titulo = titulo
        self.etiqueta_x = etiqueta_x
        self.etiqueta_y = etiqueta_y
        self.elementos_svg = []
        self.margen_izq = 80
        self.margen_der = 40
        self.margen_sup = 60
        self.margen_inf = 80
        self.ancho_grafica = self.ancho - self.margen_izq - self.margen_der
        self.alto_grafica = self.alto - self.margen_sup - self.margen_inf

    def _dibujar_fondo_y_ejes_xd(self, min_y, max_y, marcas_x=None):
        """Renderiza fondo, títulos, ejes X e Y y cuadrículas xd"""
        # Fondo blanco principal
        self.elementos_svg.append(f'<rect width="{self.ancho}" height="{self.alto}" fill="#ffffff" />')

        # Título principal
        if self.titulo:
            self.elementos_svg.append(
                f'<text x="{self.ancho / 2}" y="35" text-anchor="middle" font-family="Arial, sans-serif" '
                f'font-size="20" font-weight="bold" fill="#1e293b">{self.titulo}</text>'
            )

        # Etiquetas de Ejes
        if self.etiqueta_x:
            self.elementos_svg.append(
                f'<text x="{self.margen_izq + self.ancho_grafica / 2}" y="{self.alto - 20}" text-anchor="middle" '
                f'font-family="Arial, sans-serif" font-size="14" font-weight="600" fill="#475569">{self.etiqueta_x}</text>'
            )
        if self.etiqueta_y:
            self.elementos_svg.append(
                f'<text x="25" y="{self.margen_sup + self.alto_grafica / 2}" text-anchor="middle" '
                f'transform="rotate(-90 25 {self.margen_sup + self.alto_grafica / 2})" '
                f'font-family="Arial, sans-serif" font-size="14" font-weight="600" fill="#475569">{self.etiqueta_y}</text>'
            )

        # Ejes y Cuadrícula Y
        num_divisiones = 5
        paso_y = (max_y - min_y) / num_divisiones if max_y != min_y else 1
        for i in range(num_divisiones + 1):
            val_y = min_y + i * paso_y
            pos_y = self.margen_sup + self.alto_grafica - (i / num_divisiones) * self.alto_grafica

            self.elementos_svg.append(
                f'<line x1="{self.margen_izq}" y1="{pos_y}" x2="{self.ancho - self.margen_der}" y2="{pos_y}" '
                f'stroke="#e2e8f0" stroke-dasharray="4" />'
            )
            self.elementos_svg.append(
                f'<text x="{self.margen_izq - 10}" y="{pos_y + 4}" text-anchor="end" '
                f'font-family="Arial, sans-serif" font-size="12" fill="#64748b">{val_y:.1f}</text>'
            )

        # Línea de eje principal X e Y
        self.elementos_svg.append(
            f'<line x1="{self.margen_izq}" y1="{self.margen_sup}" x2="{self.margen_izq}" y2="{self.alto - self.margen_inf}" '
            f'stroke="#334155" stroke-width="2" />'
        )
        self.elementos_svg.append(
            f'<line x1="{self.margen_izq}" y1="{self.alto - self.margen_inf}" x2="{self.ancho - self.margen_der}" y2="{self.alto - self.margen_inf}" '
            f'stroke="#334155" stroke-width="2" />'
        )

        # Marcas en el eje X
        if marcas_x:
            n_marcas = len(marcas_x)
            ancho_paso = self.ancho_grafica / n_marcas
            for i, label in enumerate(marcas_x):
                pos_x = self.margen_izq + i * ancho_paso + ancho_paso / 2
                self.elementos_svg.append(
                    f'<text x="{pos_x}" y="{self.alto - self.margen_inf + 20}" text-anchor="middle" '
                    f'font-family="Arial, sans-serif" font-size="12" fill="#64748b">{label}</text>'
                )

    def graficar_barras_xd(self, categorias, valores, color="#3b82f6"):
        """Genera un gráfico de barras xd"""
        arr_val = Arreglo(valores)
        min_y = 0
        max_y = arr_val.maximo_xd() * 1.1 if arr_val.maximo_xd() > 0 else 10

        self._dibujar_fondo_y_ejes_xd(min_y, max_y, marcas_x=categorias)

        n = len(categorias)
        ancho_paso = self.ancho_grafica / n
        ancho_barra = ancho_paso * 0.6

        for i, val in enumerate(valores):
            pos_x = self.margen_izq + i * ancho_paso + (ancho_paso - ancho_barra) / 2
            alto_barra = (val / max_y) * self.alto_grafica if max_y > 0 else 0
            pos_y = self.alto - self.margen_inf - alto_barra

            self.elementos_svg.append(
                f'<rect x="{pos_x}" y="{pos_y}" width="{ancho_barra}" height="{alto_barra}" '
                f'fill="{color}" rx="4" stroke="#2563eb" stroke-width="1" />'
            )
            self.elementos_svg.append(
                f'<text x="{pos_x + ancho_barra / 2}" y="{pos_y - 6}" text-anchor="middle" '
                f'font-family="Arial, sans-serif" font-size="11" font-weight="bold" fill="#1e293b">{val}</text>'
            )

    def graficar_lineas_xd(self, x, y, color="#10b981", grosor=3):
        """Genera un gráfico de líneas xd"""
        arr_x = Arreglo(x)
        arr_y = Arreglo(y)

        min_x, max_x = arr_x.minimo_xd(), arr_x.maximo_xd()
        min_y, max_y = min(0, arr_y.minimo_xd()), arr_y.maximo_xd() * 1.1

        self._dibujar_fondo_y_ejes_xd(min_y, max_y, marcas_x=[str(v) for v in x])

        puntos = []
        n = len(x)
        ancho_paso = self.ancho_grafica / (n - 1) if n > 1 else self.ancho_grafica

        for i in range(n):
            pos_x = self.margen_izq + i * ancho_paso
            pos_y = self.alto - self.margen_inf - ((y[i] - min_y) / (max_y - min_y)) * self.alto_grafica
            puntos.append((pos_x, pos_y))

        str_puntos = " ".join([f"{px},{py}" for px, py in puntos])
        self.elementos_svg.append(
            f'<polyline points="{str_puntos}" fill="none" stroke="{color}" stroke-width="{grosor}" stroke-linecap="round" />'
        )

        for px, py in puntos:
            self.elementos_svg.append(
                f'<circle cx="{px}" cy="{py}" r="5" fill="{color}" stroke="#ffffff" stroke-width="2" />'
            )

    def graficar_dispersion_xd(self, x, y, color="#ef4444", radio=6):
        """Genera un gráfico de dispersión (Scatter Plot) xd"""
        arr_x = Arreglo(x)
        arr_y = Arreglo(y)

        min_x, max_x = arr_x.minimo_xd(), arr_x.maximo_xd()
        min_y, max_y = arr_y.minimo_xd(), arr_y.maximo_xd() * 1.1

        rango_x = max_x - min_x if max_x != min_x else 1
        rango_y = max_y - min_y if max_y != min_y else 1

        self._dibujar_fondo_y_ejes_xd(min_y, max_y)

        for vx, vy in zip(x, y):
            pos_x = self.margen_izq + ((vx - min_x) / rango_x) * self.ancho_grafica
            pos_y = self.alto - self.margen_inf - ((vy - min_y) / rango_y) * self.alto_grafica
            self.elementos_svg.append(
                f'<circle cx="{pos_x}" cy="{pos_y}" r="{radio}" fill="{color}" fill-opacity="0.8" stroke="#dc2626" stroke-width="1.5" />'
            )

    def graficar_histograma_xd(self, datos, bins=5, color="#8b5cf6"):
        """Genera un histograma de frecuencias xd"""
        arr = Arreglo(datos)
        min_val, max_val = arr.minimo_xd(), arr.maximo_xd()
        ancho_bin = (max_val - min_val) / bins if max_val != min_val else 1

        frecuencias = [0] * bins
        intervalos = []
        for i in range(bins):
            inf = min_val + i * ancho_bin
            sup = inf + ancho_bin
            intervalos.append(f"[{inf:.1f}-{sup:.1f}]")

        for v in datos:
            idx = int((v - min_val) / ancho_bin)
            if idx >= bins:
                idx = bins - 1
            frecuencias[idx] += 1

        self.graficar_barras_xd(intervalos, frecuencias, color=color)

    def graficar_cajas_xd(self, datos, categoria="Variable", color="#f59e0b"):
        """Genera un gráfico de cajas y bigotes (Boxplot) xd"""
        arr = Arreglo(datos)
        med = arr.mediana_xd()
        val_min = arr.minimo_xd()
        val_max = arr.maximo_xd()

        min_y = val_min * 0.9 if val_min >= 0 else val_min * 1.1
        max_y = val_max * 1.1

        self._dibujar_fondo_y_ejes_xd(min_y, max_y, marcas_x=[categoria])

        pos_x = self.margen_izq + self.ancho_grafica / 2
        ancho_caja = 100

        pos_max = self.alto - self.margen_inf - ((val_max - min_y) / (max_y - min_y)) * self.alto_grafica
        pos_min = self.alto - self.margen_inf - ((val_min - min_y) / (max_y - min_y)) * self.alto_grafica
        pos_med = self.alto - self.margen_inf - ((med - min_y) / (max_y - min_y)) * self.alto_grafica

        self.elementos_svg.append(
            f'<line x1="{pos_x}" y1="{pos_max}" x2="{pos_x}" y2="{pos_min}" stroke="#1e293b" stroke-width="2" />'
        )

        alto_caja = abs(pos_min - pos_max) * 0.5
        pos_y_caja = pos_med - alto_caja / 2
        self.elementos_svg.append(
            f'<rect x="{pos_x - ancho_caja / 2}" y="{pos_y_caja}" width="{ancho_caja}" height="{alto_caja}" '
            f'fill="{color}" fill-opacity="0.8" stroke="#d97706" stroke-width="2" rx="4" />'
        )
        self.elementos_svg.append(
            f'<line x1="{pos_x - ancho_caja / 2}" y1="{pos_med}" x2="{pos_x + ancho_caja / 2}" y2="{pos_med}" '
            f'stroke="#b45309" stroke-width="3" />'
        )

    def guardar_svg_xd(self, ruta_archivo):
        """Exporta la visualización a un archivo SVG vectorial limpio xd"""
        contenido = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.ancho}" height="{self.alto}" viewBox="0 0 {self.ancho} {self.alto}">'
        ]
        contenido.extend(self.elementos_svg)
        contenido.append('</svg>')

        with open(ruta_archivo, mode="w", encoding="utf-8") as f:
            f.write("\n".join(contenido))
        return ruta_archivo


# --- Funciones de Conveniencia del Módulo ---

def crear_figura_xd(ancho=800, alto=600, titulo="", etiqueta_x="", etiqueta_y=""):
    """Crea y retorna una nueva Figura para graficar xd"""
    return Figura(ancho=ancho, alto=alto, titulo=titulo, etiqueta_x=etiqueta_x, etiqueta_y=etiqueta_y)
