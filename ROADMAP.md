# 🗺️ Roadmap — Image Calculator

Esta es la trayectoria del proyecto. Las versiones son orientativas.

---

## ✅ v0.1 — Base (completado)
- [x] Núcleo OCR con `pytesseract`
- [x] Función `extraer_numero()` con preprocesado
- [x] Función `operar()` con 9 operaciones
- [x] Versión terminal para pruebas

## ✅ v0.2 — GUI de escritorio (completado)
- [x] Interfaz gráfica con `tkinter`
- [x] Punto de entrada único (`main.py`)
- [x] README profesional

---

## 🔜 v0.3 — Tests y estabilidad
- [ ] Suite de tests con `pytest` (`tests/`)
- [ ] Test: `extraer_numero()` con imagen válida
- [ ] Test: `extraer_numero()` con imagen sin número → `ValueError`
- [ ] Test: `operar()` división entre 0 → mensaje controlado
- [ ] Test: todas las operaciones devuelven string correcto
- [ ] Imágenes demo en `demo/` para probar sin fotos propias

## 🔜 v0.4 — Distribución
- [ ] Empaquetar como `.exe` (Windows) con PyInstaller
- [ ] Empaquetar como `.app` (macOS) con PyInstaller
- [ ] Release en GitHub con binario descargable

## 🔮 v0.5 — Bot de Telegram
- [ ] Integración con `python-telegram-bot`
- [ ] El usuario manda dos fotos → el bot responde con el resultado
- [ ] Despliegue en Railway (plan gratuito)
- [ ] Selección de operación por botones inline

## 🔮 v1.0 — Versión estable
- [ ] Soporte para múltiples números por imagen
- [ ] Historial de operaciones exportable a CSV
- [ ] Modo oscuro / claro seleccionable en la GUI
- [ ] Documentación completa en español e inglés

---

> Las ideas y sugerencias son bienvenidas — abre un [issue](https://github.com/alvarofernandezmota-tech/image-calculator/issues) o haz una PR.
