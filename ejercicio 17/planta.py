class Planta:
    def __init__(self, numero, estanterias):
        self.numero = numero
        self.estanterias = estanterias  # lista de Estanteria

    def capacidad_total(self):
        return sum(e.capacidad for e in self.estanterias)
