class Operaciones:
    """Métodos de interacción entre dos números extraídos de imágenes."""

    LISTA = ["Suma", "Resta", "Multiplicación", "División", "Comparar", "Concatenar", "Máximo", "Mínimo", "Promedio"]

    def aplicar(self, operacion: str, a: float, b: float) -> str:
        metodos = {
            "Suma":           self.sumar,
            "Resta":          self.restar,
            "Multiplicación": self.multiplicar,
            "División":       self.dividir,
            "Comparar":       self.comparar,
            "Concatenar":     self.concatenar,
            "Máximo":         self.maximo,
            "Mínimo":         self.minimo,
            "Promedio":       self.promedio,
        }
        if operacion not in metodos:
            raise ValueError(f"Operación desconocida: {operacion}")
        return metodos[operacion](a, b)

    def sumar(self, a, b):        return f"{a} + {b} = {a + b}"
    def restar(self, a, b):       return f"{a} - {b} = {a - b}"
    def multiplicar(self, a, b):  return f"{a} × {b} = {a * b}"
    def dividir(self, a, b):
        if b == 0:
            return "Error: no se puede dividir entre 0"
        return f"{a} ÷ {b} = {round(a / b, 4)}"
    def comparar(self, a, b):
        if a > b:   return f"{a} > {b}  →  A es mayor"
        elif a < b: return f"{a} < {b}  →  B es mayor"
        else:       return f"{a} = {b}  →  Son iguales"
    def concatenar(self, a, b):
        sa = str(int(a)) if a == int(a) else str(a)
        sb = str(int(b)) if b == int(b) else str(b)
        return f"Concatenación: {sa + sb}"
    def maximo(self, a, b):       return f"Máximo entre {a} y {b}: {max(a, b)}"
    def minimo(self, a, b):       return f"Mínimo entre {a} y {b}: {min(a, b)}"
    def promedio(self, a, b):     return f"Promedio de {a} y {b}: {(a + b) / 2}"
