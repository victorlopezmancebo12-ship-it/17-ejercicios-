# Definición de valores correspondientes para cada figura geométrica

figuras = {
    "circulo": {
        "parametros": ["radio"],
        "descripcion": "Figura con todos los puntos a igual distancia del centro."
    },
    "rectangulo": {
        "parametros": ["base", "altura"],
        "descripcion": "Cuadrilátero con lados opuestos iguales y ángulos rectos."
    },
    "cuadrado": {
        "parametros": ["lado"],
        "descripcion": "Rectángulo con todos los lados iguales."
    },
    "elipse": {
        "parametros": ["eje_mayor", "eje_menor"],
        "descripcion": "Curva cerrada con dos ejes perpendiculares de diferente longitud."
    }
}

# Ejemplo de uso:
for figura, valores in figuras.items():
    print(f"{figura.capitalize()}:")
    print(f"  Parámetros: {', '.join(valores['parametros'])}")
    print(f"  Descripción: {valores['descripcion']}\n")