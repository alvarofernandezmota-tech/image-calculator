#!/usr/bin/env python3
"""
Calculadora de Imágenes — Versión Terminal
==========================================
Para probar el núcleo sin interfaz gráfica.

Uso:
    python terminal.py imagen1.png imagen2.png
    python terminal.py   (modo interactivo)
"""
import sys
from nucleo.lector import LectorImagen
from nucleo.operaciones import Operaciones

lector = LectorImagen()
ops    = Operaciones()

def main():
    if len(sys.argv) == 3:
        ruta_a, ruta_b = sys.argv[1], sys.argv[2]
    else:
        ruta_a = input("Ruta imagen A: ").strip()
        ruta_b = input("Ruta imagen B: ").strip()

    print("\n🔍 Leyendo imágenes...")
    try:
        num_a = lector.extraer_numero(ruta_a)
        print(f"  → Imagen A: {num_a}")
        num_b = lector.extraer_numero(ruta_b)
        print(f"  → Imagen B: {num_b}")
    except Exception as e:
        print(f"  ❌ Error: {e}")
        return

    print("\nOperaciones disponibles:")
    for i, op in enumerate(Operaciones.LISTA, 1):
        print(f"  {i}. {op}")

    try:
        eleccion = int(input("\nElige una operación (número): ")) - 1
        operacion = Operaciones.LISTA[eleccion]
    except (ValueError, IndexError):
        print("Operación no válida.")
        return

    resultado = ops.aplicar(operacion, num_a, num_b)
    print(f"\n✅ {resultado}\n")

if __name__ == "__main__":
    main()
