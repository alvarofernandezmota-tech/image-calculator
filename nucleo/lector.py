import cv2
import pytesseract
import re
from PIL import Image
import numpy as np

FORMATOS_SOPORTADOS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff")

class LectorImagen:
    """Carga, preprocesa y extrae números de imágenes."""

    def cargar(self, ruta: str):
        """Carga la imagen desde disco. Acepta PNG, JPG, JPEG, WEBP."""
        ext = ruta.lower().split(".")[-1]
        if f".{ext}" not in FORMATOS_SOPORTADOS:
            raise ValueError(f"Formato no soportado: .{ext}. Usa: {FORMATOS_SOPORTADOS}")
        img = Image.open(ruta).convert("RGB")
        return np.array(img)

    def preprocesar(self, imagen_array):
        """Convierte a escala de grises y aplica umbral para mejorar OCR."""
        gris = cv2.cvtColor(imagen_array, cv2.COLOR_RGB2GRAY)
        h, w = gris.shape
        if w < 300:
            escala = 300 / w
            gris = cv2.resize(gris, None, fx=escala, fy=escala, interpolation=cv2.INTER_CUBIC)
        procesada = cv2.adaptiveThreshold(
            gris, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
        return procesada

    def extraer_numero(self, ruta: str):
        """Pipeline completo: carga → preprocesa → OCR → devuelve número."""
        imagen = self.cargar(ruta)
        procesada = self.preprocesar(imagen)
        config = "--psm 6 -c tessedit_char_whitelist=0123456789.,-"
        texto = pytesseract.image_to_string(procesada, config=config)
        numeros = re.findall(r"[\d]+(?:[.,][\d]+)?", texto.replace(",", "."))
        if not numeros:
            raise ValueError("No se encontró ningún número en la imagen.")
        return float(numeros[0])
