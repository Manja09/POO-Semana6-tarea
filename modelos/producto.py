class Producto:
    def __init__(self, producto_id: int, nombre: str, precio: float, stock: int, proveedor_id: int | None = None):
        self.id = producto_id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor_id = proveedor_id  # opcional

    def __str__(self):
        prov = self.proveedor_id if self.proveedor_id is not None else "N/A"
        return f"[{self.id}] {self.nombre} | ${self.precio:.2f} | Stock: {self.stock} | Prov: {prov}"
