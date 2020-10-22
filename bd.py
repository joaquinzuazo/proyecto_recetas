import sqlite3
from tkinter import messagebox


class BaseDatos():


    def __init__(self):
        """ creara la base de datos inicial del programa, ademas de intentar crear la tabla ingredientes.
            de no poder, mostrar un mensaje de error. """
        try:
            base=sqlite3.connect("recetas.db")
            cursor=base.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS ingredientes (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, producto INTEGER NOT NULL, cantidad REAL NOT NULL, precio REAL NOT NULL)")
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.")


    def conectar(self):
        """ realiza la conexion a la base de datos y devuelve la misma para utilizarse en todas las funciones que la requieran """
        
        base=sqlite3.connect("recetas.db")
        return base



# ------------ funciones ingredientes

    def agregarIngrediente(self,producto,cantidad,precio,top,tree):
        """ Llama a la funcion conectar e inserta los campos recibidos dentro de la tabla ingredientes, da un mensaje de guardado
            ademas limpia el treeview previamente para volver a cargar todos los datos con este nuevo incluido 
            de surgir algun error muestra un mensaje """
        
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("INSERT INTO ingredientes(producto, cantidad, precio)VALUES('"+producto.get()+"','"+cantidad.get()+"','"+precio.get()+"')")
            base.commit()
            messagebox.showinfo("Guardado","Se guardo con exito el ingrediente.",parent=top)
            producto.set("")
            cantidad.set("")
            precio.set("")
            tree.delete(*tree.get_children())
            self.mostrarIngredientes(tree)
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=top)
        

    def mostrarIngredientes(self,tree):
        """ recibe el treeview y carga dentro del mismo los datos que se encuentren en la tabla """

        base=self.conectar()
        cursor=base.cursor()
        cursor.execute("SELECT * FROM ingredientes")
        idd=cursor.fetchall()
        
        for x in idd:
            tree.insert("", "end", text=x[0], values=(x[1],x[2],x[3]))

        base.commit()
        return tree


    def editarIngrediente(self,producto,cantidad,precio,idd,top,tree):
        """ recibe los datos seleccionados en el treeview y actualiza los nuevos campos buscando el mismo ingrediente por el id """
        
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("UPDATE ingredientes SET cantidad='"+cantidad.get()+"', precio='"+precio.get()+"' where ingredientes.id='"+idd.get()+"'")
            messagebox.showinfo("Guardado","Se guardo con exito el ingrediente.\nAunque hayas modificado el nombre, este permanecera igual.",parent=top)
            base.commit()
            producto.set("")
            cantidad.set("")
            precio.set("")
            tree.delete(*tree.get_children())
            self.mostrarIngredientes(tree)
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=top)


    def borrarIngrediente(self,producto,cantidad,precio,idd,top,tree):
        """ recibe el ID seleccionado en el treeview y elimina el registro """
        
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("DELETE FROM ingredientes where ingredientes.id='"+idd.get()+"'")
            messagebox.showinfo("Eliminado","Se elimino con exito el ingrediente.",parent=top)
            base.commit()
            producto.set("")
            cantidad.set("")
            precio.set("")
            tree.delete(*tree.get_children())
            self.mostrarIngredientes(tree)
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=top)



# ------------ funciones recetas

    def nReceta(self,ventana,nombre):
        """ funcion que recibe el nombre ingresado y crea una nueva tabla (receta) a partir de este
            previamente verifica que el nombre no contenga espacios, para no producir error. """

        if " " in nombre.get():
            messagebox.showinfo("Error","El nombre de la receta no debe contener espacios.",parent=ventana)
        else:
            try:
                base=self.conectar()
                cursor=base.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS '"+nombre.get()+"' (ingre REAL NOT NULL, canReceta REAL NOT NULL)")
                base.commit()
                messagebox.showinfo("Creada","Se creo con exito la receta.",parent=ventana)
            except:
                messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=ventana)


    def eReceta(self,ventana,nombre):
        """ funcion que recibe el nombre ingresado y crea una nueva tabla (receta) a partir de este
            previamente verifica que el nombre no contenga espacios, para no producir error. """

        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("drop table '"+nombre.get()+"'")
            base.commit()
            messagebox.showinfo("Eliminada","Se elimino con exito la receta.",parent=ventana)
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=ventana)

    
    def verRecetas(self):
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("SELECT * FROM sqlite_master")
            idd=[]
            for t in cursor:
                if t[1] !="sqlite_sequence" and t[1] !="ingredientes":
                    idd.append(t[1])
            return idd
        except:
            pass


    def mostrarReceta(self,receta,tree):
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("SELECT * FROM '"+receta.get()+"'")
            ingreCant=cursor.fetchall()
            cursor.execute("SELECT * FROM ingredientes")
            ingre=cursor.fetchall()

            tree.delete(*tree.get_children())
            suma=0
            for i in ingreCant:
                for x in ingre:
                    if x[1] == i[0]:
                        aux=(i[1]*x[3])/x[2]
                        suma+=aux
                        tree.insert("", "end", text=x[0], values=(x[1],x[2],x[3],i[1],round(aux,2)))
            suma=round(suma,2)
            tree.insert("","end",text="Total",values=("","","","",suma))
            base.commit()
        except:
            pass


    def mostrarInReceta(self):
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("SELECT * FROM ingredientes")
            idd=cursor.fetchall()
            aux=[]
            for i in idd:
                aux.append(i[1])
            return aux
        except:
            pass


    def agregarInReceta(self,ventana,receta,ingrediente,cantidad,tree):
        try:
            base=self.conectar()
            cursor=base.cursor()
            cursor.execute("INSERT INTO '"+receta.get()+"'(ingre,canReceta)VALUES('"+ingrediente.get()+"','"+cantidad.get()+"')")
            base.commit()
            messagebox.showinfo("Guardado","Se guardo con exito el ingrediente.",parent=ventana)            
        except:
            messagebox.showinfo("Error","No se pudo establecer conexión con la base de datos.",parent=ventana)


    def mostrarRec(self):
        base=self.conectar()
        cursor=base.cursor()
        cursor.execute("SELECT * FROM sqlite_master")
        idd=[]
        for t in cursor:
            if t[1] !="sqlite_sequence" and t[1] !="ingredientes":
                idd.append(t[1])
        return idd
    