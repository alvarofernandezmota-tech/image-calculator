# 🗺️ Roadmap — Image Calculator

Esta es la trayectoria del proyecto. Las versiones son orientativas.

---

## ✅ v0.1 — Base (completado — 2026-04-04)
- [x] Núcleo OCR con `pytesseract`
- [x] Clase `LectorImagen` con pipeline: `cargar()` → `preprocesar()` → `extraer_numero()`
- [x] Clase `Operaciones` con 9 operaciones
- [x] Versión terminal para pruebas (`terminal.py`)
- [x] Soporte de formatos: PNG, JPG, JPEG, WEBP, BMP, TIFF

## ✅ v0.2 — GUI de escritorio (completado — 2026-04-04)
- [x] Interfaz gráfica con `tkinter` (`gui/app.py`)
- [x] Punto de entrada único `main.py`
- [x] README profesional con badges e instrucciones
- [x] CHANGELOG.md y ROADMAP.md

## ✅ v0.3 — Tests y estabilidad (completado — 2026-04-05)
- [x] Suite de 31 tests con `pytest`
- [x] Tests parametrizados para los 6 formatos soportados
- [x] Tests para 5 formatos no soportados → `ValueError`
- [x] Tests del pipeline OCR con mock (sin necesidad de Tesseract)
- [x] Tests de las 9 operaciones básicas + edge cases
- [x] `tests/conftest.py` con fixtures compartidas

## ✅ v0.4 — Decimales y documentación (completado — 2026-04-05)
- [x] Detección automática de formato numérico europeo (`3,14` → `3.14`)
- [x] Detección automática de separadores de miles (`1.234,56` / `1,234.56`)
- [x] 7 tests nuevos para `_normalizar_numero()`
- [x] Docstrings completos en todos los métodos del núcleo
- [x] Comentarios en español en todo el código

---

## 🔜 v0.5 — Distribución
- [ ] Empaquetar como `.exe` (Windows) con PyInstaller
- [ ] Empaquetar como `.app` (macOS) con PyInstaller
- [ ] Release oficial en GitHub con binario descargable
- [ ] Instrucciones de instalación sin Python en README

## 🔮 v0.6 — Bot de Telegram
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
