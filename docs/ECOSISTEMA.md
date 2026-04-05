# 🌐 Ecosistema THEA IA — Relación entre repos

> Este documento describe cómo `image-calculator` y `thdora` trabajan de forma independiente pero están diseñados para integrarse.

---

## Los dos repos

| Repo | Qué es | Estado |
|------|--------|--------|
| [`image-calculator`](https://github.com/alvarofernandezmota-tech/image-calculator) | OCR + Parser IA de documentos (tickets, facturas) | v0.5 ✅, v1.0 🔶 |
| [`thdora`](https://github.com/alvarofernandezmota-tech/thdora) | Asistente personal IA — Bot Telegram + FastAPI + SQLite | v0.8.1 ✅ |

Cada repo funciona de forma **completamente independiente**. No hay dependencias cruzadas en el código — la integración es por copia de módulo.

---

## Cómo se integran

```
┌─────────────────────────────────────────────────────────────┐
│                     THEA IA (ecosistema)                    │
│                                                             │
│  ┌─────────────────────┐     ┌─────────────────────────┐   │
│  │      THDORA         │     │    IMAGE-CALCULATOR      │   │
│  │                     │     │                          │   │
│  │  Bot Telegram       │     │  OCR (Tesseract)         │   │
│  │  FastAPI REST       │◄────│  Parser IA (Groq)        │   │
│  │  SQLite             │     │  Tabla editable (GUI)    │   │
│  │  Citas / Hábitos    │     │  Standalone desktop app  │   │
│  │  Tracking gastos    │     │                          │   │
│  └─────────────────────┘     └─────────────────────────┘   │
│                                                             │
│  Groq API (gratuita) ←──── usada por ambos repos            │
└─────────────────────────────────────────────────────────────┘
```

---

## Módulo que viaja entre repos

El módulo `nucleo/parser.py` de `image-calculator` se copia como `src/ai/ticket_parser.py` en `thdora` cuando esté listo.

**No es una dependencia de paquete** — es una copia directa. Esto mantiene cada repo autónomo.

```python
# En image-calculator (desarrollo y pruebas)
from nucleo.parser import parsear_ticket

# En thdora (producción, misma lógica)
from src.ai.ticket_parser import parsear_ticket
```

---

## Groq: patrón compartido

Ambos repos usan Groq de la misma forma:

```python
# thdora: src/ai/groq_client.py (ya existe)
# image-calculator: nucleo/parser.py (a implementar)

# Misma API key, mismo modelo, mismos patrones async
GROQ_API_KEY=tu_key  # en .env de cada repo
```

---

## Desarrollo independiente

```
image-calculator/          thdora/
├── nucleo/                ├── src/ai/
│   └── parser.py  ──────► │   └── ticket_parser.py
├── gui/                   ├── src/bot/
│   └── app.py             │   └── handlers/
└── tests/                 └── tests/
    └── test_parser.py
```

- Desarrollas y testeas `parser.py` en `image-calculator`
- Cuando está estable, lo copias a `thdora`
- Cada repo tiene sus propios tests
- Ninguno depende del otro para funcionar

---

## Roadmap de integración

| Paso | Dónde | Qué |
|------|-------|-----|
| 1 | `image-calculator` | Implementar `nucleo/parser.py` con Groq |
| 2 | `image-calculator` | GUI tabla editable + tests |
| 3 | `image-calculator` | Release v1.0 |
| 4 | `thdora` | Copiar como `src/ai/ticket_parser.py` |
| 5 | `thdora` | Handler bot: recibir foto → parsear → mostrar tabla |
| 6 | `thdora` | Guardar gastos en SQLite (tracking F10) |
