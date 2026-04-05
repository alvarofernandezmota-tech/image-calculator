import cv2
import pytesseract
import re
import os
from PIL import Image
import numpy as np

# Formatos de imagen aceptados por cargar()
FORMATOS_SOPORTADOS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff")

# Tamaño mínimo de ancho para que Tesseract trabaje bien
MIN_ANCHO_OCR = 600

# Rutas candidatas de Tesseract en Windows (se prueba en orden)
_RUTAS_TESSERACT_WINDOWS = [
    r"C:\Program Files\Tesseract-OCR\tesseract.exe",
    r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe",
    os.path.expanduser(r"~\AppData\Local\Tesseract-OCR\tesseract.exe"),
]

def _configurar_tesseract():
    """
    Detecta la ruta de Tesseract en Windows y la configura en pytesseract.
    Si no se encuentra en ninguna ruta conocida, asume que está en el PATH.
    """
    for ruta in _RUTAS_TESSERACT_WINDOWS:
        if os.path.isfile(ruta):
            pytesseract.pytesseract.tesseract_cmd = ruta
            return
    # Si no se encuentra, pytesseract usará el PATH del sistema

_configurar_tesseract()


class LectorImagen:
    """
    Lee un número desde una imagen usando OCR (Tesseract).

    Pipeline:
        cargar() → preprocesar() → extraer_numero()

    Soporta números enteros y decimales en formato:
        - Anglo:   1,234.56  →  1234.56
        - Europeo: 1.234,56  →  1234.56
        - Simple:  42 / 3.14 / 3,14
    """

    def cargar(self, ruta: str):
        """
        Carga la imagen desde disco y la convierte a array NumPy (RGB).

        Args:
            ruta: Ruta al archivo de imagen.

        Returns:
            numpy.ndarray: Array RGB de la imagen.

        Raises:
            ValueError: Si el formato no está en FORMATOS_SOPORTADOS.
        """
        ext = ruta.lower().split(".")[-1]
        if f".{ext}" not in FORMATOS_SOPORTADOS:
            raise ValueError(
                f"Formato no soportado: .{ext}. "
                f"Formatos válidos: {', '.join(FORMATOS_SOPORTADOS)}"
            )
        img = Image.open(ruta).convert("RGB")
        return np.array(img)

    def preprocesar(self, imagen_array):
        """
        Preprocesa la imagen para mejorar la precisión del OCR.

        Pasos:
            1. Convierte a escala de grises.
            2. Escala agresivamente a mínimo 600px de ancho.
            3. Aplica denoising para eliminar ruido de fondo.
            4. Detecta y corrige inversión (texto claro sobre fondo oscuro).
            5. Aplica umbral de Otsu para binarización óptima global.
            6. Morfología: cierre para unir trazos fragmentados.

        Args:
            imagen_array: numpy.ndarray RGB devuelto por cargar().

        Returns:
            numpy.ndarray: Imagen binarizada lista para Tesseract.
        """
        gris = cv2.cvtColor(imagen_array, cv2.COLOR_RGB2GRAY)
        h, w = gris.shape

        # Escalado agresivo: mínimo 600px de ancho para mayor precisión OCR
        if w < MIN_ANCHO_OCR:
            escala = MIN_ANCHO_OCR / w
            gris = cv2.resize(
                gris, None, fx=escala, fy=escala,
                interpolation=cv2.INTER_CUBIC
            )

        # Denoising: elimina ruido manteniendo bordes de los caracteres
        gris = cv2.fastNlMeansDenoising(gris, h=10, templateWindowSize=7, searchWindowSize=21)

        # Inversión automática: si el fondo es oscuro, invertir para Tesseract
        media_pixel = np.mean(gris)
        if media_pixel < 127:
            gris = cv2.bitwise_not(gris)

        # Umbral de Otsu: calcula automáticamente el umbral óptimo global
        _, procesada = cv2.threshold(
            gris, 0, 255,
            cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )

        # Morfología: pequeña dilatación para unir trazos fragmentados
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2, 2))
        procesada = cv2.morphologyEx(procesada, cv2.MORPH_CLOSE, kernel)

        return procesada

    def _normalizar_numero(self, texto: str) -> float:
        """
        Convierte texto OCR con separadores de miles o decimales a float.

        Maneja los dos formatos más comunes:
            - Formato anglosajón: 1,234.56  →  1234.56
            - Formato europeo:    1.234,56  →  1234.56
            - Sin separador:      42 / 3.14 / 3,14

        Args:
            texto: Cadena extraída por OCR que contiene un número.

        Returns:
            float: El número normalizado.

        Raises:
            ValueError: Si no se puede convertir a float.
        """
        t = texto.strip()

        if re.match(r'^\d{1,3}(\.\d{3})+(,\d+)?$', t):
            t = t.replace('.', '').replace(',', '.')
        elif re.match(r'^\d{1,3}(,\d{3})+(\.\d+)?$', t):
            t = t.replace(',', '')
        elif re.match(r'^\d+,\d+$', t):
            t = t.replace(',', '.')

        return float(t)

    def extraer_numero(self, ruta: str) -> float:
        """
        Pipeline completo: carga → preprocesa → OCR → normaliza → devuelve float.

        Prueba múltiples configuraciones de Tesseract (PSM 7, 8, 6) y devuelve
        el primer candidato válido encontrado.

        Args:
            ruta: Ruta al archivo de imagen.

        Returns:
            float: El primer número encontrado en la imagen.

        Raises:
            ValueError: Si no se encuentra ningún número en la imagen.
        """
        imagen = self.cargar(ruta)
        procesada = self.preprocesar(imagen)

        whitelist = "-c tessedit_char_whitelist=0123456789.,-"
        configs = [
            f"--psm 7 {whitelist}",
            f"--psm 8 {whitelist}",
            f"--psm 6 {whitelist}",
        ]

        patron = re.compile(
            r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?|\d+[.,]\d+|\d+'
        )

        for config in configs:
            texto = pytesseract.image_to_string(procesada, config=config)
            candidatos = patron.findall(texto)
            if candidatos:
                return self._normalizar_numero(candidatos[0])

        raise ValueError(
            "No se encontró ningún número en la imagen. "
            "Asegúrate de que la imagen contiene un número visible y enfocado."
        )
