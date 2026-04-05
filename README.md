# 🖼️ Image Calculator

> Lee números en imágenes y los opera entre sí. Python + OCR + GUI.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![OCR](https://img.shields.io/badge/OCR-Tesseract-orange)](https://github.com/tesseract-ocr/tesseract)
[![Version](https://img.shields.io/badge/version-0.3.0-informational)](CHANGELOG.md)
[![Tests](https://img.shields.io/badge/tests-31%20passed-brightgreen)](#-tests)

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

## 🧪 Tests

El proyecto incluye una suite de **31 tests** con `pytest`. No requieren Tesseract instalado — usan mocks para el OCR.

```bash
# Instalar pytest
pip install pytest

# Correr todos los tests
python -m pytest tests/ -v
```

### ¿Qué se testea?

| Archivo | Tests | Qué cubre |
|---|---|---|
| `test_lector.py` | 15 | 6 formatos soportados, 5 no soportados → `ValueError`, OCR entero/decimal/vacío/blanco |
| `test_operaciones.py` | 16 | 9 operaciones básicas, división entre 0, operación desconocida, negativos, precisión decimal |

---

## 🧩 Estructura del proyecto

```
image-calculator/
├── main.py              ← Punto de entrada (lanza GUI)
├── terminal.py          ← Modo terminal para pruebas rápidas
├── requirements.txt     ← Dependencias Python
├── LICENSE
├── CHANGELOG.md         ← Historial de cambios
├── ROADMAP.md           ← Trayectoria del proyecto
├── nucleo/
│   ├── lector.py        ← Carga imagen + preprocesado + OCR
│   └── operaciones.py   ← Lógica de las 9 operaciones
├── gui/
│   └── app.py           ← Interfaz gráfica tkinter
└── tests/
    ├── conftest.py      ← Fixtures compartidas
    ├── test_lector.py   ← Tests del módulo OCR
    └── test_operaciones.py ← Tests de operaciones
```

---

## 📋 Operaciones disponibles

| Operación | Ejemplo |
|-----------|-------------|
| Suma | `42 + 18 = 60` |
| Resta | `42 - 18 = 24` |
| Multiplicación | `42 × 18 = 756` |
| División | `42 ÷ 18 = 2.3333` |
| Comparar | `42 > 18 → A es mayor` |
| Concatenar | `42` y `18` → `4218` |
| Máximo | `Máximo entre 42 y 18: 42` |
| Mínimo | `Mínimo entre 42 y 18: 18` |
| Promedio | `Promedio de 42 y 18: 30.0` |

## 🖼️ Formatos soportados

`PNG` · `JPG` / `JPEG` · `WEBP` · `BMP` · `TIFF`

---

## ⚠️ Nota Windows — Tesseract

Si Tesseract no se detecta automáticamente, añade esto al principio de `nucleo/lector.py`:

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
| v0.3 | ✅ | Suite de 31 tests con pytest |
| v0.4 | 🔜 | Binario `.exe` / `.app` con PyInstaller |
| v0.5 | 🔮 | Bot de Telegram |
| v1.0 | 🔮 | Versión estable completa |

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Pasos:

1. Haz fork del repositorio
2. Crea una rama: `git checkout -b feature/nueva-funcionalidad`
3. Haz tus cambios y asegúrate de que los tests pasan: `python -m pytest tests/ -v`
4. Haz commit: `git commit -m 'Add: nueva funcionalidad'`
5. Haz push: `git push origin feature/nueva-funcionalidad`
6. Abre un Pull Request

### Ideas para contribuir

- Soporte para más idiomas en el OCR
- Nuevas operaciones matemáticas
- Mejoras en el preprocesado de imagen
- Traducción del README al inglés
- Tests adicionales

---

## 📄 Licencia

MIT — puedes usar, modificar y distribuir libremente. Ver [LICENSE](LICENSE).
