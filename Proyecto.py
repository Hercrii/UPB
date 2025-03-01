import customtkinter as ctk

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class Bicicleta:
    def __init__(self, serial, nombre, color, modelo, marca, llanta):
        self.serial = serial
        self.nombre = nombre
        self.color = color
        self.modelo = modelo
        self.marca = marca
        self.llanta = llanta

class GestionBicicletas:
    bicicletas = []
    ventana_actual = None

    @staticmethod
    def cerrar_ventana_anterior():
        if GestionBicicletas.ventana_actual:
            GestionBicicletas.ventana_actual.destroy()

    @staticmethod
    def menu_principal():
        GestionBicicletas.cerrar_ventana_anterior()
        GestionBicicletas.ventana_actual = ctk.CTk()
        GestionBicicletas.ventana_actual.geometry("400x500")
        GestionBicicletas.ventana_actual.title("Menú Principal")

        ctk.CTkLabel(GestionBicicletas.ventana_actual, text="Gestión de Bicicletas", font=("Arial", 16)).pack(pady=10)
        
        ctk.CTkButton(GestionBicicletas.ventana_actual, text="Registrar bicicleta", command=GestionBicicletas.abrir_registro).pack(pady=5)
        ctk.CTkButton(GestionBicicletas.ventana_actual, text="Ver Bicicletas", command=GestionBicicletas.ver_bicicletas).pack(pady=5)
        ctk.CTkButton(GestionBicicletas.ventana_actual, text="Modificar Bicicleta", command=GestionBicicletas.modificar_bicicleta).pack(pady=5)
        ctk.CTkButton(GestionBicicletas.ventana_actual, text="Salir", command=GestionBicicletas.ventana_actual.quit).pack(pady=5)
        
        GestionBicicletas.ventana_actual.mainloop()
    
    @staticmethod
    def abrir_registro():
        GestionBicicletas.cerrar_ventana_anterior()
        registro_win = ctk.CTk()
        registro_win.geometry("400x500")
        registro_win.title("Registrar Bicicleta")
        GestionBicicletas.ventana_actual = registro_win
        
        campos = ["Serial", "Nombre", "Color", "Modelo", "Marca", "Llanta"]
        entradas = {}
        
        for campo in campos:
            ctk.CTkLabel(registro_win, text=f"{campo}:").pack()
            entrada = ctk.CTkEntry(registro_win)
            entrada.pack()
            entradas[campo.lower()] = entrada
        
        mensaje_error = ctk.CTkLabel(registro_win, text="", text_color="red")
        mensaje_error.pack()

        def registrar():
            if any(not entrada.get().strip() for entrada in entradas.values()):
                mensaje_error.configure(text="Todos los campos son obligatorios")
                return
            bicicleta = Bicicleta(
                entradas["serial"].get(), entradas["nombre"].get(), entradas["color"].get(),
                entradas["modelo"].get(), entradas["marca"].get(), entradas["llanta"].get()
            )
            GestionBicicletas.bicicletas.append(bicicleta)
            registro_win.destroy()
            GestionBicicletas.menu_principal()
        
        ctk.CTkButton(registro_win, text="Guardar", command=registrar).pack(pady=10)
        registro_win.mainloop()

    @staticmethod
    def ver_bicicletas():
        GestionBicicletas.cerrar_ventana_anterior()
        ver_win = ctk.CTk()
        ver_win.geometry("500x400")
        ver_win.title("Bicicletas Registradas")
        GestionBicicletas.ventana_actual = ver_win
        
        for bicicleta in GestionBicicletas.bicicletas:
            info = f"{bicicleta.serial} - {bicicleta.nombre} - Color: {bicicleta.color} - Modelo: {bicicleta.modelo} - Marca: {bicicleta.marca} - Llanta: {bicicleta.llanta}"
            ctk.CTkLabel(ver_win, text=info).pack()
        
        ctk.CTkButton(ver_win, text="Volver", command=GestionBicicletas.menu_principal).pack(pady=10)
        ver_win.mainloop()

    @staticmethod
    def modificar_bicicleta():
        GestionBicicletas.cerrar_ventana_anterior()
        mod_win = ctk.CTk()
        mod_win.geometry("400x300")
        mod_win.title("Modificar Bicicleta")
        GestionBicicletas.ventana_actual = mod_win
        
        ctk.CTkLabel(mod_win, text="Ingrese el serial de la bicicleta:").pack()
        entrada_serial = ctk.CTkEntry(mod_win)
        entrada_serial.pack()
        mensaje_error = ctk.CTkLabel(mod_win, text="", text_color="red")
        mensaje_error.pack()
        
        def modificar():
            serial = entrada_serial.get()
            bicicleta = next((b for b in GestionBicicletas.bicicletas if b.serial == serial), None)
            if not bicicleta:
                mensaje_error.configure(text="Bicicleta no encontrada.")
                return
            
            opciones = ["nombre", "color", "modelo", "marca", "llanta"]
            variable = ctk.StringVar(value=opciones[0])
            ctk.CTkLabel(mod_win, text="Seleccionar campo a modificar:").pack()
            dropdown = ctk.CTkComboBox(mod_win, values=opciones, variable=variable)
            dropdown.pack()
            
            ctk.CTkLabel(mod_win, text="Nuevo valor:").pack()
            nueva_entrada = ctk.CTkEntry(mod_win)
            nueva_entrada.pack()
            
            def guardar_cambio():
                if not nueva_entrada.get().strip():
                    mensaje_error.configure(text="El valor no puede estar vacío")
                    return
                setattr(bicicleta, variable.get(), nueva_entrada.get())
                mod_win.destroy()
                GestionBicicletas.menu_principal()
            
            ctk.CTkButton(mod_win, text="Guardar", command=guardar_cambio).pack()
        
        ctk.CTkButton(mod_win, text="Buscar", command=modificar).pack(pady=5)
        mod_win.mainloop()

if __name__ == "__main__":
    GestionBicicletas.menu_principal()
