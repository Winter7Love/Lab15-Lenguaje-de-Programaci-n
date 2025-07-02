import tkinter as tk

# Clase base
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

# Clase derivada
class Coche(Vehiculo):
    def __init__(self, marca, modelo, num_puertas, tipo_transmision):
        super().__init__(marca, modelo)
        self.num_puertas = num_puertas
        self.tipo_transmision = tipo_transmision

    def mostrar_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nPuertas: {self.num_puertas}\nTransmisión: {self.tipo_transmision}"

# Función que toma los datos del formulario
def crear_coche():
    marca = entry_marca.get()
    modelo = entry_modelo.get()
    puertas = entry_puertas.get()
    transmision = entry_transmision.get()

    coche = Coche(marca, modelo, puertas, transmision)
    resultado_label.config(text=coche.mostrar_info())

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Ingreso de datos del coche")

# Widgets
tk.Label(ventana, text="Marca:").pack()
entry_marca = tk.Entry(ventana)
entry_marca.pack()

tk.Label(ventana, text="Modelo:").pack()
entry_modelo = tk.Entry(ventana)
entry_modelo.pack()

tk.Label(ventana, text="Número de puertas:").pack()
entry_puertas = tk.Entry(ventana)
entry_puertas.pack()

# Variable para almacenar la opción seleccionada
opcion_transmision = tk.StringVar(ventana)
opcion_transmision.set("Manual")  # Valor inicial

tk.Label(ventana, text="Transmisión:").pack()

# Menú desplegable
menu_transmision = tk.OptionMenu(ventana, opcion_transmision, "Manual", "Automático")
menu_transmision.pack()


tk.Button(ventana, text="Crear coche", command=crear_coche).pack()

resultado_label = tk.Label(ventana, text="", fg="blue")
resultado_label.pack()

ventana.mainloop()
