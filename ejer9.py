from enum import Enum, auto

class Cuadro(Enum):
    LAS_MENINAS = auto()

class Artista(Enum):
    DIEGO_VELAZQUEZ = auto()

class Ubicacion(Enum):
    MUSEO_DEL_PRADO = auto()
    DESCONOCIDA = auto()

class Tecnica(Enum):
    OLEO = auto()

class Soporte(Enum):
    LIENZO = auto()

class EstadoConservacion(Enum):
    EXCELENTE = auto()
    BUENO = auto()
    REGULAR = auto()
    MALO = auto()

class ObraDeArte:
    def __init__(self, cuadro, representa, pintor, lugar_pintado, existen_copias,
                 tecnica, soporte, ubicacion_actual, estado_conservacion):
        self.cuadro = cuadro
        self.representa = representa
        self.pintor = pintor
        self.lugar_pintado = lugar_pintado
        self.existen_copias = existen_copias
        self.tecnica = tecnica
        self.soporte = soporte
        self.ubicacion_actual = ubicacion_actual
        self.estado_conservacion = estado_conservacion

# Ejemplo de instancia para "Las Meninas"
las_meninas = ObraDeArte(
    cuadro=Cuadro.LAS_MENINAS,
    representa="La familia de Felipe IV",
    pintor=Artista.DIEGO_VELAZQUEZ,
    lugar_pintado="Madrid, España",
    existen_copias=True,
    tecnica=Tecnica.OLEO,
    soporte=Soporte.LIENZO,
    ubicacion_actual=Ubicacion.MUSEO_DEL_PRADO,
    estado_conservacion=EstadoConservacion.EXCELENTE
)