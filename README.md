# 🖼️ Image Calculator

> Lee números en imágenes y los opera entre sí. Python + OCR + GUI.

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green)](LICENSE)
[![OCR](https://img.shields.io/badge/OCR-Tesseract-orange)](https://github.com/tesseract-ocr/tesseract)
[![Version](https://img.shields.io/badge/version-0.5.0-informational)](CHANGELOG.md)
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

## 🔮 Visión v1.0 — Lector de documentos con tabla editable

La evolución natural del proyecto es leer **documentos completos** (tickets, facturas, restaurantes) y extraer todos los conceptos y precios para operar con ellos. El usuario puede **corregir los datos antes de calcular**, evitando errores del OCR.

```
[foto ticket supermercado]
       ↓  OCR
  texto crudo
       ↓  Parser + Plantilla
  datos limpios
       ↓  Tabla editable
  usuario revisa y corrige
       ↓  Calcular
     TOTAL
```

---

## 🧠 Arquitectura del parser y las plantillas

### ¿Por qué plantillas?

Detectar automáticamente el tipo de documento es difícil y propenso a errores. La solución más robusta y mantenible es que el **usuario seleccione el modo** (Supermercado, Restaurante, Factura…) y el programa cargue la plantilla correspondiente. Así el parser sabe exactamente qué patrones buscar y qué ignorar.

### Qué hace el parser

El parser convierte el texto crudo del OCR en datos limpios estructurados:

| Entrada (texto OCR) | Salida (datos limpios) |
|---|---|
| `"Leche entera 1L       1,25"` | `{"concepto": "Leche entera 1L", "precio": 1.25}` |
| `"Pan molde grande      0,89"` | `{"concepto": "Pan molde grande", "precio": 0.89}` |
| `"TOTAL                 3,82"` | *(ignorado)* |

**Pasos internos del parser:**
1. **Filtra líneas basura** — elimina TOTAL, IVA, nombre tienda, dirección, teléfono, NIF, fechas
2. **Detecta el patrón precio** — busca líneas que terminen con un número decimal
3. **Limpia el concepto** — elimina espacios extra y caracteres raros del OCR
4. **Normaliza el precio** — convierte `1,25` → `1.25` (float operable)

### Estructura de plantillas

Cada modo tiene sus propias reglas:

```python
PLANTILLAS = {
    "supermercado": {
        "patron_precio": r'^(.+?)\s{2,}(\d+[,\.]\d{2})\s*$',
        "ignorar": ["total", "iva", "subtotal", "fecha", "nif", "tel", "cif"]
    },
    "restaurante": {
        "patron_precio": r'^(\d+)[xX]\s*(.+?)\s+(\d+[,\.]\d{2})\s*$',
        "ignorar": ["total", "iva", "cubierto", "servicio"]
    },
    "factura": {
        "patron_precio": r'(.+?)\s+(\d+)\s+(\d+[,\.]\d{2})\s+(\d+[,\.]\d{2})\s*$',
        "ignorar": ["subtotal", "iva", "base imponible", "total"]
    }
}
```

Las plantillas son **ampliables**: si un supermercado tiene un formato raro, se añade una plantilla nueva sin tocar el resto del código.

---

## 🔄 Flujo completo del programa (v1.0)

```
┌─────────────────────────────────────────────────────────┐
│  1. USUARIO carga imagen (ticket / factura / restaurante)│
│  2. Elige MODO: Supermercado | Restaurante | Factura     │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  3. OCR — Tesseract                                      │
│     imagen.png  →  texto crudo                           │
│     "Leche entera 1L       1,25\nPan molde     0,89\n…" │
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  4. PARSER + PLANTILLA  (nucleo/parser.py)               │
│     Carga la plantilla del modo elegido                  │
│     Filtra basura → detecta líneas de producto           │
│     Extrae concepto + precio → lista de dicts            │
│     [{"concepto": "Leche entera 1L", "precio": 1.25}, …]│
└──────────────────────┬──────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────┐
│  5. TABLA EDITABLE  (gui/app.py)                         │
│     Muestra los datos limpios fila por fila              │
│     Usuario puede editar concepto y precio               │
│     Usuario puede añadir o eliminar filas                │
│     Pulsa "Calcular" → suma todos los precios → TOTAL    │
└─────────────────────────────────────────────────────────┘
```

### ¿Por qué tabla editable?

El OCR no es perfecto. Puede leer `L3che` en vez de `Leche`, o saltarse una línea. La tabla editable da al usuario el **control final** sobre los datos antes de calcular, haciendo el resultado siempre fiable independientemente de la calidad de la imagen.

---

## 🚀 Instalación

### ⬇️ Instalador para Windows (recomendado)

La forma más fácil. El instalador incluye todo — la aplicación y Tesseract OCR — sin configuración manual.

1. Ve a la sección [**Releases**](https://github.com/alvarofernandezmota-tech/image-calculator/releases/latest)
2. Descarga `ImageCalculator-Setup.exe`
3. Ejecuta el instalador y sigue los pasos
4. ¡Listo! La app aparecerá en el menú Inicio y en el escritorio

> **Nota:** El instalador requiere permisos de administrador para instalar Tesseract OCR correctamente.

---

### 🛠️ Instalación manual (desarrolladores)

#### 1. Instala Tesseract (motor OCR)

| Sistema | Instrucción |
|---------|-------------|
| Windows | [Descargar instalador](https://github.com/UB-Mannheim/tesseract/wiki) |
| macOS   | `brew install tesseract` |
| Linux   | `sudo apt install tesseract-ocr` |

#### 2. Clona el repositorio

```bash
git clone https://github.com/alvarofernandezmota-tech/image-calculator.git
cd image-calculator
```

#### 3. Instala dependencias Python

```bash
pip install -r requirements.txt
```

#### 4. Ejecuta

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
├── installer/
│   ├── ImageCalculator.iss  ← Script Inno Setup
│   └── output/          ← Instalador generado (no versionado)
├── nucleo/
│   ├── lector.py        ← Carga imagen + preprocesado + OCR
│   ├── operaciones.py   ← Lógica de las 9 operaciones
│   └── parser.py        ← [v1.0] Parser + sistema de plantillas
├── gui/
│   └── app.py           ← Interfaz gráfica tkinter (+ tabla editable en v1.0)
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

Si usas la instalación manual y Tesseract no se detecta automáticamente, añade esto al principio de `nucleo/lector.py`:

```python
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

> Si usas el instalador de Windows esto no es necesario — se configura automáticamente.

---

## 🗺️ Roadmap

Ver el [ROADMAP completo](ROADMAP.md).

| Versión | Estado | Qué incluye |
|---------|--------|-------------|
| v0.1 | ✅ | Núcleo OCR + terminal |
| v0.2 | ✅ | GUI de escritorio |
| v0.3 | ✅ | Suite de 31 tests con pytest |
| v0.4 | ✅ | Binario `.exe` con PyInstaller |
| v0.5 | ✅ | Instalador Windows con Inno Setup |
| v1.0 | 🔮 | Parser + plantillas + tabla editable |

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

- Nuevas plantillas para tipos de documento
- Soporte para más idiomas en el OCR
- Nuevas operaciones matemáticas
- Mejoras en el preprocesado de imagen
- Traducción del README al inglés
- Tests adicionales

---

## 📄 Licencia

MIT — puedes usar, modificar y distribuir libremente. Ver [LICENSE](LICENSE).
