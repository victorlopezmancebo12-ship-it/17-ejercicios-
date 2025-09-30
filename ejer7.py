

class Participante:
    """
    Representa a una persona involucrada en el proyecto.
    Atributos:
        nombre (str): Nombre del participante.
        rol (str): Rol dentro del proyecto (ej. Desarrollador, Analista).
        experiencia (int): Años de experiencia profesional.
    """
    def __init__(self, nombre, rol, experiencia):
        self.nombre = nombre
        self.rol = rol
        self.experiencia = experiencia

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

class Tarea:
    """
    Representa una tarea específica dentro del proyecto.
    Atributos:
        descripcion (str): Descripción de la tarea.
        responsable (Participante): Persona responsable de la tarea.
        estado (str): Estado de la tarea (ej. Pendiente, En progreso, Finalizada).
    """
    def __init__(self, descripcion, responsable, estado):
        self.descripcion = descripcion
        self.responsable = responsable
        self.estado = estado

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