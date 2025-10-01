from datetime import date

class Persona:
    def __init__(self, nombre: str, apellido1: str, apellido2: str, fecha_nacimiento: date, sexo: str, identificacion: str):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.identificacion = identificacion