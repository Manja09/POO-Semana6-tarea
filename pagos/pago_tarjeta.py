from pagos.pago import Pago


class PagoTarjeta(Pago):
    def __init__(self, monto: float, numero_tarjeta: str, cvv: str = "123"):
        super().__init__(monto)
        self.numero_tarjeta = numero_tarjeta
        self.cvv = cvv

    def procesar_pago(self):
        if len(self.numero_tarjeta) >= 16 and len(self.cvv) >= 3:
            return True, "Pago con tarjeta aprobado."
        return False, "Pago con tarjeta rechazado."
