from mi_ventana.mi_ventana import MiVentana


class TestVentana(MiVentana):
    def __init__(self):
        super(TestVentana, self).__init__()
        self.bg("#201620")
        self.tam(3/4) # tamano de la ventana (cuando va hacia un lado)
        self.mod_y(4) # margen superior
        self.acciones_itemmenu()
        self.bar.msg(" folder ", fg='black', bg='orange')
        self.asigna_icono('T_24.png')
        self.asigna_icono_menu('T.png')
        self.bar.msg(' MP4 ', fg='black', bg='skyblue', tag='ext_tg')
        # self.barra_color(bg='gray')


    def acciones_itemmenu(self):
        self.item_cmd("mio", self.accion)

    def accion(self):
        print("accion realizada")



if __name__=="__main__":
    app = TestVentana()
    app.mainloop()