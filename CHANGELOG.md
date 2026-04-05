# Changelog

Todos los cambios notables de este proyecto se documentan aquí.
Formato basado en [Keep a Changelog](https://keepachangelog.com/es/1.0.0/).

---

## [v0.5] - 2026-04-05

### Added
- Instalador Windows con **Inno Setup 6** (`installer/ImageCalculator.iss`)
- El instalador incluye Tesseract OCR integrado — no requiere instalación manual
- Tesseract se añade automáticamente al PATH del sistema vía registro de Windows
- Acceso directo en el escritorio y en el Menú Inicio
- Release oficial en GitHub con `ImageCalculator-Setup.exe` descargable
- README actualizado con sección de instalación rápida para usuarios finales
- `.gitignore` actualizado para excluir binarios (`dist/`, `build/`, `installer/output/`)

---

## [v0.4] - 2026-04-05

### Added
- `_normalizar_numero()` en `LectorImagen` — detección automática del formato numérico
- Soporte para **formato europeo**: `3,14` → `3.14` / `1.234,56` → `1234.56`
- Soporte para **formato anglosajón**: `1,234.56` → `1234.56`
- Soporte para separadores de miles en ambos formatos
- 7 tests nuevos para `_normalizar_numero()` en `tests/test_lector.py`
- Docstrings completos en todos los métodos de `LectorImagen` y `Operaciones`
- Comentarios de código explicativos en español en todos los módulos del núcleo

### Changed
- `extraer_numero()` usa el nuevo regex mejorado para detectar separadores de miles y decimales
- Mensaje de error de `ValueError` más descriptivo con instrucciones para el usuario
- `operaciones.py` completamente documentado con docstrings por método

---

## [v0.3] - 2026-04-05

### Added
- Suite de **31 tests** con `pytest`
- `tests/test_lector.py` — tests parametrizados para los 6 formatos soportados (`.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`)
- `tests/test_lector.py` — tests para 5 formatos no soportados → `ValueError`
- `tests/test_lector.py` — tests del pipeline OCR completo con mock
- `tests/test_operaciones.py` — tests de las 9 operaciones básicas
- `tests/test_operaciones.py` — tests edge: división entre 0, operación desconocida, negativos, precisión decimal
- `tests/conftest.py` — fixtures compartidas
- Tests con `unittest.mock` — no requieren Tesseract, corren en cualquier máquina

### Changed
- README actualizado: sección de tests, tabla de operaciones con ejemplos, estructura completa
- ROADMAP actualizado: v0.3 marcada como completada

---

## [v0.2] - 2026-04-04

### Added
- Interfaz gráfica de escritorio con `tkinter` (`gui/app.py`)
- Punto de entrada único `main.py`
- README profesional con badges, instrucciones de instalación y uso
- Soporte para selección de operación mediante menú desplegable en la GUI
- `CHANGELOG.md` y `ROADMAP.md`

---

## [v0.1] - 2026-04-04

### Added
- Núcleo OCR con `pytesseract` + preprocesado con `opencv` (`nucleo/lector.py`)
- Clase `LectorImagen` con métodos `cargar()`, `preprocesar()`, `extraer_numero()`
- Soporte para formatos: `.png`, `.jpg`, `.jpeg`, `.webp`, `.bmp`, `.tiff`
- Clase `Operaciones` con 9 operaciones: Suma, Resta, Multiplicación, División, Comparar, Concatenar, Máximo, Mínimo, Promedio
- Versión terminal para pruebas (`terminal.py`)
- `requirements.txt` con dependencias
