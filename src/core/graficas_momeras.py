"""
Librería de Visualización Propia - graficas_momeras
===================================================
Asignatura: Lenguajes de Programación y Transducción (2026-2)
Universidad Sergio Arboleda

Implementación de visualización 100% nativa en Python puro:
- Cero librerías externas (sin Matplotlib, sin Pillow, sin Pandas, sin SVG).
- Rasterizador 2D propio (algoritmo de Bresenham, polígonos, círculos y rectángulos).
- Motor de fuentes bitmap matricial 5x7 en píxeles puros.
- Codificador de imágenes PNG estándar mediante compresión DEFLATE (módulo zlib).
- Generación de gráficos: Barras, Líneas, Dispersión, Histograma y Cajas.
"""

import math
import os
import struct
import zlib


# =============================================================================
# 1. CODIFICADOR PNG NATIVO (100% Python Estándar)
# =============================================================================

def _crear_chunk_png(tipo_chunk: bytes, datos: bytes) -> bytes:
    """Empaqueta un chunk PNG con longitud, tipo, payload y CRC32."""
    longitud = struct.pack(">I", len(datos))
    crc = zlib.crc32(tipo_chunk + datos) & 0xFFFFFFFF
    crc_bytes = struct.pack(">I", crc)
    return longitud + tipo_chunk + datos + crc_bytes


def codificar_a_png(ancho: int, alto: int, matriz_rgb: list[list[tuple[int, int, int]]]) -> bytes:
    """
    Convierte una matriz 2D de píxeles (R, G, B) a un archivo PNG válido en bytes.
    Sigue la especificación RFC 2083 (PNG 1.2).
    """
    # Firma de 8 bytes oficial de PNG
    firma = b"\x89PNG\r\n\x1a\n"

    # Chunk IHDR: ancho (4B), alto (4B), bitDepth (8), colorType (2=RGB), comp (0), filter (0), interlace (0)
    ihdr_datos = struct.pack(">IIBBBBB", ancho, alto, 8, 2, 0, 0, 0)
    ihdr_chunk = _crear_chunk_png(b"IHDR", ihdr_datos)

    # Construcción de scanlines con byte de filtro 0 (None) al inicio de cada fila
    lineas = bytearray()
    for y in range(alto):
        lineas.append(0)  # Filtro 0 para la fila
        fila = matriz_rgb[y]
        for x in range(ancho):
            r, g, b = fila[x]
            lineas.append(max(0, min(255, int(r))))
            lineas.append(max(0, min(255, int(g))))
            lineas.append(max(0, min(255, int(b))))

    # Compresión DEFLATE zlib estándar
    datos_comprimidos = zlib.compress(bytes(lineas), level=6)
    idat_chunk = _crear_chunk_png(b"IDAT", datos_comprimidos)

    # Chunk IEND
    iend_chunk = _crear_chunk_png(b"IEND", b"")

    return firma + ihdr_chunk + idat_chunk + iend_chunk


# =============================================================================
# 2. TIPOGRAFÍA BITMAP MATRICIAL 5x7
# =============================================================================

