# Definición de la clase Punto
class Punto:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.poligono = None  # Referencia al polígono al que pertenece



# Crear los puntos (A, B, C, D) donde el lado BC es común
A = Punto(0, 0)
B = Punto(1, 0)
C = Punto(1, 1)
D = Punto(0, 1)

# Triángulo 1: ABC
triangulo1 = Poligono([A, B, C])

# Triángulo 2: CBD (comparten el lado BC)
# NOTA: No se puede compartir los mismos objetos Punto entre dos polígonos según la implementación,
# así que creamos nuevos objetos para los puntos compartidos.
B2 = Punto(1, 0)
C2 = Punto(1, 1)
triangulo2 = Poligono([C2, B2, D])

# Diagrama de objetos (en texto):
# 
#   A(0,0)      B(1,0)      C(1,1)      D(0,1)
#     *----------*            *----------*
#     |         /             |         /
#     |        /              |        /
#     *-------*               *-------*
#    (Triángulo 1: ABC)      (Triángulo 2: CBD)
#
# Nota: B y C son puntos distintos en memoria para cumplir la restricción de la clase.