from Tkinter import *


class Gui:

    FONT_COLOR = "white"
    r = Tk()
    nombre = StringVar(r)
    nombre.set("")


    def registrar(self):
        print("Hola registro")


    def start_gui(self):
        # Ventana principal
        
        self.r.title("PASTILLAS <3")
        self.r.geometry("480x360")

    # Frm Registros
        frm_registro = Frame(self.r)
        frm_registro.config(bg="white")


    # Nombre
        lbl_name = Label(frm_registro, text="Nombre: ")
        txt_name = Entry(frm_registro, textvariable=self.nombre)
        txt_name.grid(row=0, column=1)
        lbl_name.grid(row=0, column=0)

        # Cantidad
        lbl_cantidad = Label(frm_registro, text="Cantidad: ")
        txt_cantidad = Entry(frm_registro)
        lbl_cantidad.grid(row=1, column=0)
        txt_cantidad.grid(row=1, column=1)


    # Momento
        lbl_momento = Label(frm_registro, text="Momento: ")
        txt_momento = Entry(frm_registro)
        lbl_momento.grid(row=2, column=0)
        txt_momento.grid(row=2, column=1)

        # Registrar
        btn_registrar = Button(frm_registro, text="REGISTRAR")
        btn_registrar.config(command=lambda: self.registrar())
        btn_registrar.grid(row=3, column=0, columnspan=2)

    # Frm Info
        frm_info = Frame(self.r)
        frm_info.config(bg="black")

    # Title
        lblTitle = Label(self.r, text="PASTILLAS ALFA")
        lblTitle.config(fg=self.FONT_COLOR)
        lblTitle.pack()

        frm_registro.pack(side="left", fill='both', expand=True)
        frm_info.pack(side="right", fill='both', expand=True)
        self.r.mainloop()
