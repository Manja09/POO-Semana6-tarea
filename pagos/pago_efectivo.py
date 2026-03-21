from pagos.pago import Pago


class PagoEfectivo(Pago):
    def __init__(self, total: float, monto_recibido: float):
        super().__init__(total)
        self.monto_recibido = monto_recibido

    def procesar(self) -> tuple[bool, str]:
        if self.monto_recibido < self.total:
            return False, "Monto insuficiente para completar el pago."

        cambio = self.monto_recibido - self.total
        return True, f"Pago en efectivo aprobado. Cambio: ${cambio:.2f}"
