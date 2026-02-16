class Cliente:
    def __init__(self, cliente_id: int, nombre: str, telefono: str):
        self.id = cliente_id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"[{self.id}] {self.nombre} - Tel: {self.telefono}"
