from tkinter import *
from v_principal import *
from v_secundaria import *
from bd import BaseDatos


if __name__ == '__main__':
    BaseDatos()
    ventana=Tk()
    Vista(ventana)
    ventana.mainloop()
    
    