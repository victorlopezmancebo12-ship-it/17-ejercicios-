# Diagrama de objetos usando clases en Python para representar la información dada

class Catedral:
    def __init__(self, nombre, ubicacion, provincia, region, pais, inicio_construccion, fin_construccion, consagraciones, materiales, estilos, bien_interes_cultural):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.provincia = provincia
        self.region = region
        self.pais = pais
        self.inicio_construccion = inicio_construccion
        self.fin_construccion = fin_construccion
        self.consagraciones = consagraciones  # lista de Consagracion
        self.materiales = materiales          # lista de Material
        self.estilos = estilos                # lista de Estilo
        self.bien_interes_cultural = bien_interes_cultural




