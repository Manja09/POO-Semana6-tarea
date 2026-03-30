from pagos.pago import Pago


class PagoTransferencia(Pago):
    def __init__(self, monto: float, clabe: str, referencia: str = "REF123"):
        super().__init__(monto)
        self.clabe = clabe
        self.referencia = referencia

    def procesar_pago(self):
        if len(self.clabe) >= 10 and self.referencia:
            return True, "Pago por transferencia aprobado."
        return False, "Pago por transferencia rechazado."
