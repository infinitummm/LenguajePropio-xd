# =============================================================================
# Makefile para MomoLang XD (.xd) - DSL de Ciencia de Datos y Visualización
# Asignatura: Lenguajes de Programación y Transducción (2026-2)
# =============================================================================

PYTHON = python3
ANTLR4 = antlr4
GRAMMAR_DIR = grammar
PARSER_DIR = src/parser
TESTS_DIR = tests
EJEMPLOS_DIR = ejemplos

.PHONY: help build antlr test test-libs test-all run run-tree run-incorrect demo clean

help:
	@echo "========================================================================="
	@echo "                   COMANDOS DISPONIBLES EN MOMOLANG XD :v               "
	@echo "========================================================================="
	@echo "  make build         - Compila la gramatica ANTLR4 a Python"
	@echo "  make test          - Ejecuta las pruebas del Corte 1 (Acepta/Rechaza)"
	@echo "  make test-libs     - Ejecuta las pruebas de las librerias propias"
	@echo "  make test-all      - Ejecuta todas las pruebas unitarias y de integracion"
	@echo "  make run           - Ejecuta el validador con programa_correcto1.xd"
	@echo "  make run-tree      - Muestra el arbol sintactico jerarquico (--arbol)"
	@echo "  make run-incorrect - Prueba el diagnostico de errores con programa_incorrecto1.xd"
	@echo "  make demo          - Ejecuta la demostracion del motor propio de datos"
	@echo "  make clean         - Limpia archivos temporales y cache de Python"
	@echo "========================================================================="

build: antlr

antlr:
	@echo ">> Compilando gramatica ANTLR4: $(GRAMMAR_DIR)/LenguajeMomoXD.g4 ..."
	$(ANTLR4) -Dlanguage=Python3 -visitor -o $(PARSER_DIR) $(GRAMMAR_DIR)/LenguajeMomoXD.g4
	@if [ -d "$(PARSER_DIR)/grammar" ]; then mv $(PARSER_DIR)/grammar/* $(PARSER_DIR)/ && rmdir $(PARSER_DIR)/grammar; fi
	@echo "[OK] Lexer y Parser generados exitosamente en $(PARSER_DIR)."

test:
	@echo ">> Ejecutando pruebas del Corte 1 (Aceptacion y Rechazo) ..."
	$(PYTHON) -m unittest $(TESTS_DIR)/test_corte1.py -v

test-libs:
	@echo ">> Ejecutando pruebas unitarias de las librerias propias ..."
	$(PYTHON) -m unittest $(TESTS_DIR)/probar_librerias.py -v

test-all: test test-libs
	@echo "[OK] Todas las pruebas han sido ejecutadas exitosamente."

run:
	@echo ">> Validando programa de ejemplo 1 ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_correcto1.xd

run-tree:
	@echo ">> Validando programa de ejemplo 1 con arbol jerarquico ..."
	$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_correcto1.xd --arbol

run-incorrect:
	@echo ">> Validando programa con errores sintacticos ..."
	-$(PYTHON) ejecutar_dsl.py $(EJEMPLOS_DIR)/programa_incorrecto1.xd

demo:
	@echo ">> Ejecutando demostracion de librerias propias ..."
	$(PYTHON) demostracion_librerias.py

clean:
	@echo ">> Limpiando archivos temporales y cache ..."
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type f -name "*.pyo" -delete 2>/dev/null || true
	@echo "[OK] Limpieza completada."
