class Biblioteca:
    def __init__(self, plantas):
        self.plantas = plantas  # lista de Planta
        self.lectores = []
        self.empleados = []

    def capacidad_total(self):
        return sum(p.capacidad_total() for p in self.plantas)