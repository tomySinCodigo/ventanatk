import tkinter as tk
from to.barra import FrameBotones, Barra


if __name__ == '__main__':
    vn = tk.Tk()
    vn.geometry("600x200")
    # fm = tk.Frame(vn, height=14)
    # fm.grid(row=0, column=0, sticky='we')
    # fb = FrameBotones(vn, height=14)
    # fb.grid(row=0, column=1, sticky='we')
    vn.columnconfigure(0, weight=1)

    # BARRA
    bar = Barra(vn)
    bar.grid(row=0, column=0, sticky='we')
    bar.cnf(tam=3/5, modx=50)
    bar.ontop()


    fm_contenido = tk.Frame(vn, bg='gray30')
    fm_contenido.grid(row=1, column=0, sticky='wens')
    vn.rowconfigure(1, weight=1)

    vn.mainloop()