# Cada glifo se define en una matriz de 7 filas de 5 bits cada una
FUENTES_BITMAP = {
    ' ': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00],
    '!': [0x04, 0x04, 0x04, 0x04, 0x00, 0x00, 0x04],
    '"': [0x0A, 0x0A, 0x0A, 0x00, 0x00, 0x00, 0x00],
    '#': [0x0A, 0x0A, 0x1F, 0x0A, 0x1F, 0x0A, 0x0A],
    '$': [0x04, 0x0F, 0x14, 0x0E, 0x05, 0x1E, 0x04],
    '%': [0x19, 0x19, 0x02, 0x04, 0x08, 0x13, 0x13],
    '&': [0x0C, 0x12, 0x14, 0x08, 0x15, 0x12, 0x0D],
    '\'': [0x04, 0x04, 0x02, 0x00, 0x00, 0x00, 0x00],
    '(': [0x02, 0x04, 0x08, 0x08, 0x08, 0x04, 0x02],
    ')': [0x08, 0x04, 0x02, 0x02, 0x02, 0x04, 0x08],
    '*': [0x00, 0x04, 0x15, 0x0E, 0x15, 0x04, 0x00],
    '+': [0x00, 0x04, 0x04, 0x1F, 0x04, 0x04, 0x00],
    ',': [0x00, 0x00, 0x00, 0x00, 0x04, 0x04, 0x08],
    '-': [0x00, 0x00, 0x00, 0x1F, 0x00, 0x00, 0x00],
    '.': [0x00, 0x00, 0x00, 0x00, 0x00, 0x06, 0x06],
    '/': [0x01, 0x02, 0x04, 0x08, 0x10, 0x00, 0x00],
    '0': [0x0E, 0x11, 0x13, 0x15, 0x19, 0x11, 0x0E],
    '1': [0x04, 0x0C, 0x04, 0x04, 0x04, 0x04, 0x0E],
    '2': [0x0E, 0x11, 0x01, 0x06, 0x08, 0x10, 0x1F],
    '3': [0x1F, 0x02, 0x04, 0x02, 0x01, 0x11, 0x0E],
    '4': [0x02, 0x06, 0x0A, 0x12, 0x1F, 0x02, 0x02],
    '5': [0x1F, 0x10, 0x1E, 0x01, 0x01, 0x11, 0x0E],
    '6': [0x06, 0x08, 0x10, 0x1E, 0x11, 0x11, 0x0E],
    '7': [0x1F, 0x01, 0x02, 0x04, 0x08, 0x08, 0x08],
    '8': [0x0E, 0x11, 0x11, 0x0E, 0x11, 0x11, 0x0E],
    '9': [0x0E, 0x11, 0x11, 0x0F, 0x01, 0x02, 0x0C],
    ':': [0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x0C, 0x00],
    ';': [0x00, 0x0C, 0x0C, 0x00, 0x0C, 0x04, 0x08],
    '<': [0x02, 0x04, 0x08, 0x10, 0x08, 0x04, 0x02],
    '=': [0x00, 0x1F, 0x00, 0x1F, 0x00, 0x00, 0x00],
    '>': [0x08, 0x04, 0x02, 0x01, 0x02, 0x04, 0x08],
    '?': [0x0E, 0x11, 0x01, 0x02, 0x04, 0x00, 0x04],
    '@': [0x0E, 0x11, 0x01, 0x0D, 0x15, 0x15, 0x0E],
    'A': [0x0E, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11],
    'B': [0x1E, 0x11, 0x11, 0x1E, 0x11, 0x11, 0x1E],
    'C': [0x0E, 0x11, 0x10, 0x10, 0x10, 0x11, 0x0E],
    'D': [0x1C, 0x12, 0x11, 0x11, 0x11, 0x12, 0x1C],
    'E': [0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x1F],
    'F': [0x1F, 0x10, 0x10, 0x1E, 0x10, 0x10, 0x10],
    'G': [0x0E, 0x11, 0x10, 0x17, 0x11, 0x11, 0x0F],
    'H': [0x11, 0x11, 0x11, 0x1F, 0x11, 0x11, 0x11],
    'I': [0x0E, 0x04, 0x04, 0x04, 0x04, 0x04, 0x0E],
    'J': [0x07, 0x02, 0x02, 0x02, 0x02, 0x12, 0x0C],
    'K': [0x11, 0x12, 0x14, 0x18, 0x14, 0x12, 0x11],
    'L': [0x10, 0x10, 0x10, 0x10, 0x10, 0x10, 0x1F],
    'M': [0x11, 0x1B, 0x15, 0x11, 0x11, 0x11, 0x11],
    'N': [0x11, 0x19, 0x15, 0x13, 0x11, 0x11, 0x11],
    'O': [0x0E, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E],
    'P': [0x1E, 0x11, 0x11, 0x1E, 0x10, 0x10, 0x10],
    'Q': [0x0E, 0x11, 0x11, 0x11, 0x15, 0x12, 0x0D],
    'R': [0x1E, 0x11, 0x11, 0x1E, 0x14, 0x12, 0x11],
    'S': [0x0E, 0x11, 0x10, 0x0E, 0x01, 0x11, 0x0E],
    'T': [0x1F, 0x04, 0x04, 0x04, 0x04, 0x04, 0x04],
    'U': [0x11, 0x11, 0x11, 0x11, 0x11, 0x11, 0x0E],
    'V': [0x11, 0x11, 0x11, 0x11, 0x11, 0x0A, 0x04],
    'W': [0x11, 0x11, 0x11, 0x15, 0x15, 0x1B, 0x11],
    'X': [0x11, 0x11, 0x0A, 0x04, 0x0A, 0x11, 0x11],
    'Y': [0x11, 0x11, 0x0A, 0x04, 0x04, 0x04, 0x04],
    'Z': [0x1F, 0x01, 0x02, 0x04, 0x08, 0x10, 0x1F],
    '_': [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x1F],
    '[': [0x0E, 0x08, 0x08, 0x08, 0x08, 0x08, 0x0E],
    ']': [0x0E, 0x02, 0x02, 0x02, 0x02, 0x02, 0x0E],
}


