class Empleado(Persona):
    def __init__(self, identificacion, nombre, direccion):
        super().__init__(identificacion, nombre, direccion)
        self.prestamos = []
