# Clase padre
class Animal:
    def __init__(self, nombre, ruido):  # 🔧 corregido: __init__ con doble guión bajo
        self.nombre = nombre
        self.ruido = ruido

    def sonido(self):  # 🔧 corregido: "soindo" → "sonido"
        print(f"{self.ruido}")

# Clase hija Perro
class Perro(Animal):
    def __init__(self, nombre, ruido, color):
        super().__init__(nombre, ruido)
        self.color = color

    def describe(self):
        print(f"{self.nombre} es de color {self.color}")

# Clase hija Gato 
class Gato(Animal):
    def __init__(self, nombre, ruido, tamaño):
        super().__init__(nombre, ruido)
        self.tamaño = tamaño

    def describe(self):
        print(f"{self.nombre} es un gato {self.tamaño}")

# Crear objetos
perro = Perro("Luna", "Guau", "gris")
gato = Gato("Michi", "Miau", "mediano")

# Usar métodos
perro.describe()
perro.sonido()

gato.describe()
gato.sonido()
