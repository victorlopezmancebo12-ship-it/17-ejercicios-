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
