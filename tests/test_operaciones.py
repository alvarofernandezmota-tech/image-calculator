"""
Tests para nucleo/operaciones.py
No necesitan imágenes ni Tesseract — prueban la lógica pura.
"""
import pytest
from nucleo.operaciones import Operaciones


@pytest.fixture
def ops():
    return Operaciones()


class TestOperacionesBasicas:

    def test_suma(self, ops):
        assert ops.aplicar("Suma", 3.0, 2.0) == "3.0 + 2.0 = 5.0"

    def test_resta(self, ops):
        assert ops.aplicar("Resta", 10.0, 4.0) == "10.0 - 4.0 = 6.0"

    def test_multiplicacion(self, ops):
        assert ops.aplicar("Multiplicación", 3.0, 4.0) == "3.0 × 4.0 = 12.0"

    def test_division_normal(self, ops):
        resultado = ops.aplicar("División", 10.0, 4.0)
        assert "2.5" in resultado

    def test_division_entre_cero(self, ops):
        """División entre 0 devuelve mensaje de error, no lanza excepción."""
        resultado = ops.aplicar("División", 5.0, 0.0)
        assert resultado == "Error: no se puede dividir entre 0"

    def test_comparar_mayor(self, ops):
        resultado = ops.aplicar("Comparar", 10.0, 3.0)
        assert "A es mayor" in resultado

    def test_comparar_menor(self, ops):
        resultado = ops.aplicar("Comparar", 2.0, 8.0)
        assert "B es mayor" in resultado

    def test_comparar_iguales(self, ops):
        resultado = ops.aplicar("Comparar", 5.0, 5.0)
        assert "Son iguales" in resultado

    def test_concatenar(self, ops):
        resultado = ops.aplicar("Concatenar", 12.0, 34.0)
        assert "1234" in resultado

    def test_maximo(self, ops):
        resultado = ops.aplicar("Máximo", 7.0, 3.0)
        assert "7.0" in resultado

    def test_minimo(self, ops):
        resultado = ops.aplicar("Mínimo", 7.0, 3.0)
        assert "3.0" in resultado

    def test_promedio(self, ops):
        resultado = ops.aplicar("Promedio", 4.0, 6.0)
        assert "5.0" in resultado


class TestOperacionesEdge:

    def test_operacion_desconocida_lanza_value_error(self, ops):
        with pytest.raises(ValueError, match="Operación desconocida"):
            ops.aplicar("Inventada", 1.0, 2.0)

    def test_todas_las_operaciones_devuelven_string(self, ops):
        """Garantiza que ninguna operación devuelve None ni un tipo raro."""
        for op in Operaciones.LISTA:
            resultado = ops.aplicar(op, 6.0, 2.0)
            assert isinstance(resultado, str), f"{op} no devolvió str"

    def test_numeros_negativos(self, ops):
        resultado = ops.aplicar("Suma", -5.0, 3.0)
        assert "-2.0" in resultado

    def test_numeros_decimales_precision(self, ops):
        resultado = ops.aplicar("División", 1.0, 3.0)
        assert "0.3333" in resultado
