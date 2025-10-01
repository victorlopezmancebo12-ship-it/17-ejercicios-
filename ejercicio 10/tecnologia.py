class Tecnologia:
    """
    Representa una tecnología utilizada en el proyecto.
    Atributos:
        nombre (str): Nombre de la tecnología (ej. Python, Docker).
        tipo (str): Tipo de tecnología (ej. Lenguaje, Herramienta).
        proyectos (list[Proyecto]): Proyectos donde se usa la tecnología.
    """
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
        self.proyectos = []

    def asignar_proyecto(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)