# Clase padre
class Animal:
    def __init__(self, nombre, ruido):
        self.nombre = nombre
        self.ruido = ruido

    def sonido(self):
        print(f"{self.ruido}")

# Clase hija: Perro
class Perro(Animal):
    def __init__(self, nombre, ruido, color):
        super().__init__(nombre, ruido)
        self.color = color

    def describe(self):
        print(f"{self.nombre} es de color {self.color}")

# Clase hija: Gato
class Gato(Animal):
    def __init__(self, nombre, ruido, tamaño):
        super().__init__(nombre, ruido)
        self.tamaño = tamaño

    def describe(self):
        print(f"{self.nombre} es un gato {self.tamaño}")

# Clase hija: Pez
class Pez(Animal):
    def __init__(self, nombre, ruido, especie):
        super().__init__(nombre, ruido)
        self.especie = especie

    def describe(self):
        print(f"{self.nombre} es un pez de especie {self.especie}")


perro = Perro("Luna", "Guau", "gris")
gato = Gato("Michi", "Miau", "mediano")
pez = Pez("Nemo", "Blub blub", "Payaso")

perro.describe()
perro.sonido()

gato.describe()
gato.sonido()

pez.describe()
pez.sonido()
