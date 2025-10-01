class Estanteria:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.libros = []

    def agregar_libro(self, libro):
        if len(self.libros) < self.capacidad:
            self.libros.append(libro)
            return True
        return False
