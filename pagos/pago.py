class Pago:
    def __init__(self, total: float):
        self.total = total

    def procesar(self) -> tuple[bool, str]:
        raise NotImplementedError("Este método debe implementarse en las subclases.")
