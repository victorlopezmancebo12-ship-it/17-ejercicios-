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
        if participante not in self.participantes:
            self.participantes.append(participante)
            participante.asignar_proyecto(self)

    def agregar_tecnologia(self, tecnologia):
        if tecnologia not in self.tecnologias:
            self.tecnologias.append(tecnologia)
            tecnologia.asignar_proyecto(self)

    def agregar_tarea(self, tarea):
        if tarea not in self.tareas:
            self.tareas.append(tarea)
            tarea.proyecto = self
            if tarea.responsable and self not in tarea.responsable.proyectos:
                tarea.responsable.asignar_proyecto(self)