class Poligono:
    def __init__(self, puntos):
        if len(puntos) < 3:
            raise ValueError("Un polígono debe tener al menos 3 puntos.")
        self.puntos = puntos

    def __repr__(self):
        return f"Poligono({self.puntos})"


# Ejemplo: cuadrado con vértices en (0,0), (0,1), (1,1), (1,0)
if __name__ == "__main__":
    p1 = Punto(0, 0)
    p2 = Punto(0, 1)
    p3 = Punto(1, 1)
    p4 = Punto(1, 0)
    cuadrado = Poligono([p1, p2, p3, p4])
    print(cuadrado)