from pagos.pago import Pago


class PagoTarjeta(Pago):
    def __init__(self, monto, numero_tarjeta, cvv="123"):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv

    def procesar_pago(self):
        return True
