from pagos.pago_efectivo import PagoEfectivo
from pagos.pago_tarjeta import PagoTarjeta
from pagos.pago_transferencia import PagoTransferencia


def test_pago_efectivo_aprobado():
    pago = PagoEfectivo(100.0, 150.0)
    assert pago.procesar()[0] is True


def test_pago_tarjeta_aprobado():
    pago = PagoTarjeta(200.0, "1234567812345678", "123")
    assert pago.procesar()[0] is True


def test_pago_transferencia_aprobado():
    pago = PagoTransferencia(300.0, "BBVA", "REF001")
    assert pago.procesar()[0] is True
