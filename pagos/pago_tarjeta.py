from pagos.pago import Pago


class PagoTarjeta(Pago):
    def __init__(self, total: float, numero_tarjeta: str, cvv: str):
        super().__init__(total)
        self.numero_tarjeta = numero_tarjeta.replace(" ", "")
        self.cvv = cvv

    def procesar(self) -> tuple[bool, str]:
        if not (self.numero_tarjeta.isdigit() and len(self.numero_tarjeta) == 16):
            return False, "Tarjeta inválida (debe tener 16 dígitos)."
        if not (self.cvv.isdigit() and len(self.cvv) in (3, 4)):
            return False, "CVV inválido."
        return True, "Pago con tarjeta aprobado."
