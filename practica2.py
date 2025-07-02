# Clase padre
class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel

    def descripcion(self):
        print(f"{self.nombre} es de tipo {self.tipo} y tiene nivel {self.nivel}")

# Clase hija: PokemonLegendario
class PokemonLegendario(Pokemon):
    def __init__(self, nombre, tipo, nivel, habilidad):
        super().__init__(nombre, tipo, nivel)
        self.habilidad = habilidad

    def mostrar_habilidad(self):
        print(f"{self.nombre} tiene una habilidad legendaria: {self.habilidad}")

pikachu = Pokemon("Pikachu", "Eléctrico", 35)
bulbasaur = Pokemon("Bulbasaur", "Planta", 20)
charmander = Pokemon("Charmander", "Fuego", 25)
mewtwo = PokemonLegendario("Mewtwo", "Psíquico", 70, "Telequinesis")

pikachu.descripcion()
bulbasaur.descripcion()
charmander.descripcion()
mewtwo.descripcion()
mewtwo.mostrar_habilidad()
