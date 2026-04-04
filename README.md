# 🖼️ Image Calculator

> Lee números en imágenes y los opera entre sí. Python + OCR + GUI.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![OCR](https://img.shields.io/badge/OCR-Tesseract-orange)](https://github.com/tesseract-ocr/tesseract)
[![Version](https://img.shields.io/badge/version-0.2.0-informational)](CHANGELOG.md)

---

## ¿Qué hace?

Carga dos imágenes que contienen números, los lee automáticamente con OCR y aplica la operación que elijas: suma, resta, multiplicación, división, comparación, concatenación, máximo, mínimo o promedio.

```
Imagen A: [foto con el número 42]
Imagen B: [foto con el número 18]
→ Operación: Suma
→ Resultado: 42 + 18 = 60
```

---

## 🚀 Instalación

### 1. Instala Tesseract (motor OCR)

| Sistema | Instrucción |
|---------|-------------|
| Windows | [Descargar instalador](https://github.com/UB-Mannheim/tesseract/wiki) |
| macOS   | `brew install tesseract` |
| Linux   | `sudo apt install tesseract-ocr` |

### 2. Clona el repositorio

```bash
git clone https://github.com/alvarofernandezmota-tech/image-calculator.git
cd image-calculator
```

### 3. Instala dependencias Python

```bash
pip install -r requirements.txt
```

### 4. Ejecuta

```bash
python main.py
```

---

## 🧩 Estructura del proyecto

```
image-calculator/
├── main.py              ← Punto de entrada (lanza GUI)
├── requirements.txt     ← Dependencias Python
├── LICENSE
├── CHANGELOG.md         ← Historial de cambios
├── ROADMAP.md           ← Trayectoria del proyecto
├── nucleo/
│   ├── lector.py        ← Carga imagen + preprocesado + OCR
│   └── operaciones.py   ← Lógica de operaciones
└── gui/
    └── app.py           ← Interfaz gráfica tkinter
```

---

## 📋 Operaciones disponibles

| Operación | Descripción |
|-----------|-------------|
| Suma | `A + B` |
| Resta | `A - B` |
| Multiplicación | `A × B` |
| División | `A ÷ B` |
| Comparar | Cuál es mayor, menor o si son iguales |
| Concatenar | Une los dígitos: `12` y `34` → `1234` |
| Máximo | El mayor de los dos |
| Mínimo | El menor de los dos |
| Promedio | `(A + B) / 2` |

## 🖼️ Formatos soportados

PNG · JPG / JPEG · WEBP · BMP · TIFF

---

## ⚠️ Nota Windows

Si Tesseract no se encuentra automáticamente, añade al principio de `nucleo/lector.py`:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

## 🗺️ Roadmap

Ver el [ROADMAP completo](ROADMAP.md).

| Versión | Estado | Qué incluye |
|---------|--------|-------------|
| v0.1 | ✅ | Núcleo OCR + terminal |
| v0.2 | ✅ | GUI de escritorio |
| v0.3 | 🔜 | Tests + imágenes demo |
| v0.4 | 🔜 | Binario `.exe` / `.app` |
| v0.5 | 🔮 | Bot de Telegram |
| v1.0 | 🔮 | Versión estable completa |

---

## 🤝 Contribuir

1. Haz fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz commit: `git commit -m 'Add: nueva funcionalidad'`
4. Haz push: `git push origin feature/nueva-funcionalidad`
5. Abre un Pull Request

---

## 📄 Licencia

MIT — puedes usar, modificar y distribuir libremente.
