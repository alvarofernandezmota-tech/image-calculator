# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [v0.3] - 2026-04-05

### Added
- Suite de tests con `pytest` — 22 tests en total
- `tests/test_lector.py` — tests parametrizados para los 6 formatos soportados (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`)
- `tests/test_lector.py` — tests para formatos no soportados (`.gif`, `.pdf`, `.svg`, `.txt`, `.mp4`) → `ValueError`
- `tests/test_lector.py` — tests del pipeline OCR completo con mock: número entero, decimal, imagen sin número, imagen en blanco
- `tests/test_operaciones.py` — tests de las 9 operaciones: suma, resta, multiplicación, división, comparar, concatenar, máximo, mínimo, promedio
- `tests/test_operaciones.py` — tests edge: división entre 0, operación desconocida, números negativos, precisión decimal
- `tests/test_operaciones.py` — test que garantiza que todas las operaciones devuelven `str`
- `tests/conftest.py` — fixtures compartidas
- Tests usan `unittest.mock` — no requieren Tesseract instalado, corren en cualquier máquina y CI

---

## [v0.2] - 2026-04-04

### Added
- Interfaz gráfica de escritorio con `tkinter` (`gui/app.py`)
- Punto de entrada único `main.py`
- README profesional con badges, instrucciones de instalación y uso
- Soporte para selección de operación mediante menú desplegable en la GUI

---

## [v0.1] - 2026-04-04

### Added
- Núcleo OCR con `pytesseract` + preprocesado con `opencv` (`nucleo/lector.py`)
- Clase `LectorImagen` con métodos `cargar()`, `preprocesar()`, `extraer_numero()`
- Soporte para formatos: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`
- Clase `Operaciones` con 9 operaciones: Suma, Resta, Multiplicación, División, Comparar, Concatenar, Máximo, Mínimo, Promedio
- Versión terminal para pruebas (`terminal.py`)
