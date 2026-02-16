from pagos.pago import Pago


class PagoTransferencia(Pago):
    def __init__(self, total: float, referencia: str):
        super().__init__(total)
        self.referencia = referencia.strip()

    def procesar(self) -> tuple[bool, str]:
        if len(self.referencia) < 6:
            return False, "Referencia inválida (mínimo 6 caracteres)."
        return True, "Transferencia aprobada."
