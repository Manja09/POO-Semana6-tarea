from modelos.orden_compra import OrdenCompra
from modelos.producto import Producto
from pagos.pago_efectivo import PagoEfectivo
from pagos.pago_tarjeta import PagoTarjeta
from pagos.pago_transferencia import PagoTransferencia


def main() -> None:
    producto1 = Producto(1, "Laptop", 12000.0, 5, None)
    producto2 = Producto(2, "Mouse", 350.0, 10, None)

    orden = OrdenCompra()
    orden.agregar_producto(producto1)
    orden.agregar_producto(producto2)

    print(orden.mostrar_orden())

    total = orden.calcular_total()

    pago_efectivo = PagoEfectivo(total, 13000.0)
    print(pago_efectivo.procesar())

    pago_tarjeta = PagoTarjeta(total, "1234567812345678", "123")
    print(pago_tarjeta.procesar())

    pago_transferencia = PagoTransferencia(total, "BBVA", "REF123456")
    print(pago_transferencia.procesar())


if __name__ == "__main__":
    main()
