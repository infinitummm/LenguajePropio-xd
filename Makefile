# =============================================================================
# Makefile para MomoLang XD (.xd) - DSL de Ciencia de Datos y Visualización
# Asignatura: Lenguajes de Programación y Transducción (2026-2)
# =============================================================================

PYTHON ?= python3
ifeq ($(OS),Windows_NT)
    PYTHON = python
endif
ANTLR4 ?= antlr4
GRAMMAR_DIR = grammar
PARSER_DIR = src/parser
EJEMPLOS_DIR = ejemplos

.PHONY: help build antlr run run-tree run-incorrect run-ventas run-empleados run-estudiantes run-error-semantico clean

help:
	@echo "========================================================================="
	@echo "                   COMANDOS DISPONIBLES EN MOMOLANG XD :v               "
	@echo "========================================================================="
	@echo "  make build               - Compila la gramatica ANTLR4 a Python"
	@echo "  make run                 - Ejecuta programa_correcto1.xd"
	@echo "  make run-ventas          - Ejecuta el analisis de ventas (Fase 2)"
	@echo "  make run-empleados       - Ejecuta el analisis de nomina (Fase 2)"
	@echo "  make run-estudiantes     - Ejecuta el analisis de notas academicas (Fase 2)"
	@echo "  make run-error-semantico - Prueba la deteccion de errores semanticos"
	@echo "  make run-incorrect       - Prueba el diagnostico de errores sintacticos"
	@echo "  make run-tree            - Muestra el arbol sintactico jerarquico (--arbol)"
	@echo "  make clean               - Limpia archivos temporales y cache de Python"
	@echo "========================================================================="

build: antlr

antlr:
	@echo ">> Compilando gramatica ANTLR4: $(GRAMMAR_DIR)/LenguajeMomoXD.g4 ..."
	$(ANTLR4) -Dlanguage=Python3 -visitor -o $(PARSER_DIR) $(GRAMMAR_DIR)/LenguajeMomoXD.g4
	@if [ -d "$(PARSER_DIR)/grammar" ]; then mv $(PARSER_DIR)/grammar/* $(PARSER_DIR)/ && rmdir $(PARSER_DIR)/grammar; fi
	@echo "[OK] Lexer y Parser generados exitosamente en $(PARSER_DIR)."

run:
	@echo ">> Ejecutando programa_correcto1.xd ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_correcto1.xd

run-ventas:
	@echo ">> Ejecutando analisis de ventas (Fase 2) ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_ventas_fase2.xd

run-empleados:
	@echo ">> Ejecutando analisis de empleados (Fase 2) ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_empleados_fase2.xd

run-estudiantes:
	@echo ">> Ejecutando analisis de estudiantes (Fase 2) ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_estudiantes_fase2.xd

run-error-semantico:
	@echo ">> Probando deteccion de error semantico ..."
	-$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_error_semantico.xd

run-tree:
	@echo ">> Validando programa de ejemplo 1 con arbol jerarquico ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_correcto1.xd --arbol

run-incorrect:
	@echo ">> Validando programa con errores sintacticos ..."
	-$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_incorrecto1.xd

clean:
	@echo ">> Limpiando archivos temporales y cache ..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "[OK] Limpieza completada."
