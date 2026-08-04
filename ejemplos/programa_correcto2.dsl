# Ejemplo 2: Análisis exploratorio y dispersión (Corte 1 xd)
datos_raw = cargar_csv_xd "datos/ventas_prueba.csv"

datos_ordenados = datos_raw 
  |> seleccionar_xd [unidades, precio]
  |> ordenar_por_xd precio descendente

graficar_dispersion_xd datos_ordenados titulo "Dispersion Unidades vs Precio xd" eje_x "Unidades" eje_y "Precio ($)" guardar "salidas/grafico_dsl_dispersion.svg"
