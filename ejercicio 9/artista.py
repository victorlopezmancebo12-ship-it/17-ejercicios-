from enum import Enum, auto

class ObraArte:
    def __init__(self, titulo, autor, lugar_creacion, tecnica, material_soporte, ubicacion_actual, estado_conservacion):
        self.titulo = titulo
        self.autor = autor
        self.lugar_creacion = lugar_creacion
        self.tecnica = tecnica
        self.material_soporte = material_soporte
        self.ubicacion_actual = ubicacion_actual
        self.estado_conservacion = estado_conservacion



# Ejemplo: La Gioconda (Mona Lisa)
gioconda = Retrato(
    titulo="La Gioconda",
    autor="Leonardo da Vinci",
    lugar_creacion="Florencia, Italia",
    tecnica=Tecnica.OLEO,
    material_soporte=MaterialSoporte.MADERA,
    ubicacion_actual=Ubicacion.LOUVRE,
    estado_conservacion=EstadoConservacion.BUENO,
    representado="Lisa Gherardini",
    existen_copias=True
)