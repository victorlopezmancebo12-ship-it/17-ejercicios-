
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