from modelos.orden_compra import OrdenCompra
from modelos.producto import Producto


class GestorProductos:
    def __init__(self):
        self._productos: list[Producto] = []
        self._next_id: int = 1

    def listar(self) -> list[Producto]:
        return self._productos

    def agregar(
        self, nombre: str, precio: float, stock: int, proveedor_id: int | None = None
    ) -> Producto:
        nuevo_id: int = self._next_id
        prod = Producto(nuevo_id, nombre, precio, stock, proveedor_id)
        self._productos.append(prod)
        self._next_id += 1
        return prod

    def buscar_por_id(self, producto_id: int) -> Producto | None:
        for p in self._productos:
            if p.id == producto_id:
                return p
        return None

    def modificar(
        self,
        producto_id: int,
        nombre: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
        proveedor_id: int | None = None,
    ) -> bool:
        producto = self.buscar_por_id(producto_id)
        if producto is None:
            return False

        if nombre is not None:
            producto.nombre = nombre
        if precio is not None:
            producto.precio = precio
        if stock is not None:
            producto.stock = stock
        if proveedor_id is not None:
            producto.proveedor_id = proveedor_id

        return True

    def eliminar(self, producto_id: int) -> bool:
        producto = self.buscar_por_id(producto_id)
        if producto is None:
            return False

        self._productos.remove(producto)
        return True


class GestorOrdenes:
    def __init__(self):
        self._ordenes: list[OrdenCompra] = []

    def crear(self) -> OrdenCompra:
        orden = OrdenCompra()
        self._ordenes.append(orden)
        return orden

    def listar(self) -> list[OrdenCompra]:
        return self._ordenes
