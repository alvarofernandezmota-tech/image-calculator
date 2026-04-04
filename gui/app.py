import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from PIL import Image, ImageTk
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from nucleo.lector import LectorImagen
from nucleo.operaciones import Operaciones

THUMB = (220, 160)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🖼️  Calculadora de Imágenes")
        self.resizable(False, False)
        self.configure(bg="#1e1e2e")
        self._setup_estilo()
        self.lector = LectorImagen()
        self.ops    = Operaciones()
        self.ruta_a = tk.StringVar(value="")
        self.ruta_b = tk.StringVar(value="")
        self.numero_a = None
        self.numero_b = None
        self._construir_ui()

    def _setup_estilo(self):
        self.style = ttk.Style(self)
        self.style.theme_use("clam")
        self.style.configure("TLabel",   background="#1e1e2e", foreground="#cdd6f4", font=("Segoe UI", 11))
        self.style.configure("TButton",  font=("Segoe UI", 10, "bold"), padding=6)
        self.style.configure("Accent.TButton", background="#89b4fa", foreground="#1e1e2e")
        self.style.map("Accent.TButton", background=[("active", "#74c7ec")])
        self.style.configure("TCombobox", font=("Segoe UI", 11))

    def _construir_ui(self):
        tk.Label(self, text="Calculadora de Imágenes", bg="#1e1e2e",
                 fg="#89b4fa", font=("Segoe UI", 16, "bold")).grid(row=0, column=0, columnspan=3, pady=(16, 4))
        tk.Label(self, text="Carga dos imágenes con números y elige una operación",
                 bg="#1e1e2e", fg="#6c7086", font=("Segoe UI", 9)).grid(row=1, column=0, columnspan=3, pady=(0,10))
        self._panel_imagen(col=0, letra="A", var=self.ruta_a, cmd=self._cargar_a)
        self._panel_imagen(col=2, letra="B", var=self.ruta_b, cmd=self._cargar_b)
        tk.Label(self, text="VS", bg="#1e1e2e", fg="#fab387",
                 font=("Segoe UI", 22, "bold")).grid(row=2, column=1, padx=14, pady=8)
        tk.Label(self, text="Operación:", bg="#1e1e2e", fg="#cdd6f4",
                 font=("Segoe UI", 11)).grid(row=4, column=0, columnspan=3, pady=(10, 2))
        self.combo = ttk.Combobox(self, values=Operaciones.LISTA, state="readonly",
                                  width=22, font=("Segoe UI", 11))
        self.combo.current(0)
        self.combo.grid(row=5, column=0, columnspan=3, pady=4)
        ttk.Button(self, text="⚡  Calcular", style="Accent.TButton",
                   command=self._calcular).grid(row=6, column=0, columnspan=3, pady=12, ipadx=20)
        self.lbl_resultado = tk.Label(self, text="Resultado aparecerá aquí",
                                      bg="#313244", fg="#a6e3a1",
                                      font=("Segoe UI", 13, "bold"),
                                      width=42, height=3, relief="flat", wraplength=400)
        self.lbl_resultado.grid(row=7, column=0, columnspan=3, padx=14, pady=(0, 16))

    def _panel_imagen(self, col, letra, var, cmd):
        marco = tk.Frame(self, bg="#313244", bd=0)
        marco.grid(row=2, column=col, padx=14, pady=8)
        tk.Label(marco, text=f"Imagen {letra}", bg="#313244",
                 fg="#cba6f7", font=("Segoe UI", 11, "bold")).pack(pady=(8,4))
        canvas = tk.Label(marco, bg="#45475a", width=220, height=160,
                          text="Sin imagen", fg="#6c7086", font=("Segoe UI", 9))
        canvas.pack(padx=8)
        tk.Label(marco, textvariable=var, bg="#313244", fg="#6c7086",
                 font=("Segoe UI", 8), wraplength=220).pack(pady=(2,4))
        ttk.Button(marco, text=f"📂  Cargar imagen {letra}", command=cmd).pack(pady=(2,8))
        if letra == "A": self.canvas_a = canvas
        else:            self.canvas_b = canvas
        lbl_num = tk.Label(marco, text="Número: —", bg="#313244",
                           fg="#f38ba8", font=("Segoe UI", 10, "bold"))
        lbl_num.pack(pady=(0,8))
        if letra == "A": self.lbl_num_a = lbl_num
        else:            self.lbl_num_b = lbl_num

    def _cargar_imagen(self, canvas, lbl_num, var, attr_numero):
        tipos = [("Imágenes", "*.png *.jpg *.jpeg *.webp *.bmp *.tiff"), ("Todos", "*.*")]
        ruta = filedialog.askopenfilename(filetypes=tipos)
        if not ruta: return
        var.set(os.path.basename(ruta))
        img = Image.open(ruta).convert("RGB")
        img.thumbnail(THUMB)
        photo = ImageTk.PhotoImage(img)
        canvas.config(image=photo, text="")
        canvas.image = photo
        try:
            numero = self.lector.extraer_numero(ruta)
            lbl_num.config(text=f"Número: {numero}", fg="#a6e3a1")
            setattr(self, attr_numero, numero)
        except Exception as e:
            lbl_num.config(text=f"⚠ {e}", fg="#f38ba8")
            setattr(self, attr_numero, None)

    def _cargar_a(self): self._cargar_imagen(self.canvas_a, self.lbl_num_a, self.ruta_a, "numero_a")
    def _cargar_b(self): self._cargar_imagen(self.canvas_b, self.lbl_num_b, self.ruta_b, "numero_b")

    def _calcular(self):
        if self.numero_a is None or self.numero_b is None:
            messagebox.showwarning("Faltan imágenes", "Carga las dos imágenes primero.")
            return
        resultado = self.ops.aplicar(self.combo.get(), self.numero_a, self.numero_b)
        self.lbl_resultado.config(text=resultado, fg="#a6e3a1")


def main():
    App().mainloop()

if __name__ == "__main__":
    main()
