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
