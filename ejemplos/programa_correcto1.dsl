# Ejemplo 1: Flujo completo de ventas en DSL (Corte 1 xd)
ventas = cargar_csv_xd "datos/ventas_prueba.csv"

ventas_limpias = ventas 
  |> seleccionar_xd [fecha, ciudad, categoria, unidades, precio]
  |> filtrar_xd unidades > 10
  |> crear_columna_xd total = unidades * precio

resumen_ciudad = ventas_limpias 
  |> agrupar_por_xd [ciudad] 
  |> resumir_xd total_ventas = suma(total), promedio_u = promedio(unidades)

guardar_csv_xd resumen_ciudad "salidas/resumen_ciudades_dsl.csv"
graficar_barras_xd resumen_ciudad titulo "Ventas por Ciudad xd" eje_x "Ciudad" eje_y "Total Ventas ($)" guardar "salidas/grafico_dsl_barras.svg"
