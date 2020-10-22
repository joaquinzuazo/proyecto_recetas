from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from bd import BaseDatos


class Ventanas():

# ----------- ventana ingredientes

    def ingredientes(self,ventana):
        """ sub ventana de ingredientes, contiene en la misma un treeview que se busca al inicio si hay datos pre existentes
        campos para cargar datos nuevos y con el boton guardar enviarlos a la DB
        ademas haciendo doble clic sobre el tree, se puede seleccionar un dato ya existente para eliminarlo o editarlo """

        self.bd=BaseDatos()
        self.ventana=ventana
        
        self.v_ingre=Toplevel(ventana)
        self.v_ingre.title("Ingredientes")
        self.v_ingre.geometry("+350+200")

        Label(self.v_ingre,text="Agregar ingrediente",bg="violet",fg="white",font=("Arial",10)).grid(row=0,column=0,columnspan=3,sticky="nsew")

        self.L1=StringVar()
        Label(self.v_ingre,text="Producto:",font=("Arial",10)).grid(row=1,column=0,sticky=W)
        self.e1=Entry(self.v_ingre,textvariable=self.L1,width=20,font=("Arial",10))
        self.e1.grid(row=1,column=1,padx=50)

        self.L2=StringVar()
        Label(self.v_ingre,text="Cantidad:",font=("Arial",10)).grid(row=2,column=0,sticky=W)
        self.e2=Entry(self.v_ingre, textvariable=self.L2,width=20,font=("Arial",10))
        self.e2.grid(row=2,column=1,padx=50)

        self.L3=StringVar()
        Label(self.v_ingre,text="Precio:",font=("Arial",10)).grid(row=3,column=0,sticky=W)
        self.e3=Entry(self.v_ingre,textvariable=self.L3,width=20,font=("Arial",10))
        self.e3.grid(row=3,column=1,padx=50)

        Button(self.v_ingre,text="Guardar",command=lambda: self.bd.agregarIngrediente(self.L1,self.L2,self.L3,self.v_ingre,self.tree),font=("Arial",10)).grid(row=1,column=2,padx=10,pady=10,rowspan=3)
        
        Label(self.v_ingre,text="Haga doble clic sobre el ingrediente que desea editar o eliminar",bg="violet",fg="white",font=("Arial",9)).grid(row=4,column=0,columnspan=3,sticky="nsew",pady=10)
        Button(self.v_ingre,text="Editar",command=lambda: self.bd.editarIngrediente(self.L1,self.L2,self.L3,self.idd,self.v_ingre,self.tree),font=("Arial",10)).grid(row=5,column=0,padx=10,pady=10)
        Button(self.v_ingre,text="Eliminar",command=lambda: self.bd.borrarIngrediente(self.L1,self.L2,self.L3,self.idd,self.v_ingre,self.tree),font=("Arial",10)).grid(row=5,column=2,padx=10,pady=10)

        self.tree=ttk.Treeview(self.v_ingre)
        self.tree.grid(row=6,column=0,columnspan=3,pady=10,padx=10)
        self.tree["columns"]=("#1","#2","#3")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("#1", width=100, minwidth=100)
        self.tree.column("#2", width=100, minwidth=100)
        self.tree.column("#3", width=100, minwidth=100)
        self.tree.heading("#0",text="ID")
        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Cantidad")
        self.tree.heading("#3", text="Precio")
        self.tree.bind("<Double-1>", self.seleccion)
        self.bd.mostrarIngredientes(self.tree)

    def seleccion(self,evento):
        item=self.tree.selection()
        self.idd=StringVar()
        self.L1.set(self.tree.item(item)["values"][0])
        self.L2.set(self.tree.item(item)["values"][1])
        self.L3.set(self.tree.item(item)["values"][2])
        self.idd.set(self.tree.item(item)["text"])




