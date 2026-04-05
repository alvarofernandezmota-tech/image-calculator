"""
Tests para nucleo/lector.py
Usan mocks para no depender de Tesseract ni de imágenes reales.
Para tests con imágenes reales: instala Tesseract y usa demo/
"""
import pytest
from unittest.mock import patch, MagicMock
import numpy as np
from nucleo.lector import LectorImagen, FORMATOS_SOPORTADOS


class TestFormatos:
    """Comprueba qué formatos acepta y cuáles rechaza cargar()."""

    @pytest.mark.parametrize("ruta", [
        "imagen.png",
        "imagen.jpg",
        "imagen.jpeg",
        "imagen.webp",
        "imagen.bmp",
        "imagen.tiff",
    ])
    def test_formatos_soportados_no_lanzan_error_de_formato(self, ruta):
        """Todos los formatos soportados pasan la validación de extensión."""
        lector = LectorImagen()
        imagen_mock = MagicMock()
        imagen_mock.convert.return_value = MagicMock(
            __array__=MagicMock(return_value=np.ones((100, 100, 3), dtype=np.uint8))
        )
        with patch("nucleo.lector.Image.open", return_value=imagen_mock):
            with patch("numpy.array", return_value=np.ones((100, 100, 3), dtype=np.uint8)):
                try:
                    lector.cargar(ruta)
                except ValueError as e:
                    if "Formato no soportado" in str(e):
                        pytest.fail(f"{ruta} debería estar soportado pero lanzó: {e}")

    @pytest.mark.parametrize("ruta", [
        "imagen.gif",
        "imagen.pdf",
        "imagen.svg",
        "imagen.txt",
        "imagen.mp4",
    ])
    def test_formatos_no_soportados_lanzan_value_error(self, ruta):
        """Formatos fuera de la lista lanzan ValueError con mensaje claro."""
        lector = LectorImagen()
        with pytest.raises(ValueError, match="Formato no soportado"):
            lector.cargar(ruta)


class TestExtraerNumero:
    """Tests del pipeline completo extraer_numero()."""

    def test_extrae_numero_entero(self):
        """Si OCR devuelve '42', extraer_numero retorna 42.0."""
        lector = LectorImagen()
        array_mock = np.ones((100, 100, 3), dtype=np.uint8)
        gris_mock = np.ones((100, 100), dtype=np.uint8)

        with patch.object(lector, "cargar", return_value=array_mock):
            with patch.object(lector, "preprocesar", return_value=gris_mock):
                with patch("nucleo.lector.pytesseract.image_to_string", return_value="42"):
                    resultado = lector.extraer_numero("cualquier.png")
        assert resultado == 42.0

    def test_extrae_numero_decimal(self):
        """Si OCR devuelve '3.14', extraer_numero retorna 3.14."""
        lector = LectorImagen()
        array_mock = np.ones((100, 100, 3), dtype=np.uint8)
        gris_mock = np.ones((100, 100), dtype=np.uint8)

        with patch.object(lector, "cargar", return_value=array_mock):
            with patch.object(lector, "preprocesar", return_value=gris_mock):
                with patch("nucleo.lector.pytesseract.image_to_string", return_value="3.14"):
                    resultado = lector.extraer_numero("cualquier.png")
        assert resultado == pytest.approx(3.14)

    def test_imagen_sin_numero_lanza_value_error(self):
        """Si OCR no encuentra ningún número, lanza ValueError."""
        lector = LectorImagen()
        array_mock = np.ones((100, 100, 3), dtype=np.uint8)
        gris_mock = np.ones((100, 100), dtype=np.uint8)

        with patch.object(lector, "cargar", return_value=array_mock):
            with patch.object(lector, "preprocesar", return_value=gris_mock):
                with patch("nucleo.lector.pytesseract.image_to_string", return_value="abc xyz"):
                    with pytest.raises(ValueError, match="No se encontró ningún número"):
                        lector.extraer_numero("vacia.png")

    def test_imagen_blanco_puro_lanza_value_error(self):
        """Una imagen completamente blanca (sin texto) lanza ValueError."""
        lector = LectorImagen()
        array_mock = np.ones((100, 100, 3), dtype=np.uint8)
        gris_mock = np.ones((100, 100), dtype=np.uint8)

        with patch.object(lector, "cargar", return_value=array_mock):
            with patch.object(lector, "preprocesar", return_value=gris_mock):
                with patch("nucleo.lector.pytesseract.image_to_string", return_value=""):
                    with pytest.raises(ValueError):
                        lector.extraer_numero("blanco.png")
