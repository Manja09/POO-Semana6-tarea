from pagos.pago import Pago


class PagoEfectivo(Pago):
    def __init__(self, monto, monto_recibido):
        super().__init__(monto)
        self.monto_recibido = monto_recibido

    def procesar_pago(self):
        if self.monto_recibido >= self.monto:
            return True
        return False
