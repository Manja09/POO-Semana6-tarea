class Producto:
    def __init__(
        self,
        id: int,
        nombre: str,
        precio: float,
        stock: int,
        proveedor_id: int | None = None,
    ):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.proveedor_id = proveedor_id

    def mostrar_info(self) -> str:
        return (
            f"{self.id} - {self.nombre} - ${self.precio:.2f} - "
            f"Stock: {self.stock} - Proveedor: {self.proveedor_id}"
        )
