class Proyecto:
    """
    Representa un proyecto profesional.
    Atributos:
        nombre (str): Nombre del proyecto.
        descripcion (str): Breve descripción del proyecto.
        duracion_meses (int): Duración estimada en meses.
        participantes (list[Participante]): Lista de personas involucradas.
        tecnologias (list[Tecnologia]): Tecnologías utilizadas.
        tareas (list[Tarea]): Tareas del proyecto.
    """
    def __init__(self, nombre, descripcion, duracion_meses):
        self.nombre = nombre
        self.descripcion = descripcion
        self.duracion_meses = duracion_meses
        self.participantes = []
        self.tecnologias = []
        self.tareas = []

    def agregar_participante(self, participante):
        self.participantes.append(participante)

    def agregar_tecnologia(self, tecnologia):
        self.tecnologias.append(tecnologia)

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)