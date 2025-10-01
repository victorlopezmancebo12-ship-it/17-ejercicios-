class Retrato(ObraArte):
    def __init__(self, titulo, autor, lugar_creacion, tecnica, material_soporte, ubicacion_actual, estado_conservacion, representado, existen_copias):
        super().__init__(titulo, autor, lugar_creacion, tecnica, material_soporte, ubicacion_actual, estado_conservacion)
        self.representado = representado
        self.existen_copias = existen_copias