# =============================================================================
# 3. LIENZO Y RASTERIZADOR 2D (LienzoMomo)
# =============================================================================

class LienzoMomo:
    """Lienzo 2D matricial que soporta trazado vectorial y exportación PNG directa."""

    def __init__(self, ancho: int = 700, alto: int = 450, color_fondo=(250, 250, 252)):
        self.ancho = ancho
        self.alto = alto
        self.color_fondo = color_fondo
        self.pixeles = [[color_fondo for _ in range(ancho)] for _ in range(alto)]

    def poner_pixel(self, x: int, y: int, color: tuple[int, int, int]):
        """Pinta un píxel si está dentro de los límites del lienzo."""
        ix, iy = int(round(x)), int(round(y))
        if 0 <= ix < self.ancho and 0 <= iy < self.alto:
            self.pixeles[iy][ix] = color

    def dibujar_linea(self, x0: int, y0: int, x1: int, y1: int, color=(40, 40, 40), grosor: int = 1):
        """Algoritmo de Bresenham para trazar líneas de cualquier pendiente con grosor."""
        x0, y0, x1, y1 = int(round(x0)), int(round(y0)), int(round(x1)), int(round(y1))
        dx = abs(x1 - x0)
        dy = -abs(y1 - y0)
        sx = 1 if x0 < x1 else -1
        sy = 1 if y0 < y1 else -1
        err = dx + dy

        while True:
            if grosor <= 1:
                self.poner_pixel(x0, y0, color)
            else:
                radio = grosor // 2
                for gx in range(-radio, radio + 1):
                    for gy in range(-radio, radio + 1):
                        self.poner_pixel(x0 + gx, y0 + gy, color)

            if x0 == x1 and y0 == y1:
                break
            e2 = 2 * err
            if e2 >= dy:
                err += dy
                x0 += sx
            if e2 <= dx:
                err += dx
                y0 += sy

    def dibujar_rectangulo(self, x: int, y: int, ancho: int, alto: int, color_relleno=None, color_borde=None):
        """Dibuja un rectángulo con relleno opcional y borde opcional."""
        x, y, ancho, alto = int(x), int(y), int(ancho), int(alto)
        x_fin = x + ancho
        y_fin = y + alto

        if color_relleno:
            for py in range(max(0, y), min(self.alto, y_fin)):
                for px in range(max(0, x), min(self.ancho, x_fin)):
                    self.pixeles[py][px] = color_relleno

        if color_borde:
            for px in range(max(0, x), min(self.ancho, x_fin)):
                self.poner_pixel(px, y, color_borde)
                self.poner_pixel(px, y_fin - 1, color_borde)
            for py in range(max(0, y), min(self.alto, y_fin)):
                self.poner_pixel(x, py, color_borde)
                self.poner_pixel(x_fin - 1, py, color_borde)

    def dibujar_circulo(self, cx: int, cy: int, radio: int, color_relleno=None, color_borde=None):
        """Dibuja un círculo relleno o bordeado centrado en (cx, cy)."""
        cx, cy, radio = int(round(cx)), int(round(cy)), int(round(radio))
        for y in range(cy - radio, cy + radio + 1):
            for x in range(cx - radio, cx + radio + 1):
                dist_sq = (x - cx) ** 2 + (y - cy) ** 2
                if color_relleno and dist_sq <= radio ** 2:
                    self.poner_pixel(x, y, color_relleno)
                elif color_borde and (radio - 1) ** 2 <= dist_sq <= radio ** 2:
                    self.poner_pixel(x, y, color_borde)

    def dibujar_texto(self, texto: str, x: int, y: int, color=(30, 30, 30), escala: int = 1):
        """Dibuja texto mediante fuente matricial 5x7."""
        texto_str = str(texto).upper()
        cursor_x = int(x)
        cursor_y = int(y)

        for car in texto_str:
            glifo = FUENTES_BITMAP.get(car, FUENTES_BITMAP.get('?', [0] * 7))
            for fila_idx, fila_bits in enumerate(glifo):
                for col_idx in range(5):
                    # El bit 4 es el de la izquierda (0b10000)
                    bit = (fila_bits >> (4 - col_idx)) & 1
                    if bit:
                        for ey in range(escala):
                            for ex in range(escala):
                                px = cursor_x + (col_idx * escala) + ex
                                py = cursor_y + (fila_idx * escala) + ey
                                self.poner_pixel(px, py, color)
            cursor_x += (5 + 1) * escala  # 5 de ancho + 1 de espaciado

    def exportar_png(self, ruta_archivo: str):
        """Codifica y guarda el lienzo en formato PNG estándar."""
        directorio = os.path.dirname(ruta_archivo)
        if directorio and not os.path.exists(directorio):
            os.makedirs(directorio, exist_ok=True)

        datos_png = codificar_a_png(self.ancho, self.alto, self.pixeles)
        with open(ruta_archivo, "wb") as f:
            f.write(datos_png)


