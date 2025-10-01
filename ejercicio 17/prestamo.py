class Prestamo:
    def __init__(self, libro, persona, fecha_prestamo, es_empleado=False):
        self.libro = libro
        self.persona = persona
        self.fecha_prestamo = fecha_prestamo
        self.es_empleado = es_empleado
        self.fecha_entrega = self.calcular_fecha_entrega()

    def calcular_fecha_entrega(self):
        dias = 60 if self.es_empleado else 30
        return self.fecha_prestamo + timedelta(days=dias)

    def esta_vencido(self, fecha_actual):
        return fecha_actual > self.fecha_entrega

    def dias_retraso(self, fecha_actual):
        if self.esta_vencido(fecha_actual):
            return (fecha_actual - self.fecha_entrega).days
        return 0