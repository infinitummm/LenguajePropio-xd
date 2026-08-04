"""
Script de Demostración Completo de las 3 Librerías Propias en Español xd
"""

import os
from src.core.matematica_propia import Arreglo, crear_arreglo_xd, rango_xd
from src.core.datos_propios import cargar_csv_xd, guardar_csv_xd
from src.core.graficos_propios import crear_figura_xd

def ejecutar_demostracion_xd():
    print("=" * 60)
    print("INICIANDO DEMOSTRACION DE LIBRERIAS PROPIAS EN ESPANOL xd")
    print("=" * 60)

    os.makedirs("salidas", exist_ok=True)

    # -------------------------------------------------------------
    # 1. Demostración de matemática_propia (Reemplazo de NumPy)
    # -------------------------------------------------------------
    print("\n[1/3] Probando 'matematica_propia' (Reemplazo propio de NumPy)...")
    v1 = crear_arreglo_xd([10, 25, 30, 45, 60])
    v2 = crear_arreglo_xd([2, 5, 3, 5, 10])

    print(f"  - Vector 1: {v1}")
    print(f"  - Vector 2: {v2}")
    print(f"  - Suma elemento a elemento (v1 + v2): {v1 + v2}")
    print(f"  - Multiplicacion (v1 * v2): {v1 * v2}")
    print(f"  - Promedio de Vector 1 (promedio_xd): {v1.promedio_xd():.2f}")
    print(f"  - Mediana de Vector 1 (mediana_xd): {v1.mediana_xd():.2f}")
    print(f"  - Desviacion Estandar (desviacion_estandar_xd): {v1.desviacion_estandar_xd():.2f}")
    print(f"  - Mascara Booleana (Vector 1 > 30): {v1.mayor_que_xd(30)}")

    # -------------------------------------------------------------
    # 2. Demostración de datos_propios (Reemplazo de Pandas)
    # -------------------------------------------------------------
    print("\n[2/3] Probando 'datos_propios' (Reemplazo propio de Pandas)...")
    ruta_csv = "datos/ventas_prueba.csv"
    tabla = cargar_csv_xd(ruta_csv)
    print(f"  - CSV Cargado exitosamente: {tabla.numero_filas} filas x {len(tabla.columnas)} columnas")
    print(f"  - Columnas presentes: {tabla.nombres_columnas}")

    unidades = tabla["unidades"].arreglo
    precio = tabla["precio"].arreglo
    tabla["total"] = unidades * precio
    print("  - Columna calculada 'total' anadida exitosamente.")

    mascara_electronica = tabla["categoria"].arreglo.igual_a_xd("Electronica")
    tabla_electronica = tabla.filtrar_xd(mascara_electronica)
    print(f"  - Ventas filtradas de 'Electronica': {tabla_electronica.numero_filas} registros.")

    resumen_ciudad = tabla.agrupar_por_xd("ciudad").resumir_xd(
        ingreso_total=("total", "suma"),
        promedio_unidades=("unidades", "promedio"),
        registros=("unidades", "conteo")
    )
    print("\n  - Resumen por Ciudad (Agrupamiento):")
    for fila in resumen_ciudad.obtener_filas_xd():
        print(f"    * Ciudad: {fila['ciudad']} | Ventas Totales: ${fila['ingreso_total']:.2f} | Promedio Unidades: {fila['promedio_unidades']:.1f}")

    ruta_salida_csv = "salidas/resumen_ciudades.csv"
    guardar_csv_xd(resumen_ciudad, ruta_salida_csv)
    print(f"  - Tabla de resumen guardada en: '{ruta_salida_csv}'")

    # -------------------------------------------------------------
    # 3. Demostración de graficos_propios (Reemplazo de Matplotlib)
    # -------------------------------------------------------------
    print("\n[3/3] Probando 'graficos_propios' (Reemplazo propio de Matplotlib)...")

    fig_barras = crear_figura_xd(titulo="Ingresos Totales por Ciudad xd", etiqueta_x="Ciudad", etiqueta_y="Ventas ($)")
    ciudades = resumen_ciudad["ciudad"].datos
    ingresos = resumen_ciudad["ingreso_total"].datos
    fig_barras.graficar_barras_xd(ciudades, ingresos, color="#3b82f6")
    fig_barras.guardar_svg_xd("salidas/grafico_barras_ingresos.svg")
    print("  - [SVG Gen] Grafico de Barras guardado en 'salidas/grafico_barras_ingresos.svg'")

    fig_lineas = crear_figura_xd(titulo="Tendencia de Precios por Registro xd", etiqueta_x="Indice", etiqueta_y="Precio")
    indices = list(range(1, tabla.numero_filas + 1))
    precios = tabla["precio"].datos
    fig_lineas.graficar_lineas_xd(indices, precios, color="#10b981")
    fig_lineas.guardar_svg_xd("salidas/grafico_lineas_precios.svg")
    print("  - [SVG Gen] Grafico de Lineas guardado en 'salidas/grafico_lineas_precios.svg'")

    fig_hist = crear_figura_xd(titulo="Distribucion de Unidades Vendidas xd", etiqueta_x="Rango de Unidades", etiqueta_y="Frecuencia")
    fig_hist.graficar_histograma_xd(unidades.datos, bins=4, color="#8b5cf6")
    fig_hist.guardar_svg_xd("salidas/grafico_histograma_unidades.svg")
    print("  - [SVG Gen] Histograma guardado en 'salidas/grafico_histograma_unidades.svg'")

    fig_disp = crear_figura_xd(titulo="Dispersion: Unidades vs Precio xd", etiqueta_x="Unidades", etiqueta_y="Precio ($)")
    fig_disp.graficar_dispersion_xd(unidades.datos, precios, color="#ef4444")
    fig_disp.guardar_svg_xd("salidas/grafico_dispersion_unidades_precio.svg")
    print("  - [SVG Gen] Grafico de Dispersion guardado en 'salidas/grafico_dispersion_unidades_precio.svg'")

    print("\n" + "=" * 60)
    print("DEMOSTRACION COMPLETADA EXITOSAMENTE xd")
    print("=" * 60)

if __name__ == "__main__":
    ejecutar_demostracion_xd()
