import cv2
import pytesseract
import re
from PIL import Image
import numpy as np

# Formatos de imagen aceptados por cargar()
FORMATOS_SOPORTADOS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff")


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
            2. Escala a mínimo 300px de ancho si es muy pequeña.
            3. Aplica umbral adaptativo gaussiano (binarización local).

        Args:
            imagen_array: numpy.ndarray RGB devuelto por cargar().

        Returns:
            numpy.ndarray: Imagen binarizada lista para Tesseract.
        """
        gris = cv2.cvtColor(imagen_array, cv2.COLOR_RGB2GRAY)
        h, w = gris.shape

        # Escalar si la imagen es demasiado pequeña (mejora OCR notablemente)
        if w < 300:
            escala = 300 / w
            gris = cv2.resize(
                gris, None, fx=escala, fy=escala,
                interpolation=cv2.INTER_CUBIC
            )

        # Umbral adaptativo: maneja variaciones de iluminación
        procesada = cv2.adaptiveThreshold(
            gris, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY, 11, 2
        )
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

        # Formato europeo: punto como miles, coma como decimal
        # Ejemplo: "1.234,56" → "1234.56"
        if re.match(r'^\d{1,3}(\.\d{3})+(,\d+)?$', t):
            t = t.replace('.', '').replace(',', '.')

        # Formato anglosajón: coma como miles, punto como decimal
        # Ejemplo: "1,234.56" → "1234.56"
        elif re.match(r'^\d{1,3}(,\d{3})+(\.\d+)?$', t):
            t = t.replace(',', '')

        # Decimal simple con coma europea: "3,14" → "3.14"
        elif re.match(r'^\d+,\d+$', t):
            t = t.replace(',', '.')

        # Decimal simple con punto o entero: "3.14" / "42" → sin cambios
        # else: t queda igual

        return float(t)

    def extraer_numero(self, ruta: str) -> float:
        """
        Pipeline completo: carga → preprocesa → OCR → normaliza → devuelve float.

        Detecta automáticamente el formato numérico (europeo o anglosajón)
        y lo convierte a float correctamente.

        Args:
            ruta: Ruta al archivo de imagen.

        Returns:
            float: El primer número encontrado en la imagen.

        Raises:
            ValueError: Si no se encuentra ningún número en la imagen.

        Ejemplos:
            >>> lector.extraer_numero("foto_42.png")       # → 42.0
            >>> lector.extraer_numero("precio_3_14.png")   # → 3.14
            >>> lector.extraer_numero("miles_1234.png")    # → 1234.56
        """
        imagen = self.cargar(ruta)
        procesada = self.preprocesar(imagen)

        # PSM 6: asume bloque de texto uniforme (ideal para números aislados)
        # Whitelist: solo dígitos y separadores decimales/miles
        config = "--psm 6 -c tessedit_char_whitelist=0123456789.,-"
        texto = pytesseract.image_to_string(procesada, config=config)

        # Busca patrones numéricos incluyendo separadores de miles y decimales
        candidatos = re.findall(
            r'\d{1,3}(?:[.,]\d{3})*(?:[.,]\d+)?|\d+[.,]\d+|\d+',
            texto
        )

        if not candidatos:
            raise ValueError(
                "No se encontró ningún número en la imagen. "
                "Asegúrate de que la imagen contiene un número visible y enfocado."
            )

        return self._normalizar_numero(candidatos[0])
