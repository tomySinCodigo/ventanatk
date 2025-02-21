import tkinter as tk
from ventana_tk2.barra import Barra


class VentanaTk(tk.Tk):
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

    def setSize(self, w:int, h=int, tam=3/5):
        self.geometry(f"{w}x{h}")
        self.bar.setSize(w, h, tam=tam)