# ----------- ventanas recetas

    def crearReceta(self,ventana):
        
        self.bd=BaseDatos()

        self.c_receta=Toplevel(ventana)
        self.c_receta.title("Nueva receta")
        self.c_receta.geometry("+350+200")

        Label(self.c_receta,text="Crear nueva receta",bg="violet",fg="white",font=("Arial",10)).grid(row=0,column=0,columnspan=3,sticky="nsew")

        self.L1=StringVar()
        Label(self.c_receta,text="Nombre:",font=("Arial",10)).grid(row=1,column=0,sticky=W)
        self.e1=Entry(self.c_receta,textvariable=self.L1,width=20,font=("Arial",10))
        self.e1.grid(row=1,column=1,padx=50)

        Button(self.c_receta,text="Crear",command=lambda:[self.bd.nReceta(self.c_receta,self.L1),self.crearRecetaIn(self.c_receta)],font=("Arial",10)).grid(row=1,column=2,padx=10,pady=10)


    def eliReceta(self,ventana):
        
        self.bd=BaseDatos()

        self.e_receta=Toplevel(ventana)
        self.e_receta.title("Nueva receta")
        self.e_receta.geometry("+350+200")

        Label(self.e_receta,text="Eliminar receta",bg="violet",fg="white",font=("Arial",10)).grid(row=0,column=0,columnspan=3,sticky="nsew")

        Label(self.e_receta,text="Receta:",font=("Arial",10)).grid(row=2,column=0,sticky=W)
        self.combo1=ttk.Combobox(self.e_receta,font=("Arial",10))
        self.combo1.grid(row=2,column=1,pady=10,padx=10)
        self.combo1["values"]=self.bd.mostrarRec()

        Button(self.e_receta,text="Eliminar",command=lambda:self.bd.eReceta(self.e_receta,self.combo1),font=("Arial",10)).grid(row=2,column=2,padx=10,pady=10)


    def crearRecetaIn(self,ventana):
        
        self.bd=BaseDatos()

        self.in_receta=Toplevel(ventana)
        self.in_receta.title("Nueva receta")
        self.in_receta.geometry("+350+200")

        Label(self.in_receta,text="Cargar ingredientes",bg="violet",fg="white",font=("Arial",10)).grid(row=1,column=0,columnspan=3,sticky="nsew",pady=10)

        Label(self.in_receta,text="Receta:",font=("Arial",10)).grid(row=2,column=0,sticky=W)
        self.combo1=ttk.Combobox(self.in_receta,font=("Arial",10))
        self.combo1.grid(row=2,column=1,pady=10,padx=10)
        self.combo1["values"]=self.bd.mostrarRec()

        Button(self.in_receta,text="Ver ingredientes\n ya cargados",command=lambda:self.bd.mostrarReceta(self.combo1,self.tree),font=("Arial",10)).grid(row=2,column=2,padx=10,pady=10)

        Label(self.in_receta,text="Ingrediente:",font=("Arial",10)).grid(row=3,column=0,sticky=W)
        self.combo=ttk.Combobox(self.in_receta,font=("Arial",10))
        self.combo.grid(row=3,column=1,pady=10,padx=10)
        self.combo["values"]=self.bd.mostrarInReceta()

        self.L4=StringVar()
        Label(self.in_receta,text="Cantidad en receta:",font=("Arial",10)).grid(row=4,column=0,sticky=W)
        self.e4=Entry(self.in_receta,textvariable=self.L4,width=20,font=("Arial",10))
        self.e4.grid(row=4,column=1,padx=50)

        Button(self.in_receta,text="Agregar",command=lambda:[self.bd.agregarInReceta(self.in_receta,self.combo1,self.combo,self.L4,self.tree),self.bd.mostrarReceta(self.combo1,self.tree)],font=("Arial",10)).grid(row=4,column=2,padx=10,pady=10)

        self.tree=ttk.Treeview(self.in_receta)
        self.tree.grid(row=5,column=0,rowspan=10,columnspan=3,pady=10,padx=10)
        self.tree["columns"]=("#1","#2","#3","#4","#5")
        self.tree.column("#0", width=60, minwidth=60)
        self.tree.column("#1", width=100, minwidth=100)
        self.tree.column("#2", width=50, minwidth=50)
        self.tree.column("#3", width=50, minwidth=50)
        self.tree.column("#4", width=120, minwidth=120)
        self.tree.column("#5", width=50, minwidth=50)
        self.tree.heading("#0",text="ID")
        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Cantidad")
        self.tree.heading("#3", text="Precio")
        self.tree.heading("#4", text="Cantidad en receta")
        self.tree.heading("#5", text="Costo")


    def verReceta(self,ventana):
        self.bd=BaseDatos()

        self.v_receta=Toplevel(ventana)
        self.v_receta.title("Recetas")
        self.v_receta.geometry("+350+200")

        Label(self.v_receta,text="Seleccionar receta",bg="violet",fg="white",font=("Arial",10)).grid(row=0,column=0,columnspan=3,sticky="nsew")
    
        self.combo=ttk.Combobox(self.v_receta,font=("Arial",10))
        self.combo.grid(row=1,column=0,pady=10,padx=10)
        self.combo["values"]=self.bd.verRecetas()

        Button(self.v_receta,text="Mostrar receta",command=lambda: self.bd.mostrarReceta(self.combo,self.tree), font=("Arial",10)).grid(row=1,column=1,padx=10,pady=10)

        self.tree=ttk.Treeview(self.v_receta)
        self.tree.grid(row=5,column=0,rowspan=10,columnspan=3,pady=10,padx=10)
        self.tree["columns"]=("#1","#2","#3","#4","#5")
        self.tree.column("#0", width=60, minwidth=60)
        self.tree.column("#1", width=100, minwidth=100)
        self.tree.column("#2", width=50, minwidth=50)
        self.tree.column("#3", width=50, minwidth=50)
        self.tree.column("#4", width=120, minwidth=120)
        self.tree.column("#5", width=50, minwidth=50)
        self.tree.heading("#0",text="ID")
        self.tree.heading("#1", text="Producto")
        self.tree.heading("#2", text="Cantidad")
        self.tree.heading("#3", text="Precio")
        self.tree.heading("#4", text="Cantidad en receta")
        self.tree.heading("#5", text="Costo")