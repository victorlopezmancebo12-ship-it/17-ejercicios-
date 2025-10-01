class Persona:
    def __init__(self, nombre, apellido, apellido_de_soltera=None, conyuge=None, padres=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_de_soltera = apellido_de_soltera
        self.conyuge = conyuge
        self.padres = padres if padres else []