# =============================================================================
# 4. GENERADORES DE GRÁFICAS DE DOMINIO MOMERO
# =============================================================================

PALETA_MOMERA = [
    (30, 136, 229),   # Azul primario Momo
    (251, 140, 0),    # Naranja grasoso
    (67, 160, 71),    # Verde prro
    (142, 36, 170),   # Morado epico
    (229, 57, 53),    # Rojo peligro
    (0, 172, 193),    # Cyan fresco
    (109, 76, 65),    # Cafe papu
    (57, 73, 171),    # Indigo legendario
]


def _extraer_datos(tabla, col_x, col_y=None):
    """Extrae valores de las columnas seleccionadas de una TablaMomo."""
    cols_disp = tabla.columnas if hasattr(tabla, 'columnas') else list(tabla.keys())
    if col_x not in cols_disp:
        raise ValueError(f"Columna eje X '{col_x}' no existe. Disponibles: {cols_disp}")
    valores_x = tabla[col_x].datos if hasattr(tabla[col_x], 'datos') else list(tabla[col_x])

    valores_y = None
    if col_y:
        if col_y not in cols_disp:
            raise ValueError(f"Columna eje Y '{col_y}' no existe. Disponibles: {cols_disp}")
        valores_y = tabla[col_y].datos if hasattr(tabla[col_y], 'datos') else list(tabla[col_y])

    return valores_x, valores_y


