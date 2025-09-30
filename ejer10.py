class Participante:
    """
    Representa a una persona involucrada en el proyecto.
    Atributos:
        nombre (str): Nombre del participante.
        rol (str): Rol dentro del proyecto (ej. Desarrollador, Analista).
        experiencia (int): Años de experiencia profesional.
        proyectos (list[Proyecto]): Proyectos en los que participa.
        tareas (list[Tarea]): Tareas asignadas al participante.
    """
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia
        self.proyectos = []
        self.tareas = []

    def asignar_proyecto(self, proyecto):
        if proyecto not in self.proyectos:
            self.proyectos.append(proyecto)

    def asignar_tarea(self, tarea):
        if tarea not in self.tareas:
            self.tareas.append(tarea)

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

class Tarea:
    """
    Representa una tarea específica dentro del proyecto.
    Atributos:
        descripcion (str): Descripción de la tarea.
        responsable (Participante): Persona responsable de la tarea.
        estado (str): Estado de la tarea (ej. Pendiente, En progreso, Finalizada).
        proyecto (Proyecto): Proyecto al que pertenece la tarea.
    """
    def __init__(self, descripcion, responsable, estado, proyecto=None):
        self.descripcion = descripcion
        self.responsable = responsable
        self.estado = estado
        self.proyecto = proyecto
        # Asociaciones bidireccionales
        if responsable:
            responsable.asignar_tarea(self)
        if proyecto:
            proyecto.agregar_tarea(self)

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