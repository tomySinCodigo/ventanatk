import tkinter as tk
from tkinter import ttk
from ventana_tk2 import VentanaTk


if __name__ == '__main__':
    vn = VentanaTk()
    vn.setSize(w=650, h=250, tam=2/6)

    vn.rowconfigure(1, weight=1)
    # lista = tk.StringVar(value=list(range(25)))
    # liw = tk.Listbox(vn, listvariable=lista, bg="gray")
    # liw.grid(row=1, column=0, sticky='wens')

    ico = tk.PhotoImage(file="16w.png")
    vn.bar.setIconMenu(image=ico)
    vn.bar.setBg("#383838")
    # vn.bar.fm_bts.bt_fw.bg="yellow"
    
    vn.addGrip() #penultimo para colocar encima del contenido
    vn.setBg("red") # cambia color de fondo y de grip

    vn.mainloop()