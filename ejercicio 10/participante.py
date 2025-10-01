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




