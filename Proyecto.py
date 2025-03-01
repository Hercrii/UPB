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
    Bicicletas = []
    ventana_actual = None

    @staticmethod
    def menu_principal():
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
        if GestionBicicletas.ventana_actual:
            GestionBicicletas.ventana_actual.destroy()
        registro_win = ctk.CTkToplevel()
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
        
        def registrar():
            bicicleta = Bicicleta(
                entradas["serial"].get(), entradas["nombre"].get(), entradas["color"].get(),
                entradas["modelo"].get(), entradas["marca"].get(), entradas["llanta"].get()
            )
            GestionBicicletas.Bicicletas.append(bicicleta)
            registro_win.destroy()
            GestionBicicletas.menu_principal()
        
        ctk.CTkButton(registro_win, text="Guardar", command=registrar).pack(pady=10)

    @staticmethod
    def ver_bicicletas():
        if GestionBicicletas.ventana_actual:
            GestionBicicletas.ventana_actual.destroy()
        ver_win = ctk.CTkToplevel()
        ver_win.geometry("500x400")
        ver_win.title("Bicicletas Registradas")
        GestionBicicletas.ventana_actual = ver_win
        
        for bicicleta in GestionBicicletas.Bicicletas:
            info = f"{bicicleta.serial} - {bicicleta.nombre} - Color: {bicicleta.color} - Modelo: {bicicleta.modelo} - Marca: {bicicleta.marca} - Llanta: {bicicleta.llanta}"
            ctk.CTkLabel(ver_win, text=info).pack()
        
        def volver():
            ver_win.destroy()
            GestionBicicletas.menu_principal()
        
        ctk.CTkButton(ver_win, text="Volver", command=volver).pack(pady=10)

    @staticmethod
    def modificar_bicicleta():
        if GestionBicicletas.ventana_actual:
            GestionBicicletas.ventana_actual.destroy()
        mod_win = ctk.CTkToplevel()
        mod_win.geometry("400x300")
        mod_win.title("Modificar Bicicleta")
        GestionBicicletas.ventana_actual = mod_win
        
        ctk.CTkLabel(mod_win, text="Ingrese el serial de la bicicleta:").pack()
        entrada_serial = ctk.CTkEntry(mod_win)
        entrada_serial.pack()
        
        def modificar():
            serial = entrada_serial.get()
            bicicleta = next((b for b in GestionBicicletas.Bicicletas if b.serial == serial), None)
            if not bicicleta:
                ctk.CTkLabel(mod_win, text="Bicicleta no encontrada.", fg_color="red").pack()
                return
            
            mod_sub_win = ctk.CTkToplevel()
            mod_sub_win.geometry("400x300")
            mod_sub_win.title("Seleccionar campo a modificar")
            
            opciones = ["nombre", "color", "modelo", "marca", "llanta"]
            variable = ctk.StringVar(value=opciones[0])
            dropdown = ctk.CTkComboBox(mod_sub_win, values=opciones, variable=variable)
            dropdown.pack()
            
            ctk.CTkLabel(mod_sub_win, text="Nuevo valor:").pack()
            nueva_entrada = ctk.CTkEntry(mod_sub_win)
            nueva_entrada.pack()
            
            def guardar_cambio():
                setattr(bicicleta, variable.get(), nueva_entrada.get())
                mod_sub_win.destroy()
                mod_win.destroy()
                GestionBicicletas.menu_principal()
            
            ctk.CTkButton(mod_sub_win, text="Guardar", command=guardar_cambio).pack()
        
        ctk.CTkButton(mod_win, text="Buscar", command=modificar).pack(pady=5)
        
        def volver():
            mod_win.destroy()
            GestionBicicletas.menu_principal()
        
        ctk.CTkButton(mod_win, text="Volver", command=volver).pack(pady=10)

if __name__ == "__main__":
    GestionBicicletas.menu_principal()
