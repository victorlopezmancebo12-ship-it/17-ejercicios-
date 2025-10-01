class Tecnologia:
    """
    Representa una tecnología utilizada en el proyecto.
    Atributos:
        nombre (str): Nombre de la tecnología (ej. Python, Docker).
        tipo (str): Tipo de tecnología (ej. Lenguaje, Herramienta).
    """
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo