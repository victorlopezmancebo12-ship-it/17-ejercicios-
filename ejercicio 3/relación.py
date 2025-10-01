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