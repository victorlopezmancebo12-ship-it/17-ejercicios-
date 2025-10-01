class Poligono:
    def __init__(self, puntos: list[Punto]):
        if len(puntos) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")
        self.puntos = puntos
        for punto in puntos:
            if punto.poligono is not None:
                raise ValueError("Un punto solo puede pertenecer a un polígono.")
            punto.poligono = self