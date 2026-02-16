from modelos.producto import Producto


class ItemOrden:
    def __init__(self, producto: Producto, cantidad: int):
        self.producto = producto
        self.cantidad = cantidad

    def subtotal(self) -> float:
        return self.producto.precio * self.cantidad

    def __str__(self):
        return f"{self.producto.nombre} x{self.cantidad} = ${self.subtotal():.2f}"


class OrdenCompra:
    def __init__(self, orden_id: int, cliente_id: int):
        self.id = orden_id
        self.cliente_id = cliente_id
        self.items: list[ItemOrden] = []
        self.estado = "PENDIENTE"  # PENDIENTE / PAGADA / ERROR

    def agregar_item(self, producto: Producto, cantidad: int) -> bool:
        if cantidad <= 0:
            return False
        if producto.stock < cantidad:
            return False

        producto.stock -= cantidad
        self.items.append(ItemOrden(producto, cantidad))
        return True

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items)

    def __str__(self):
        lineas = [f"Orden #{self.id} | Cliente: {self.cliente_id} | Estado: {self.estado}"]
        for it in self.items:
            lineas.append(f"  - {it}")
        lineas.append(f"TOTAL: ${self.total():.2f}")
        return "\n".join(lineas)
