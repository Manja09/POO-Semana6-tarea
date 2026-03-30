from pagos.pago_efectivo import PagoEfectivo
from pagos.pago_tarjeta import PagoTarjeta
from pagos.pago_transferencia import PagoTransferencia


def test_pago_efectivo():
    pago = PagoEfectivo(100, 150)
    resultado = pago.procesar_pago()
    assert resultado[0] is True


def test_pago_tarjeta():
    pago = PagoTarjeta(200, "1234567890123456")
    resultado = pago.procesar_pago()
    assert resultado[0] is True


def test_pago_transferencia():
    pago = PagoTransferencia(300, "CLABE1234567890")
    resultado = pago.procesar_pago()
    assert resultado[0] is True
