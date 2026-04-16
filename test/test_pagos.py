from servicios.gestores import GestorProductos


def test_agregar_producto_guarda_datos_correctamente():
    gestor = GestorProductos()

    producto = gestor.agregar("Laptop", 15000.0, 10)

    assert producto.id == 1
    assert producto.nombre == "Laptop"
    assert producto.precio == 15000.0
    assert producto.stock == 10
    assert producto.proveedor_id is None
    assert len(gestor.listar()) == 1
