# Changelog

Todos los cambios notables de este proyecto están documentados aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [0.2.0] — 2026-04-04

### Añadido
- Interfaz gráfica de escritorio con `tkinter` (`gui/app.py`)
- Preprocesado adaptativo de imagen (escala de grises + umbral adaptativo)
- Soporte para 9 operaciones: suma, resta, multiplicación, división, comparar, concatenar, máximo, mínimo, promedio
- Compatibilidad con PNG, JPG, WEBP, BMP, TIFF
- Nota de configuración para Windows (ruta Tesseract)
- `requirements.txt` con dependencias exactas

### Cambiado
- Arquitectura separada en capas: `nucleo/` (lógica) y `gui/` (interfaz)
- `main.py` como único punto de entrada

---

## [0.1.0] — 2026-04-01

### Añadido
- Núcleo OCR básico con `pytesseract` (`nucleo/lector.py`)
- Función `extraer_numero()` — lee el primer número de una imagen
- Función `operar()` — aplica una operación a dos números
- Versión de terminal (`terminal.py`) para pruebas rápidas
- Licencia MIT
