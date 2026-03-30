from pagos.pago import Pago


class PagoTransferencia(Pago):
    def __init__(self, monto, clabe, referencia="ABC123"):
        super().__init__(monto)
        self.clabe = clabe
        self.referencia = referencia

    def procesar_pago(self):
        return True
