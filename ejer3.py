# Diagrama de objetos representando la réplica de "La Gioconda"

class ObraDeArte:
    def __init__(self, titulo, autor, fecha, tecnica, subtecnica, soporte, descripcion, estado_conservacion, original=None):
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.tecnica = tecnica
        self.subtecnica = subtecnica
        self.soporte = soporte
        self.descripcion = descripcion
        self.estado_conservacion = estado_conservacion
        self.original = original  # Referencia a la obra original (si es réplica)

# Obra original
gioconda_original = ObraDeArte(
    titulo="La Gioconda",
    autor="Leonardo Da Vinci",
    fecha="1503-1516",
    tecnica="óleo",
    subtecnica="sfumato",
    soporte="madera de álamo",
    descripcion="Obra maestra expuesta en el Museo Louvre de París.",
    estado_conservacion="regular"
)

# Réplica estudiada
gioconda_replicada = ObraDeArte(
    titulo="La Gioconda (Réplica del Prado)",
    autor="Anónimo (alumno de la escuela de Leonardo)",
    fecha="1503-1516",
    tecnica="óleo",
    subtecnica="pincelada simple",
    soporte="madera de nogal",
    descripcion=(
        "Réplica más antigua conocida, procedente de las Colecciones Reales, "
        "expuesta en el Museo del Prado. Realizada por un discípulo de Leonardo "
        "al mismo tiempo que la original. Mejor estado de conservación que la original."
    ),
    estado_conservacion="muy bueno",
    original=gioconda_original
)

# Visualización simple del diagrama de objetos
def mostrar_obra(obra):
    print(f"Título: {obra.titulo}")
    print(f"Autor: {obra.autor}")
    print(f"Fecha: {obra.fecha}")
    print(f"Técnica: {obra.tecnica}")
    print(f"Sub-técnica: {obra.subtecnica}")
    print(f"Soporte: {obra.soporte}")
    print(f"Estado de conservación: {obra.estado_conservacion}")
    print(f"Descripción: {obra.descripcion}")
    if obra.original:
        print("\n--- Obra Original Relacionada ---")
        mostrar_obra(obra.original)

if __name__ == "__main__":
    mostrar_obra(gioconda_replicada)