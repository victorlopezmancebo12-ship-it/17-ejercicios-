# Diagrama de objetos representado en Python usando clases y relaciones

class Persona:
    def __init__(self, nombre, apellido, apellido_soltera=None):
        self.nombre = nombre
        self.apellido = apellido
        self.apellido_soltera = apellido_soltera
        self.pareja = None
        self.hijos = []


carlos = Persona("Carlos", "Windsor")
diana = Persona("Diana", "de Gales", apellido_soltera="Spencer")
guillermo = Persona("Guillermo", "Windsor")
kate = Persona("Kate", "Windsor", apellido_soltera="Middleton")


carlos.pareja = diana
diana.pareja = carlos

guillermo.pareja = kate
kate.pareja = guillermo


carlos.hijos.append(guillermo)
diana.hijos.append(guillermo)


def mostrar_familia(persona, nivel=0):
    indent = "  " * nivel
    print(f"{indent}{persona.nombre} {persona.apellido}", end="")
    if persona.apellido_soltera:
        print(f" (nacida {persona.apellido_soltera})", end="")
    if persona.pareja:
        print(f" — casado/a con {persona.pareja.nombre} {persona.pareja.apellido}", end="")
    print()
    for hijo in persona.hijos:
        mostrar_familia(hijo, nivel + 1)


mostrar_familia(carlos)