from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from v_secundaria import Ventanas


class Vista():


        def __init__(self,ventana):
            """  ventana principal, solo con fondo y barra de menu para las distintas opciones """
            

            self.ventana=ventana
            self.vsecu=Ventanas()

            self.ventana.title("Recetas - Página principal")
            self.ventana.geometry("450x450+300+150")

            barra=Menu(self.ventana)
            self.ventana.config(menu=barra)
            self.imagen=PhotoImage(file="muf.png")
            Label(self.ventana,image=self.imagen).grid(row=0,column=0)

            archivo=Menu(barra, tearoff=0,font=("Arial",10))
            barra.add_cascade(label="Menu",menu=archivo,font=("Arial",10))
            archivo.add_command(label="Ingedientes",command=lambda: self.vsecu.ingredientes(self.ventana),font=("Arial",10))
            
            opciones=Menu(barra, tearoff=0,font=("Arial",10))
            opciones.add_command(label="Nueva",command=lambda: self.vsecu.crearReceta(self.ventana),font=("Arial",10))
            opciones.add_command(label="Cargar ingredientes",command=lambda: self.vsecu.crearRecetaIn(self.ventana),font=("Arial",10))
            opciones.add_command(label="Ver receta",command=lambda: self.vsecu.verReceta(self.ventana),font=("Arial",10))
            opciones.add_command(label="Eliminar receta",command=lambda: self.vsecu.eliReceta(self.ventana),font=("Arial",10))
            archivo.add_cascade(label="Recetas", menu=opciones,font=("Arial",10))
            archivo.add_separator()
            archivo.add_command(label="Salir",command=lambda: exit(),font=("Arial",10))

            #archivo_in=Menu(barra, tearoff=0,font=("Arial",10))
            #barra.add_cascade(label="Ayuda",menu=archivo_in,font=("Arial",10))
            #archivo_in.add_command(label="Acerca de",command=lambda: Ventanas.instrucciones(self,self.ventana),font=("Arial",10))