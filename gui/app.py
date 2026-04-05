import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.lector import LectorImagen
from nucleo.operaciones import Operaciones

# Tamaño de la miniatura de imagen en la GUI
THUMB = (220, 160)


class App(tk.Tk):
    """
    Ventana principal de la Calculadora de Imágenes.

    Características:
        - Ventana redimensionable y centrada en pantalla
        - Tamaño inicial proporcional a la pantalla del usuario
        - Tamaño mínimo para que la UI no se rompa
        - Atajo F11 para pantalla completa / Escape para salir de ella
        - Grid expandible: el resultado crece con la ventana
    """

    def __init__(self):
        super().__init__()
        self.title("🖼️  Calculadora de Imágenes")
        self.configure(bg="#1e1e2e")

        # --- Tamaño inicial: 70% del ancho x 80% del alto de la pantalla ---
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla  = self.winfo_screenheight()
        ancho_ventana  = min(int(ancho_pantalla * 0.70), 900)
        alto_ventana   = min(int(alto_pantalla  * 0.80), 700)

        # Centrar la ventana en pantalla
        x = (ancho_pantalla - ancho_ventana) // 2
        y = (alto_pantalla  - alto_ventana)  // 2
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")

        # Tamaño mínimo para que no se rompa el layout
        self.minsize(600, 520)

        # Ventana redimensionable en ambos ejes
        self.resizable(True, True)

        # F11 → pantalla completa | Escape → salir de pantalla completa
        self._pantalla_completa = False
        self.bind("<F11>",    self._toggle_pantalla_completa)
        self.bind("<Escape>", self._salir_pantalla_completa)

        self._setup_estilo()

        self.lector = LectorImagen()
        self.ops    = Operaciones()

        self.ruta_a   = tk.StringVar(value="")
        self.ruta_b   = tk.StringVar(value="")
        self.numero_a = None
        self.numero_b = None

        self._construir_ui()

    # ------------------------------------------------------------------ #
    #  Pantalla completa                                                   #
    # ------------------------------------------------------------------ #

    def _toggle_pantalla_completa(self, event=None):
        """Alterna entre pantalla completa y ventana normal (F11)."""
        self._pantalla_completa = not self._pantalla_completa
        self.attributes("-fullscreen", self._pantalla_completa)

    def _salir_pantalla_completa(self, event=None):
        """Sale de pantalla completa al pulsar Escape."""
        if self._pantalla_completa:
            self._pantalla_completa = False
            self.attributes("-fullscreen", False)

    # ------------------------------------------------------------------ #
    #  Estilos                                                             #
    # ------------------------------------------------------------------ #

    def _setup_estilo(self):
        """Configura el tema visual oscuro (Catppuccin Mocha)."""
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TLabel",
            background="#1e1e2e", foreground="#cdd6f4",
            font=("Segoe UI", 11))
        self.style.configure("TButton",
            font=("Segoe UI", 10, "bold"), padding=6)
        self.style.configure("Accent.TButton",
            background="#89b4fa", foreground="#1e1e2e")
        self.style.map("Accent.TButton",
            background=[("active", "#74c7ec")])
        self.style.configure("TCombobox",
            font=("Segoe UI", 11))

    # ------------------------------------------------------------------ #
    #  Construcción de la UI                                              #
    # ------------------------------------------------------------------ #

    def _construir_ui(self):
        """
        Construye todos los widgets de la ventana principal.

        Estructura del grid (6 columnas, pesos asignados para expansión):
            Fila 0  — Título
            Fila 1  — Subtítulo
            Fila 2  — Paneles A | VS | B
            Fila 3  — Etiqueta operación
            Fila 4  — Combobox operación
            Fila 5  — Botón calcular
            Fila 6  — Resultado (se expande con la ventana)
        """
        # Columnas: los extremos se expanden, el centro es fijo
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=0)
        self.columnconfigure(2, weight=1)

        # La fila del resultado crece cuando se agranda la ventana
        self.rowconfigure(6, weight=1)

        # --- Título ---
        tk.Label(self,
            text="Calculadora de Imágenes",
            bg="#1e1e2e", fg="#89b4fa",
            font=("Segoe UI", 18, "bold")
        ).grid(row=0, column=0, columnspan=3, pady=(18, 4))

        # --- Subtítulo ---
        tk.Label(self,
            text="Carga dos imágenes con números y elige una operación  •  F11 para pantalla completa",
            bg="#1e1e2e", fg="#6c7086",
            font=("Segoe UI", 9)
        ).grid(row=1, column=0, columnspan=3, pady=(0, 10))

        # --- Paneles de imagen ---
        self._panel_imagen(col=0, letra="A", var=self.ruta_a, cmd=self._cargar_a)
        tk.Label(self,
            text="VS",
            bg="#1e1e2e", fg="#fab387",
            font=("Segoe UI", 24, "bold")
        ).grid(row=2, column=1, padx=14, pady=8)
        self._panel_imagen(col=2, letra="B", var=self.ruta_b, cmd=self._cargar_b)

        # --- Operación ---
        tk.Label(self,
            text="Operación:",
            bg="#1e1e2e", fg="#cdd6f4",
            font=("Segoe UI", 11)
        ).grid(row=3, column=0, columnspan=3, pady=(10, 2))

        self.combo = ttk.Combobox(
            self, values=Operaciones.LISTA,
            state="readonly", width=26,
            font=("Segoe UI", 11)
        )
        self.combo.current(0)
        self.combo.grid(row=4, column=0, columnspan=3, pady=4)

        # --- Botón calcular ---
        ttk.Button(
            self, text="⚡  Calcular",
            style="Accent.TButton",
            command=self._calcular
        ).grid(row=5, column=0, columnspan=3, pady=12, ipadx=28, ipady=4)

        # --- Resultado (se expande con la ventana) ---
        self.lbl_resultado = tk.Label(
            self,
            text="El resultado aparecerá aquí",
            bg="#313244", fg="#a6e3a1",
            font=("Segoe UI", 14, "bold"),
            wraplength=600, justify="center",
            relief="flat"
        )
        self.lbl_resultado.grid(
            row=6, column=0, columnspan=3,
            padx=20, pady=(0, 20),
            sticky="nsew"  # se expande en todas las direcciones
        )

    # ------------------------------------------------------------------ #
    #  Paneles de imagen                                                   #
    # ------------------------------------------------------------------ #

    def _panel_imagen(self, col, letra, var, cmd):
        """
        Crea un panel de carga de imagen con miniatura, nombre de archivo
        y número extraído por OCR.

        Args:
            col:   Columna del grid principal donde insertar el panel.
            letra: 'A' o 'B' — identifica el panel.
            var:   StringVar para mostrar el nombre del archivo.
            cmd:   Función a llamar al pulsar el botón de carga.
        """
        marco = tk.Frame(self, bg="#313244", bd=0)
        marco.grid(row=2, column=col, padx=16, pady=8, sticky="n")

        tk.Label(marco,
            text=f"Imagen {letra}",
            bg="#313244", fg="#cba6f7",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=(10, 4))

        canvas = tk.Label(marco,
            bg="#45475a", width=22, height=10,
            text="Sin imagen", fg="#6c7086",
            font=("Segoe UI", 9)
        )
        canvas.pack(padx=10)

        tk.Label(marco,
            textvariable=var,
            bg="#313244", fg="#6c7086",
            font=("Segoe UI", 8),
            wraplength=220
        ).pack(pady=(2, 4))

        ttk.Button(marco,
            text=f"📂  Cargar imagen {letra}",
            command=cmd
        ).pack(pady=(2, 8))

        if letra == "A": self.canvas_a = canvas
        else:            self.canvas_b = canvas

        lbl_num = tk.Label(marco,
            text="Número: —",
            bg="#313244", fg="#f38ba8",
            font=("Segoe UI", 10, "bold")
        )
        lbl_num.pack(pady=(0, 10))

        if letra == "A": self.lbl_num_a = lbl_num
        else:            self.lbl_num_b = lbl_num

    # ------------------------------------------------------------------ #
    #  Carga de imágenes y cálculo                                         #
    # ------------------------------------------------------------------ #

    def _cargar_imagen(self, canvas, lbl_num, var, attr_numero):
        """
        Abre el diálogo de archivo, carga la imagen, genera la miniatura
        y extrae el número con OCR.

        Si OCR falla, muestra el error en rojo sin bloquear la aplicación.
        """
        tipos = [
            ("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff"),
            ("Todos", "*.*")
        ]
        ruta = filedialog.askopenfilename(filetypes=tipos)
        if not ruta:
            return  # El usuario canceló el diálogo

        var.set(os.path.basename(ruta))

        # Generar y mostrar miniatura
        img = Image.open(ruta).convert("RGB")
        img.thumbnail(THUMB)
        photo = ImageTk.PhotoImage(img)
        canvas.config(image=photo, text="")
        canvas.image = photo  # Referencia necesaria para que tkinter no borre la imagen

        # Extraer número con OCR
        try:
            numero = self.lector.extraer_numero(ruta)
            lbl_num.config(text=f"Número: {numero}", fg="#a6e3a1")
            setattr(self, attr_numero, numero)
        except Exception as e:
            lbl_num.config(text=f"⚠ {e}", fg="#f38ba8")
            setattr(self, attr_numero, None)

    def _cargar_a(self):
        """Carga la imagen A."""
        self._cargar_imagen(self.canvas_a, self.lbl_num_a, self.ruta_a, "numero_a")

    def _cargar_b(self):
        """Carga la imagen B."""
        self._cargar_imagen(self.canvas_b, self.lbl_num_b, self.ruta_b, "numero_b")

    def _calcular(self):
        """
        Aplica la operación seleccionada sobre los números extraídos
        y muestra el resultado.

        Muestra un aviso si alguna imagen no ha sido cargada correctamente.
        """
        if self.numero_a is None or self.numero_b is None:
            messagebox.showwarning(
                "Faltan imágenes",
                "Carga las dos imágenes correctamente antes de calcular."
            )
            return
        resultado = self.ops.aplicar(self.combo.get(), self.numero_a, self.numero_b)
        self.lbl_resultado.config(text=resultado, fg="#a6e3a1")


def main():
    """Punto de entrada de la aplicación gráfica."""
    App().mainloop()


if __name__ == "__main__":
    main()
