from modelos.cliente import Cliente
from modelos.proveedor import Proveedor
from modelos.producto import Producto
from modelos.orden_compra import OrdenCompra


class GestorClientes:
    def __init__(self):
        self._clientes: list[Cliente] = []
        self._next_id = 1

    def listar(self):
        return self._clientes

    def agregar(self, nombre: str, telefono: str):
        c = Cliente(self._next_id, nombre, telefono)
        self._clientes.append(c)
        self._next_id += 1
        return c

    def buscar_por_id(self, cliente_id: int):
        for c in self._clientes:
            if c.id == cliente_id:
                return c
        return None

    def modificar(self, cliente_id: int, nombre: str, telefono: str) -> bool:
        c = self.buscar_por_id(cliente_id)
        if not c:
            return False
        c.nombre = nombre
        c.telefono = telefono
        return True

    def eliminar(self, cliente_id: int) -> bool:
        c = self.buscar_por_id(cliente_id)
        if not c:
            return False
        self._clientes.remove(c)
        return True


class GestorProveedores:
    def __init__(self):
        self._proveedores: list[Proveedor] = []
        self._next_id = 1

    def listar(self):
        return self._proveedores

    def agregar(self, nombre: str, telefono: str):
        p = Proveedor(self._next_id, nombre, telefono)
        self._proveedores.append(p)
        self._next_id += 1
        return p

    def buscar_por_id(self, proveedor_id: int):
        for p in self._proveedores:
            if p.id == proveedor_id:
                return p
        return None

    def modificar(self, proveedor_id: int, nombre: str, telefono: str) -> bool:
        p = self.buscar_por_id(proveedor_id)
        if not p:
            return False
        p.nombre = nombre
        p.telefono = telefono
        return True

    def eliminar(self, proveedor_id: int) -> bool:
        p = self.buscar_por_id(proveedor_id)
        if not p:
            return False
        self._proveedores.remove(p)
        return True


class GestorProductos:
    def __init__(self):
        self._productos: list[Producto] = []
        self._next_id = 1

    def listar(self):
        return self._productos

    def agregar(self, nombre: str, precio: float, stock: int, proveedor_id: int | None = None):
        prod = Producto(self._next_id, nombre, precio, stock, proveedor_id)
        self._productos.append(prod)
        self._next_id += 1
        return prod

    def buscar_por_id(self, producto_id: int):
        for p in self._productos:
            if p.id == producto_id:
                return p
        return None

    def modificar(self, producto_id: int, nombre: str, precio: float, stock: int, proveedor_id: int | None = None) -> bool:
        p = self.buscar_por_id(producto_id)
        if not p:
            return False
        p.nombre = nombre
        p.precio = precio
        p.stock = stock
        p.proveedor_id = proveedor_id
        return True

    def eliminar(self, producto_id: int) -> bool:
        p = self.buscar_por_id(producto_id)
        if not p:
            return False
        self._productos.remove(p)
        return True


class GestorOrdenes:
    def __init__(self):
        self._ordenes: list[OrdenCompra] = []
        self._next_id = 1

    def crear(self, cliente_id: int):
        o = OrdenCompra(self._next_id, cliente_id)
        self._ordenes.append(o)
        self._next_id += 1
        return o

    def listar(self):
        return self._ordenes