def graficar_barras(tabla, col_x: str, col_y: str, titulo: str = "Grafico de Barras",
                    eje_x: str = "", eje_y: str = "", ruta_salida: str = "salidas/grafico_barras.png"):
    """Genera y exporta un gráfico de barras a PNG."""
    vx, vy = _extraer_datos(tabla, col_x, col_y)
    pares = []
    for x_val, y_val in zip(vx, vy):
        if y_val is not None:
            try:
                pares.append((str(x_val), float(y_val)))
            except (ValueError, TypeError):
                continue

    if not pares:
        raise ValueError("No hay datos numéricos válidos para graficar barras.")

    ancho_lienzo, alto_lienzo = 720, 460
    lienzo = LienzoMomo(ancho_lienzo, alto_lienzo)

    # Márgenes de trazado
    m_izq, m_der, m_sup, m_inf = 75, 40, 60, 70
    x_origen = m_izq
    y_origen = alto_lienzo - m_inf
    ancho_util = ancho_lienzo - m_izq - m_der
    alto_util = y_origen - m_sup

    max_y = max(p[1] for p in pares)
    if max_y <= 0:
        max_y = 1.0
    # Redondeo superior amigable para escala
    cota_superior = max_y * 1.15

    # Dibujar título
    lienzo.dibujar_texto(titulo, m_izq + 10, 20, color=(20, 25, 40), escala=2)

    # Rejilla y etiquetas Y
    num_divisiones = 5
    for i in range(num_divisiones + 1):
        frac = i / num_divisiones
        val = frac * cota_superior
        py = int(y_origen - (frac * alto_util))
        # Línea de guía
        lienzo.dibujar_linea(x_origen, py, x_origen + ancho_util, py, color=(225, 230, 238), grosor=1)
        # Etiqueta numérica Y
        texto_y = f"{val:.1f}" if cota_superior < 100 else f"{int(val)}"
        lienzo.dibujar_texto(texto_y, 10, py - 4, color=(100, 110, 130), escala=1)

    # Ejes X e Y
    lienzo.dibujar_linea(x_origen, y_origen, x_origen + ancho_util, y_origen, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(x_origen, y_origen, x_origen, m_sup - 10, color=(50, 60, 80), grosor=2)

    # Títulos de ejes
    if eje_x:
        lienzo.dibujar_texto(eje_x, x_origen + (ancho_util // 2) - (len(eje_x) * 3), alto_lienzo - 25, color=(50, 60, 80), escala=1)
    if eje_y:
        lienzo.dibujar_texto(eje_y, m_izq, m_sup - 25, color=(50, 60, 80), escala=1)

    # Trazado de barras
    num_barras = len(pares)
    ancho_slot = ancho_util / num_barras
    ancho_barra = max(10, int(ancho_slot * 0.65))

    for idx, (etiqueta, valor) in enumerate(pares):
        cx = x_origen + int((idx + 0.5) * ancho_slot)
        bx = cx - (ancho_barra // 2)
        h_barra = int((valor / cota_superior) * alto_util)
        by = y_origen - h_barra
        color_barra = PALETA_MOMERA[idx % len(PALETA_MOMERA)]

        # Rectángulo relleno de la barra
        lienzo.dibujar_rectangulo(bx, by, ancho_barra, h_barra, color_relleno=color_barra, color_borde=(30, 40, 60))

        # Etiqueta de valor encima de la barra
        txt_val = f"{valor:.1f}" if valor < 100 else f"{int(valor)}"
        lienzo.dibujar_texto(txt_val, bx + max(0, (ancho_barra - len(txt_val) * 6) // 2), by - 12, color=(40, 50, 70), escala=1)

        # Etiqueta de categoría en eje X
        etq_corta = etiqueta[:8]
        lienzo.dibujar_texto(etq_corta, bx + max(0, (ancho_barra - len(etq_corta) * 6) // 2), y_origen + 10, color=(50, 60, 80), escala=1)

    lienzo.exportar_png(ruta_salida)
    return ruta_salida


def graficar_lineas(tabla, col_x: str, col_y: str, titulo: str = "Grafico de Lineas",
                    eje_x: str = "", eje_y: str = "", ruta_salida: str = "salidas/grafico_lineas.png"):
    """Genera y exporta un gráfico de líneas a PNG."""
    vx, vy = _extraer_datos(tabla, col_x, col_y)
    puntos = []
    for x_val, y_val in zip(vx, vy):
        if y_val is not None:
            try:
                puntos.append((str(x_val), float(y_val)))
            except (ValueError, TypeError):
                continue

    if not puntos:
        raise ValueError("No hay datos numéricos válidos para graficar líneas.")

    ancho_lienzo, alto_lienzo = 720, 460
    lienzo = LienzoMomo(ancho_lienzo, alto_lienzo)

    m_izq, m_der, m_sup, m_inf = 75, 40, 60, 70
    x_origen = m_izq
    y_origen = alto_lienzo - m_inf
    ancho_util = ancho_lienzo - m_izq - m_der
    alto_util = y_origen - m_sup

    max_y = max(p[1] for p in puntos)
    min_y = min(p[1] for p in puntos)
    rango_y = (max_y - min_y) if (max_y - min_y) > 0 else 1.0
    cota_inf = max(0.0, min_y - rango_y * 0.1)
    cota_sup = max_y + rango_y * 0.1

    lienzo.dibujar_texto(titulo, m_izq + 10, 20, color=(20, 25, 40), escala=2)

    num_div = 5
    for i in range(num_div + 1):
        frac = i / num_div
        val = cota_inf + frac * (cota_sup - cota_inf)
        py = int(y_origen - (frac * alto_util))
        lienzo.dibujar_linea(x_origen, py, x_origen + ancho_util, py, color=(225, 230, 238), grosor=1)
        txt_y = f"{val:.1f}" if (cota_sup - cota_inf) < 100 else f"{int(val)}"
        lienzo.dibujar_texto(txt_y, 10, py - 4, color=(100, 110, 130), escala=1)

    lienzo.dibujar_linea(x_origen, y_origen, x_origen + ancho_util, y_origen, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(x_origen, y_origen, x_origen, m_sup - 10, color=(50, 60, 80), grosor=2)

    if eje_x:
        lienzo.dibujar_texto(eje_x, x_origen + (ancho_util // 2) - (len(eje_x) * 3), alto_lienzo - 25, color=(50, 60, 80), escala=1)
    if eje_y:
        lienzo.dibujar_texto(eje_y, m_izq, m_sup - 25, color=(50, 60, 80), escala=1)

    coords_pixeles = []
    n_pts = len(puntos)
    paso_x = ancho_util / (n_pts - 1) if n_pts > 1 else ancho_util / 2

    for idx, (etq, val) in enumerate(puntos):
        px = int(x_origen + idx * paso_x) if n_pts > 1 else int(x_origen + paso_x)
        py = int(y_origen - ((val - cota_inf) / (cota_sup - cota_inf)) * alto_util)
        coords_pixeles.append((px, py, etq, val))

    # Trazar segmentos conectores
    for i in range(len(coords_pixeles) - 1):
        x_a, y_a, _, _ = coords_pixeles[i]
        x_b, y_b, _, _ = coords_pixeles[i + 1]
        lienzo.dibujar_linea(x_a, y_a, x_b, y_b, color=(30, 136, 229), grosor=3)

    # Trazar nodos y etiquetas
    for px, py, etq, val in coords_pixeles:
        lienzo.dibujar_circulo(px, py, radio=5, color_relleno=(251, 140, 0), color_borde=(30, 40, 60))
        txt_val = f"{val:.1f}" if val < 100 else f"{int(val)}"
        lienzo.dibujar_texto(txt_val, px - 10, py - 16, color=(30, 40, 60), escala=1)
        lienzo.dibujar_texto(etq[:6], px - 12, y_origen + 10, color=(60, 70, 90), escala=1)

    lienzo.exportar_png(ruta_salida)
    return ruta_salida


def graficar_dispersion(tabla, col_x: str, col_y: str, titulo: str = "Grafico de Dispersion",
                        eje_x: str = "", eje_y: str = "", ruta_salida: str = "salidas/grafico_dispersion.png"):
    """Genera y exporta un gráfico de dispersión (Scatter plot) a PNG."""
    vx, vy = _extraer_datos(tabla, col_x, col_y)
    puntos = []
    for x_val, y_val in zip(vx, vy):
        if x_val is not None and y_val is not None:
            try:
                puntos.append((float(x_val), float(y_val)))
            except (ValueError, TypeError):
                continue

    if not puntos:
        raise ValueError("No hay pares numéricos (X, Y) válidos para dispersión.")

    ancho_lienzo, alto_lienzo = 720, 460
    lienzo = LienzoMomo(ancho_lienzo, alto_lienzo)

    m_izq, m_der, m_sup, m_inf = 75, 40, 60, 60
    x_origen = m_izq
    y_origen = alto_lienzo - m_inf
    ancho_util = ancho_lienzo - m_izq - m_der
    alto_util = y_origen - m_sup

    min_x, max_x = min(p[0] for p in puntos), max(p[0] for p in puntos)
    min_y, max_y = min(p[1] for p in puntos), max(p[1] for p in puntos)
    rx = (max_x - min_x) if (max_x - min_x) > 0 else 1.0
    ry = (max_y - min_y) if (max_y - min_y) > 0 else 1.0

    cota_x_min, cota_x_max = min_x - rx * 0.08, max_x + rx * 0.08
    cota_y_min, cota_y_max = min_y - ry * 0.08, max_y + ry * 0.08

    lienzo.dibujar_texto(titulo, m_izq + 10, 20, color=(20, 25, 40), escala=2)

    # Rejilla
    num_div = 5
    for i in range(num_div + 1):
        frac = i / num_div
        vy_val = cota_y_min + frac * (cota_y_max - cota_y_min)
        py = int(y_origen - frac * alto_util)
        lienzo.dibujar_linea(x_origen, py, x_origen + ancho_util, py, color=(225, 230, 238), grosor=1)
        txt_y = f"{vy_val:.1f}" if (cota_y_max - cota_y_min) < 100 else f"{int(vy_val)}"
        lienzo.dibujar_texto(txt_y, 10, py - 4, color=(100, 110, 130), escala=1)

        vx_val = cota_x_min + frac * (cota_x_max - cota_x_min)
        px = int(x_origen + frac * ancho_util)
        lienzo.dibujar_linea(px, y_origen, px, m_sup, color=(235, 240, 246), grosor=1)
        txt_x = f"{vx_val:.1f}" if (cota_x_max - cota_x_min) < 100 else f"{int(vx_val)}"
        lienzo.dibujar_texto(txt_x, px - 12, y_origen + 8, color=(100, 110, 130), escala=1)

    lienzo.dibujar_linea(x_origen, y_origen, x_origen + ancho_util, y_origen, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(x_origen, y_origen, x_origen, m_sup - 10, color=(50, 60, 80), grosor=2)

    if eje_x:
        lienzo.dibujar_texto(eje_x, x_origen + (ancho_util // 2) - (len(eje_x) * 3), alto_lienzo - 20, color=(50, 60, 80), escala=1)
    if eje_y:
        lienzo.dibujar_texto(eje_y, m_izq, m_sup - 25, color=(50, 60, 80), escala=1)

    for px_val, py_val in puntos:
        cx = int(x_origen + ((px_val - cota_x_min) / (cota_x_max - cota_x_min)) * ancho_util)
        cy = int(y_origen - ((py_val - cota_y_min) / (cota_y_max - cota_y_min)) * alto_util)
        lienzo.dibujar_circulo(cx, cy, radio=6, color_relleno=(229, 57, 53), color_borde=(50, 20, 20))

    lienzo.exportar_png(ruta_salida)
    return ruta_salida


def graficar_histograma(tabla, col_x: str, bins: int = 6, titulo: str = "Histograma de Frecuencias",
                        eje_x: str = "", eje_y: str = "Frecuencia", ruta_salida: str = "salidas/grafico_histograma.png"):
    """Genera y exporta un histograma agrupado por intervalos de clase a PNG."""
    vx, _ = _extraer_datos(tabla, col_x)
    valores = []
    for x_val in vx:
        if x_val is not None:
            try:
                valores.append(float(x_val))
            except (ValueError, TypeError):
                continue

    if not valores:
        raise ValueError(f"No hay valores numéricos en '{col_x}' para generar un histograma.")

    ancho_lienzo, alto_lienzo = 720, 460
    lienzo = LienzoMomo(ancho_lienzo, alto_lienzo)

    m_izq, m_der, m_sup, m_inf = 75, 40, 60, 70
    x_origen = m_izq
    y_origen = alto_lienzo - m_inf
    ancho_util = ancho_lienzo - m_izq - m_der
    alto_util = y_origen - m_sup

    min_val, max_val = min(valores), max(valores)
    if min_val == max_val:
        max_val += 1.0

    ancho_bin = (max_val - min_val) / bins
    conteos = [0] * bins

    for val in valores:
        idx = int((val - min_val) / ancho_bin)
        if idx >= bins:
            idx = bins - 1
        conteos[idx] += 1

    max_freq = max(conteos) if conteos else 1
    cota_sup_freq = max_freq + 1

    lienzo.dibujar_texto(titulo, m_izq + 10, 20, color=(20, 25, 40), escala=2)

    # Rejilla Y
    for f in range(cota_sup_freq + 1):
        py = int(y_origen - (f / cota_sup_freq) * alto_util)
        lienzo.dibujar_linea(x_origen, py, x_origen + ancho_util, py, color=(225, 230, 238), grosor=1)
        lienzo.dibujar_texto(str(f), 35, py - 4, color=(100, 110, 130), escala=1)

    lienzo.dibujar_linea(x_origen, y_origen, x_origen + ancho_util, y_origen, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(x_origen, y_origen, x_origen, m_sup - 10, color=(50, 60, 80), grosor=2)

    if eje_x:
        lienzo.dibujar_texto(eje_x, x_origen + (ancho_util // 2) - (len(eje_x) * 3), alto_lienzo - 25, color=(50, 60, 80), escala=1)
    if eje_y:
        lienzo.dibujar_texto(eje_y, m_izq, m_sup - 25, color=(50, 60, 80), escala=1)

    slot_ancho = ancho_util / bins
    for b_idx in range(bins):
        bx = int(x_origen + b_idx * slot_ancho)
        frec = conteos[b_idx]
        h_bin = int((frec / cota_sup_freq) * alto_util)
        by = y_origen - h_bin
        color_b = PALETA_MOMERA[b_idx % len(PALETA_MOMERA)]

        lienzo.dibujar_rectangulo(bx, by, int(slot_ancho), h_bin, color_relleno=color_b, color_borde=(30, 40, 60))
        if frec > 0:
            lienzo.dibujar_texto(str(frec), bx + int(slot_ancho // 2) - 3, by - 12, color=(30, 40, 60), escala=1)

        lim_inf = min_val + b_idx * ancho_bin
        txt_lim = f"{lim_inf:.1f}" if max_val < 50 else f"{int(lim_inf)}"
        lienzo.dibujar_texto(txt_lim, bx - 6, y_origen + 8, color=(70, 80, 100), escala=1)

    lienzo.exportar_png(ruta_salida)
    return ruta_salida


def graficar_cajas(tabla, col_x: str, col_y: str = None, titulo: str = "Diagrama de Cajas",
                   eje_x: str = "", eje_y: str = "", ruta_salida: str = "salidas/grafico_cajas.png"):
    """Genera y exporta un diagrama de cajas (Boxplot) para análisis de distribución y cuartiles."""
    vx, _ = _extraer_datos(tabla, col_x)
    valores = []
    for x_val in vx:
        if x_val is not None:
            try:
                valores.append(float(x_val))
            except (ValueError, TypeError):
                continue

    if len(valores) < 4:
        raise ValueError(f"Se requieren al menos 4 observaciones en '{col_x}' para un diagrama de cajas.")

    valores.sort()
    n = len(valores)

    def _percentil(p):
        k = (n - 1) * p
        f = math.floor(k)
        c = math.ceil(k)
        if f == c:
            return valores[int(k)]
        return valores[int(f)] * (c - k) + valores[int(c)] * (k - f)

    min_val = valores[0]
    q1 = _percentil(0.25)
    mediana = _percentil(0.50)
    q3 = _percentil(0.75)
    max_val = valores[-1]

    ancho_lienzo, alto_lienzo = 720, 460
    lienzo = LienzoMomo(ancho_lienzo, alto_lienzo)

    m_izq, m_der, m_sup, m_inf = 75, 40, 60, 60
    x_origen = m_izq
    y_origen = alto_lienzo - m_inf
    ancho_util = ancho_lienzo - m_izq - m_der
    alto_util = y_origen - m_sup

    rango = (max_val - min_val) if (max_val - min_val) > 0 else 1.0
    cota_inf = min_val - rango * 0.1
    cota_sup = max_val + rango * 0.1

    def _mapear_y(val):
        return int(y_origen - ((val - cota_inf) / (cota_sup - cota_inf)) * alto_util)

    lienzo.dibujar_texto(titulo, m_izq + 10, 20, color=(20, 25, 40), escala=2)

    # Rejilla Y
    num_div = 5
    for i in range(num_div + 1):
        frac = i / num_div
        v_y = cota_inf + frac * (cota_sup - cota_inf)
        py = int(y_origen - frac * alto_util)
        lienzo.dibujar_linea(x_origen, py, x_origen + ancho_util, py, color=(225, 230, 238), grosor=1)
        txt_y = f"{v_y:.1f}" if (cota_sup - cota_inf) < 100 else f"{int(v_y)}"
        lienzo.dibujar_texto(txt_y, 10, py - 4, color=(100, 110, 130), escala=1)

    lienzo.dibujar_linea(x_origen, y_origen, x_origen + ancho_util, y_origen, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(x_origen, y_origen, x_origen, m_sup - 10, color=(50, 60, 80), grosor=2)

    # Posición central de la caja
    cx = x_origen + (ancho_util // 2)
    ancho_caja = 120

    py_min = _mapear_y(min_val)
    py_q1 = _mapear_y(q1)
    py_med = _mapear_y(mediana)
    py_q3 = _mapear_y(q3)
    py_max = _mapear_y(max_val)

    # Bigotes
    lienzo.dibujar_linea(cx, py_min, cx, py_q1, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(cx, py_q3, cx, py_max, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(cx - 30, py_min, cx + 30, py_min, color=(50, 60, 80), grosor=2)
    lienzo.dibujar_linea(cx - 30, py_max, cx + 30, py_max, color=(50, 60, 80), grosor=2)

    # Caja intercuartílica (Q1 a Q3)
    lienzo.dibujar_rectangulo(cx - (ancho_caja // 2), py_q3, ancho_caja, py_q1 - py_q3,
                             color_relleno=(67, 160, 71), color_borde=(30, 60, 40))

    # Línea de mediana
    lienzo.dibujar_linea(cx - (ancho_caja // 2), py_med, cx + (ancho_caja // 2), py_med,
                        color=(251, 140, 0), grosor=3)

    # Textos indicadores
    lienzo.dibujar_texto(f"MAX: {max_val:.1f}", cx + 40, py_max - 4, color=(40, 50, 70), escala=1)
    lienzo.dibujar_texto(f"Q3:  {q3:.1f}", cx + (ancho_caja // 2) + 10, py_q3 - 4, color=(40, 50, 70), escala=1)
    lienzo.dibujar_texto(f"MED: {mediana:.1f}", cx + (ancho_caja // 2) + 10, py_med - 4, color=(251, 140, 0), escala=1)
    lienzo.dibujar_texto(f"Q1:  {q1:.1f}", cx + (ancho_caja // 2) + 10, py_q1 - 4, color=(40, 50, 70), escala=1)
    lienzo.dibujar_texto(f"MIN: {min_val:.1f}", cx + 40, py_min - 4, color=(40, 50, 70), escala=1)

    if eje_x:
        lienzo.dibujar_texto(eje_x, cx - (len(eje_x) * 3), y_origen + 20, color=(50, 60, 80), escala=1)

    lienzo.exportar_png(ruta_salida)
    return ruta_salida
