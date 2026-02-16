class Proveedor:
    def __init__(self, proveedor_id: int, nombre: str, telefono: str):
        self.id = proveedor_id
        self.nombre = nombre
        self.telefono = telefono

    def __str__(self):
        return f"[{self.id}] {self.nombre} - Tel: {self.telefono}"
