from modelos.producto import Producto


class OrdenCompra:
    def __init__(self):
        self.productos: list[Producto] = []

    def agregar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def calcular_total(self) -> float:
        return sum(producto.precio for producto in self.productos)

    def mostrar_orden(self) -> str:
        if not self.productos:
            return "No hay productos en la orden."

        detalle = "\n".join(producto.mostrar_info() for producto in self.productos)
        total = self.calcular_total()
        return f"Productos:\n{detalle}\nTotal: ${total:.2f}"
