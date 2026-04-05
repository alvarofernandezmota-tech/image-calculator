class Operaciones:
    """
    Aplica operaciones matemáticas entre dos números extraídos de imágenes.

    Uso:
        ops = Operaciones()
        resultado = ops.aplicar("Suma", 42.0, 18.0)
        # → "42.0 + 18.0 = 60.0"

    Operaciones disponibles (ver LISTA):
        Suma, Resta, Multiplicación, División, Comparar,
        Concatenar, Máximo, Mínimo, Promedio
    """

    # Lista oficial de operaciones — usada por la GUI para el menú desplegable
    LISTA = [
        "Suma", "Resta", "Multiplicación", "División",
        "Comparar", "Concatenar", "Máximo", "Mínimo", "Promedio"
    ]

    def aplicar(self, operacion: str, a: float, b: float) -> str:
        """
        Despacha la operación al método correspondiente.

        Args:
            operacion: Nombre de la operación (debe estar en LISTA).
            a: Primer número (extraído de la imagen A).
            b: Segundo número (extraído de la imagen B).

        Returns:
            str: Resultado formateado como cadena legible.

        Raises:
            ValueError: Si la operación no está en LISTA.
        """
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
            raise ValueError(
                f"Operación desconocida: '{operacion}'. "
                f"Operaciones válidas: {', '.join(self.LISTA)}"
            )
        return metodos[operacion](a, b)

    # --- Operaciones aritméticas ---

    def sumar(self, a: float, b: float) -> str:
        """Suma A + B."""
        return f"{a} + {b} = {a + b}"

    def restar(self, a: float, b: float) -> str:
        """Resta A - B."""
        return f"{a} - {b} = {a - b}"

    def multiplicar(self, a: float, b: float) -> str:
        """Multiplica A × B."""
        return f"{a} × {b} = {a * b}"

    def dividir(self, a: float, b: float) -> str:
        """
        Divide A ÷ B. Devuelve mensaje de error si B es 0
        (no lanza excepción para no romper la GUI).
        """
        if b == 0:
            return "Error: no se puede dividir entre 0"
        return f"{a} ÷ {b} = {round(a / b, 4)}"

    # --- Operaciones de comparación y texto ---

    def comparar(self, a: float, b: float) -> str:
        """Compara A y B e indica cuál es mayor o si son iguales."""
        if a > b:   return f"{a} > {b}  →  A es mayor"
        elif a < b: return f"{a} < {b}  →  B es mayor"
        else:       return f"{a} = {b}  →  Son iguales"

    def concatenar(self, a: float, b: float) -> str:
        """
        Une los dígitos de A y B como si fueran texto.
        Ejemplo: 12 y 34 → "1234"
        Los decimales se omiten si el número es entero.
        """
        sa = str(int(a)) if a == int(a) else str(a)
        sb = str(int(b)) if b == int(b) else str(b)
        return f"Concatenación: {sa + sb}"

    # --- Operaciones estadísticas ---

    def maximo(self, a: float, b: float) -> str:
        """Devuelve el mayor entre A y B."""
        return f"Máximo entre {a} y {b}: {max(a, b)}"

    def minimo(self, a: float, b: float) -> str:
        """Devuelve el menor entre A y B."""
        return f"Mínimo entre {a} y {b}: {min(a, b)}"

    def promedio(self, a: float, b: float) -> str:
        """Calcula el promedio (media aritmética) de A y B."""
        return f"Promedio de {a} y {b}: {(a + b) / 2}"
