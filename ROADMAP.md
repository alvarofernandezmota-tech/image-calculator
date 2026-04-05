# 🗺️ Roadmap — Image Calculator

Esta es la trayectoria del proyecto. Las versiones son orientativas.

---

## ✅ v0.1 — Base (completado)
- [x] Núcleo OCR con `pytesseract`
- [x] Clase `LectorImagen` con pipeline: `cargar()` → `preprocesar()` → `extraer_numero()`
- [x] Clase `Operaciones` con 9 operaciones: Suma, Resta, Multiplicación, División, Comparar, Concatenar, Máximo, Mínimo, Promedio
- [x] Versión terminal para pruebas (`terminal.py`)
- [x] Soporte de formatos: PNG, JPG, JPEG, WEBP, BMP, TIFF

## ✅ v0.2 — GUI de escritorio (completado)
- [x] Interfaz gráfica con `tkinter` (`gui/app.py`)
- [x] Punto de entrada único `main.py`
- [x] README profesional con badges e instrucciones
- [x] CHANGELOG.md y ROADMAP.md

## ✅ v0.3 — Tests y estabilidad (completado)
- [x] Suite de 31 tests con `pytest`
- [x] `tests/test_lector.py` — tests parametrizados para los 6 formatos soportados
- [x] `tests/test_lector.py` — tests para 5 formatos no soportados → `ValueError`
- [x] `tests/test_lector.py` — tests del pipeline OCR: número entero, decimal, sin número, imagen en blanco
- [x] `tests/test_operaciones.py` — tests de las 9 operaciones básicas
- [x] `tests/test_operaciones.py` — tests edge: división entre 0, operación desconocida, negativos, precisión decimal
- [x] `tests/conftest.py` — fixtures compartidas
- [x] Tests con `unittest.mock` — no requieren Tesseract, corren en cualquier máquina

---

## 🔜 v0.4 — Distribución
- [ ] Empaquetar como `.exe` (Windows) con PyInstaller
- [ ] Empaquetar como `.app` (macOS) con PyInstaller
- [ ] Release oficial en GitHub con binario descargable
- [ ] Instrucciones de instalación sin Python en README

## 🔮 v0.5 — Bot de Telegram
- [ ] Integración con `python-telegram-bot`
- [ ] El usuario manda dos fotos → el bot responde con el resultado
- [ ] Selección de operación por botones inline
- [ ] Despliegue en Railway (plan gratuito)

## 🔮 v1.0 — Versión estable
- [ ] Soporte para múltiples números por imagen
- [ ] Historial de operaciones exportable a CSV
- [ ] Modo oscuro / claro en la GUI
- [ ] Documentación completa en español e inglés
- [ ] GitHub Actions CI — tests automáticos en cada PR

---

> Las ideas y sugerencias son bienvenidas — abre un [issue](https://github.com/alvarofernandezmota-tech/image-calculator/issues) o haz una PR.
