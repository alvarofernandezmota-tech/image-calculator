#!/usr/bin/env python3
"""
Calculadora de Imágenes
=======================
Punto de entrada principal. Lanza la interfaz de escritorio.

Requisitos (instalar una sola vez):
    pip install pillow opencv-python pytesseract

Además necesitas Tesseract instalado en tu sistema:
    Windows: https://github.com/UB-Mannheim/tesseract/wiki
    macOS:   brew install tesseract
    Linux:   sudo apt install tesseract-ocr

Uso:
    python main.py
"""

from gui.app import main

if __name__ == "__main__":
    main()
