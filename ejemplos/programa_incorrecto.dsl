# Ejemplo Incorrecto (Sintaxis inválida para prueba de diagnóstico sintáctico xd)
ventas = cargar_csv_xd "datos/ventas_prueba.csv"

# Error sintáctico: Falta la asignación o el operador pipe |>
ventas_limpias seleccionar_xd [fecha, ciudad]

# Error sintáctico: Expresión mal formada sin operador relacional
ventas_filtradas = ventas_limpias |> filtrar_xd unidades + 
