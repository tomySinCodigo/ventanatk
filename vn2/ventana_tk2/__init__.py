import tkinter as tk
from tkinter import ttk
from ventana_tk2.barra import Barra
from tkinterdnd2 import TkinterDnD, DND_FILES
from ventana_tk2.widgets import MiGrip


class VentanaTk(TkinterDnD.Tk):
    def __init__(self, **kw):
        super().__init__(**kw)
        self._config_VentanaTk()

    
    def _config_VentanaTk(self):
        self.columnconfigure(0, weight=1)
        self.overrideredirect(True)

        self.bar = Barra(self)
        self.bar.grid(row=0, column=0, sticky='wens')
        self.setSize(800, 100)
        self.bar.cnf(mody=4)
        self.bar.ontop()

        self.drop_target_register(DND_FILES)
        self.dnd_bind("<<Drop>>", self.obtenDrop)

    def addGrip(self, bg="gray"):
        grip = MiGrip(self, bg=bg)
        grip.place(relx=1.0, rely=1.0, anchor="se")
        grip.bind("<Button-1>", grip.start_resize)  # Detectar clic inicial
        grip.bind("<B1-Motion>", grip.perform_resize)

    def setSize(self, w:int, h=int, tam=3/5):
        """size window and side (tam)"""
        self.geometry(f"{w}x{h}")
        self.bar.setSize(w, h, tam=tam)

    def toClipboard(self, texto:str):
        """texto to clipboard"""
        self.clipboard_clear()
        self.clipboard_append()
        self.update()

    def obtenDrop(self, e):
        archivos = self.fix(e.data)
        print(type(archivos))
        print(archivos)

    def fix(self, texto:str) -> list:
        """retorna list de strings sin llaves"""
        def getIndices(texto:str):
            indices = []
            i = 0
            for _ in range(texto.count(":")):
                if ":" in texto[i:]:
                    i = texto.index(":", i+1)
                    indices.append(i-1)
            indices.append(-1)
            return indices
        rutas = []
        inicio = 0
        for fin in getIndices(texto)[1:]:
            ruta = texto[inicio:] if fin==-1 else texto[inicio:fin]
            rutas.append(ruta.strip("{} "))    
            inicio = fin
        return rutas
    
