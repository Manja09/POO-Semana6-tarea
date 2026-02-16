from pagos.pago import Pago


class PagoEfectivo(Pago):
    def __init__(self, total: float, monto_entregado: float):
        super().__init__(total)
        self.monto_entregado = monto_entregado

    def procesar(self) -> tuple[bool, str]:
        if self.monto_entregado < self.total:
            return False, "Efectivo insuficiente."
        cambio = self.monto_entregado - self.total
        return True, f"Pago en efectivo aprobado. Cambio: ${cambio:.2f}"
