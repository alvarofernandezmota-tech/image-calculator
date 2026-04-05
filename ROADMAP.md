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

## ✅ v0.5 — Distribución Windows (completado — 2026-04-05)
- [x] Empaquetado como `.exe` con PyInstaller
- [x] Instalador Windows con Inno Setup 6 (`installer/ImageCalculator.iss`)
- [x] Tesseract OCR integrado en el instalador — sin configuración manual
- [x] Tesseract añadido automáticamente al PATH del sistema
- [x] Release oficial en GitHub con `ImageCalculator-Setup.exe` descargable
- [x] README actualizado con instrucciones para usuarios finales

---

## 🔶 v1.0 — Lector de documentos con IA (en desarrollo)

> **Objetivo:** leer tickets, facturas y recibos completos, extraer todos los conceptos y precios, y presentarlos en una tabla editable antes de calcular el total.

### Arquitectura v1.0

```
imagen → OCR (Tesseract) → texto crudo
                               ↓
                    Parser IA (Groq API)
                               ↓
                    datos limpios (JSON)
                    [{"concepto": "Leche", "precio": 1.25}, …]
                               ↓
                    Tabla editable (GUI tkinter)
                    usuario corrige si hay errores OCR
                               ↓
                           TOTAL
```

### Módulos nuevos

```
nucleo/
└── parser.py        ← Parser IA con Groq + fallback heurístico
gui/
└── app.py           ← GUI actualizada con tabla editable y selector de modo
```

### Tareas
- [ ] `nucleo/parser.py` — cliente Groq que recibe texto OCR y devuelve JSON limpio
- [ ] Sistema de plantillas por modo (Supermercado / Restaurante / Factura)
- [ ] Fallback heurístico si Groq no está disponible (sin internet)
- [ ] GUI nueva: selector de modo + tabla editable (concepto + precio editables)
- [ ] Botones: añadir fila, eliminar fila, calcular total
- [ ] Tests del parser con textos OCR de ejemplo
- [ ] Actualizar `requirements.txt` con `groq` o `httpx`
- [ ] Documentación de integración con THdora

### Variables de entorno necesarias

```env
GROQ_API_KEY=tu_api_key_aqui     # Gratuita en console.groq.com
GROQ_MODEL=llama3-8b-8192        # opcional, por defecto
```

---

## 🔮 Integración con THdora (ecosistema THEA IA)

> **Objetivo:** el módulo `nucleo/parser.py` se integra en [THdora](https://github.com/alvarofernandezmota-tech/thdora) como `src/ai/ticket_parser.py`

El usuario manda una foto de un ticket por Telegram → THDORA usa el parser para extraer los gastos → los registra automáticamente.

Flujo completo dentro de THdora:

```
[usuario] foto ticket por Telegram
       ↓
[bot]  recibe la imagen
       ↓
[nucleo/lector.py]  OCR → texto crudo       ← viene de image-calculator
       ↓
[src/ai/ticket_parser.py]  Groq → JSON      ← viene de image-calculator
       ↓
[bot]  muestra tabla editable al usuario
       ↓
[usuario] confirma o edita
       ↓
[src/db]  guarda el gasto en SQLite
```

Estas son las fases del roadmap de THdora donde se integra:
- **F12 — IA conversacional**: el parser de tickets es la primera habilidad visual del bot
- **F10 — Tracking personal**: los gastos del ticket pueden alimentar el tracking diario

---

## 🔮 v1.1 — Bot de Telegram standalone
- [ ] Integración con `python-telegram-bot`
- [ ] El usuario manda foto de ticket → el bot responde con tabla de gastos
- [ ] Selección de operación por botones inline
- [ ] Despliegue en Railway (plan gratuito)

## 🔮 v2.0 — Versión completa
- [ ] Historial de tickets exportable a CSV / Excel
- [ ] Estadísticas de gasto por categoría
- [ ] Modo oscuro / claro en la GUI
- [ ] GitHub Actions CI — tests automáticos en cada PR
- [ ] Documentación completa en español e inglés

---

> Las ideas y sugerencias son bienvenidas — abre un [issue](https://github.com/alvarofernandezmota-tech/image-calculator/issues) o haz una PR.
