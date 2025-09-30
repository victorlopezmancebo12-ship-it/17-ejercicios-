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

class Consagracion:
    def __init__(self, fecha, descripcion):
        self.fecha = fecha
        self.descripcion = descripcion

class Material:
    def __init__(self, nombre):
        self.nombre = nombre

class Estilo:
    def __init__(self, nombre):
        self.nombre = nombre

class BienInteresCultural:
    def __init__(self, fecha_declaracion):
        self.fecha_declaracion = fecha_declaracion

# Instanciación de objetos según la descripción
consagraciones = [
    Consagracion("1128", "Primera consagración"),
    Consagracion("3 de abril de 1211", "Consagración definitiva")
]

materiales = [Material("granito")]

estilos = [
    Estilo("románico"),
    Estilo("gótico"),
    Estilo("barroco"),
    Estilo("plateresco"),
    Estilo("neoclásico")
]

bien_interes_cultural = BienInteresCultural("1896")

catedral_santiago = Catedral(
    nombre="Catedral de Santiago de Compostela",
    ubicacion="Santiago de Compostela",
    provincia="La Coruña",
    region="Galicia",
    pais="España",
    inicio_construccion=1075,
    fin_construccion=1211,
    consagraciones=consagraciones,
    materiales=materiales,
    estilos=estilos,
    bien_interes_cultural=bien_interes_cultural
)