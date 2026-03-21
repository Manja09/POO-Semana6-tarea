from pagos.pago import Pago


class PagoTransferencia(Pago):
    def __init__(self, total: float, banco: str, referencia: str):
        super().__init__(total)
        self.banco = banco
        self.referencia = referencia

    def procesar(self) -> tuple[bool, str]:
        if self.total <= 0:
            return False, "El total debe ser mayor que cero."

        if not self.banco.strip():
            return False, "El banco no puede estar vacío."

        if not self.referencia.strip():
            return False, "La referencia no puede estar vacía."

        return True, "Pago por transferencia aprobado."
