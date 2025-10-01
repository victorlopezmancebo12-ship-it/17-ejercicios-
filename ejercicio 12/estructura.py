class EstructuraArqueologica:
    def __init__(self, codigo, datacion, materiales, estructuras=None):
        """
        :param codigo: str, código identificador de la estructura
        :param datacion: str, datación de la estructura (ej. 'Siglo III a.C.')
        :param materiales: list[str], materiales que componen la estructura
        :param estructuras: list[EstructuraArqueologica], otras estructuras que la componen
        """
        self.codigo = codigo
        self.datacion = datacion
        self.materiales = materiales
        self.estructuras = estructuras if estructuras is not None else []

    def agregar_estructura(self, estructura):
        """Agrega una estructura a la lista de estructuras que la componen."""
        self.estructuras.append(estructura)