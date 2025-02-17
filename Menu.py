import tkinter as tk
from tkinter import messagebox, simpledialog

######## COSNTRUCTOR INGENIERIA
class Ingenieria:
    def __init__(self, cedula, nombre, apellido, telefono, serial, semestre, promedio):
        self.cedula = cedula #### asigna un parametro al atributo de la instancia self...
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.serial = serial
        self.semestre = semestre
        self.promedio = promedio

######## METODO INGENIERIAA
class MetodoIngenieria:
    prestamos = []
    
    def menu_crud_ingenieria():
        while True:
            opciones = ["Registrar Prestamo", "Modificar Prestamo", "Eliminar Prestamo", "Buscar Prestamo", "Volver"]
            opcion = simpledialog.askinteger("Menu de Ingenierias", "Seleccione una opción:\n" + "\n".join(f"{i+1}. {opcion}" for i, opcion in enumerate(opciones)))
            
            if opcion == 1:
                messagebox.showinfo(" Registrar", MetodoIngenieria.registrar_prestamo())
            elif opcion == 2:
                codigo = simpledialog.askstring("Modificar",  "Ingrese el codigo o cedula del prestamo a buscar:")
                messagebox.showinfo("Modificar", MetodoIngenieria.actualizar_prestamo(codigo))
            elif opcion == 3:
                codigo = simpledialog.askstring("Eliminar",  "Ingrese el codigo o cedula del prestamo a buscar:")
                messagebox.showinfo("Eliminar", MetodoIngenieria.eliminar_registro(codigo))
            elif opcion == 4:
                codigo = simpledialog.askstring("Buscar", "Ingrese el codigo o cedula del prestamo a buscar:")
                messagebox.showinfo("Buscar", MetodoIngenieria.buscar_prestamo(codigo))
            elif opcion == 5:
                return
            else:
                messagebox.showerror("Error", "Opcion no válida")


    def registrar_prestamo():
        cedula = MetodoIngenieria.validar_entrada("Ingrese la cedula del estudiante:", True)
        if MetodoIngenieria.existe_prestamo(cedula):
            return "Este estudiante ya tiene un prestamo."
        
        nombre = MetodoIngenieria.validar_entrada("Ingrese el nombre del estudiante:")
        apellido = MetodoIngenieria.validar_entrada("Ingrese el apellido del estudiante:")
        telefono = MetodoIngenieria.validar_entrada("Ingrese el telefono del estudiante:", True)
        semestre = int(MetodoIngenieria.validar_entrada("Ingrese el semestre actual:", True))
        promedio = float(MetodoIngenieria.validar_entrada("Ingrese el promedio:", True))
        serial = MetodoIngenieria.validar_entrada("Ingrese el serial del equipo:")
        
        nuevo_prestamo = Ingenieria(cedula, nombre, apellido, telefono, serial, semestre, promedio)
        MetodoIngenieria.prestamos.append(nuevo_prestamo)
        return "¡Datos agregados con exito!"
 

    def actualizar_prestamo(codigo):
        for prestamo in MetodoIngenieria.prestamos:
            if prestamo.cedula == codigo or prestamo.serial == codigo:
                atributo = simpledialog.askstring("Actualizar", "Ingrese el atributo a modificar (nombre, apellido, telefono, semestre, promedio, serial):").lower()
                if hasattr(prestamo, atributo):
                    nuevo_valor = MetodoIngenieria.validar_entrada(f"Ingrese el nuevo valor para {atributo}:")
                    setattr(prestamo, atributo, nuevo_valor)
                    return f"¡{atributo.capitalize()} actualizado con exito!"
                return "Atributo no valido."
        return  "No se encontro ningún préstamo con ese codigo o cedula."
    

    def eliminar_registro(codigo):
        for i, prestamo in enumerate(MetodoIngenieria.prestamos):
            if prestamo.cedula == codigo or prestamo.serial == codigo:
                del MetodoIngenieria.prestamos[i]
                return "Prestamo eliminado con éxito."
        return "No se encontro ningún préstamo con ese codigo o cedula."
    
   
    def buscar_prestamo(codigo):
        for prestamo in MetodoIngenieria.prestamos:
            if prestamo.cedula == codigo or prestamo.serial == codigo:
                return f"Prestamo encontrado:\nCedula: {prestamo.cedula}\nNombre: {prestamo.nombre}\nApellido: {prestamo.apellido}\nTelefono: {prestamo.telefono}\nSemestre: {prestamo.semestre}\nPromedio: {prestamo.promedio}\nSerial: {prestamo.serial}"
        return "No se encontro ningun prestamo con este codigo o cedula."
    

    def existe_prestamo(cedula):
        return any(prestamo.cedula == cedula for prestamo in MetodoIngenieria.prestamos)
    
    
    def validar_entrada(mensaje, es_numerico=False):
        while True:
            entrada = simpledialog.askstring("Entrada", mensaje)
            if entrada is None or entrada.strip() == "":
                messagebox.showerror("Error", "Este campo no puede estar vacio.")
                continue
            if es_numerico:
                try:
                    if mensaje.lower().startswith("ingrese el semestre actual:"):
                        int(entrada)
                    else:
                        float(entrada) 
                except ValueError:
                    messagebox.showerror("¡Error!", "Debe ingresar un numero válido.")
                    continue
            return entrada

###### MENU PRINCIPAL
class Menu:
    def __init__(self):
        self.run()

    def run(self):
        messagebox.showinfo("PRESTAMOS", "¡BIENVENIDO A EQUIPOS ELECTRONICOS!")
        
        opciones = ["1. Prestamo a Ingenierias", "2. Prestamo a Diseño", "3. Gestión de Portatiles", "4. Gestión de Tabletas", "5. Inventario", "6. Salir"]
        
        while True:
            opcion = self.mostrar_menu(opciones)
            
            if opcion == 1:
                MetodoIngenieria.menu_crud_ingenieria() ### INGRESAMOS AL METODO DE INGENIERIAS ESPECIFICAMENTE AL MENU
            # elif opcion == 2:
            #     MetodoDiseno.menu_crud_diseno()
            # elif opcion == 3:
            #     MetodoComputador.menu_crud_computador()
            # elif opcion == 4:
            #     MetodoTablet.menu_crud_tableta()
            elif opcion == 5:
                pass 
            elif opcion == 6:
                messagebox.showinfo("Salir", "Saliendo del programa.\n¡Muchas gracias!")
                break
            else:
                messagebox.showerror("¡Error!", "Opción no valida. Por favor, seleccione una opción valida.")
    
    def mostrar_menu(self, opciones):
        root = tk.Tk()
        root.withdraw()
        return simpledialog.askinteger("Inventario", "Seleccione que desea realizar:\n" + "\n".join(opciones))

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    Menu()
    root.mainloop()